"""
test_OrangeHRM.py - Script to validate Login and PIM test cases
"""

# Import necessary libraries
from Locators.OrangeHRM_Locators import Locators
from Utilities.excel_functions import Excel_Operations
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Load test data from Excel file
test_data_excel_file = Locators().excel_file
test_sheet_number = Locators().sheet_number

# Create an object for the excel class
excel_handler = Excel_Operations(test_data_excel_file,test_sheet_number)

# Define a test class for OrangeHRM login
class Test_OrangeHRM_Login():
    # Fixture to set up and tear down the browser
    @pytest.fixture
    def boot(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,60)
        self.driver.get(Locators.url)
        yield
        # Close the browser after the test is complete
        self.driver.close()

    # Test case for valid login
    def test_TC_Login_01(self,boot):
        """
        TC ID - TC_Login_01
        Test Objective - Successful Employee Login to OrangeHRM Portal
        """
        try:
            # Read test data from Excel file
            test_username = excel_handler.read_data(2,7)
            test_password = excel_handler.read_data(2,8)

            # Enter the username and password
            valid_username = self.wait.until(EC.presence_of_element_located((By.NAME,Locators().username)))
            valid_username.send_keys(test_username)
            valid_password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            valid_password.send_keys(test_password)

            # Click the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().submit_button)))
            login_button.click()

        # Check if the login was successful
            if Locators().dashboard_url == self.driver.current_url:
                print("SUCCESS : Login with Valid Username {a} & Password {b}".format(a=test_username, b=test_password))
                excel_handler.write_data(2,12,Locators.pass_data)
                # Assert that Login is successful
                assert True, "Login successful"
            else:
                print("ERROR : Unable to Login with Username {a} & Password {b}".format(a=test_username, b=test_password))
                excel_handler.write_data(2, 12, Locators.fail_data)
                # Assert that Login is unsuccessful
                assert False, "Login Unsuccessful with valid username & password"

        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    # Test case for invalid login
    def test_TC_Login_02(self,boot):
        """
        TC ID - TC_Login_02
        Test Objective - Invalid Employee login to OrangeHRM Portal
        """
        try:
            # Read test data from Excel file
            test_username = excel_handler.read_data(3,7)
            test_password = excel_handler.read_data(3,8)

            # Enter the username and password
            invalid_username = self.wait.until(EC.presence_of_element_located((By.NAME,Locators().username)))
            invalid_username.send_keys(test_username)
            invalid_password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            invalid_password.send_keys(test_password)

            # Click the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().submit_button)))
            login_button.click()

            # Check if the login was successful
            if Locators().url == self.driver.current_url:
                print("ERROR : Login unsuccessful with invalid username {a} & Password {b}".format(a=test_username, b=test_password))
                excel_handler.write_data(3,12,Locators().pass_data)
                # Assert that Login is unsuccessful
                assert True, "Login failed with invalid username and password"
                self.driver.refresh()
            else:
                print("ERROR : Login successful with invalid Username {a} & Password {b}".format(a=test_username, b=test_password))
                excel_handler.write_data(2, 12, Locators.fail_data)
                # Assert that Login is successful
                assert False, "Login Successful with invalid username & password"

        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    # Test case for editing employee details
    def test_TC_PIM_02(self,boot):
        """
        TC ID - TC_Login_03
        Test Objective - Edit an existing employee in the PIM module
        """
        try:
            # Initialize the ActionChains object
            actions = ActionChains(self.driver)

            # Read test data from Excel file
            test_username = excel_handler.read_data(2, 7)
            test_password = excel_handler.read_data(2, 8)

            # Enter the username and password
            valid_username = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().username)))
            valid_username.send_keys(test_username)
            valid_password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            valid_password.send_keys(test_password)

            # Click the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
            login_button.click()

            # Click on the PIM menu item
            PIM = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Locators().PIM)))
            actions.move_to_element(PIM).perform()
            PIM.click()

            # Click on the edit button
            edit = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().edit)))
            actions.move_to_element(edit).perform()
            edit.click()

            # Read the employee details from the Excel file
            firstname = excel_handler.read_data(4, 9)
            middlename = excel_handler.read_data(4, 10)
            lastname = excel_handler.read_data(4, 11)

            # Update the employee's first name
            fname = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().firstname)))
            actions.move_to_element(fname).perform()
            fname.send_keys(Keys.CONTROL + 'a')
            fname.send_keys(Keys.DELETE)
            fname.send_keys(firstname)
            if fname.get_attribute('value') == firstname:
                print("SUCCESS: Employee Firstname Updated Successfully")
            else:
                print("ERROR: Employee Firstname not updated")
            assert fname.get_attribute('value') == firstname, "Assertion failed: Firstname does not match expected input."

            # Update the employee's middle name
            mname = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().middlename)))
            actions.move_to_element(mname).perform()
            mname.send_keys(Keys.CONTROL + 'a')
            mname.send_keys(Keys.DELETE)
            mname.send_keys(middlename)
            if mname.get_attribute('value') == middlename:
                print("SUCCESS: Employee Middlename Updated Successfully")
            else:
                print("ERROR: Employee Middlename not updated")
            assert mname.get_attribute('value') == middlename, "Assertion failed: Middlename does not match expected input."

            # Update the employee's last name
            lname = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().lastname)))
            actions.move_to_element(lname).perform()
            lname.send_keys(Keys.CONTROL + 'a')
            lname.send_keys(Keys.DELETE)
            lname.send_keys(lastname)
            if lname.get_attribute('value') == lastname:
                print("SUCCESS: Employee LastName Updated Successfully")
            else:
                print("ERROR: Employee Lastname not updated")
            assert lname.get_attribute('value') == lastname, "Assertion failed: Lastname does not match expected input."

            # Click the save button
            save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().save)))
            save_button.click()

            # Wait for the success message to appear
            success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().success_toast_message)))

            # Check if the employee edit was successful
            if success_message.text == Locators().success_print:
                print("SUCCESS: Employee Edit is Completed with Firstname - '{a}', Middlename - '{b}' & LastName - '{c}'".format(a=firstname,b=middlename,c=lastname))
                excel_handler.write_data(4, 12, Locators().pass_data)

            else:
                print("ERROR: Employee Edit is not completed")
                excel_handler.write_data(4, 12, Locators().fail_data)

            # Assert that the success message matches the expected text
            assert success_message.text == Locators().success_print, "Assertion failed: Success message does not match expected text."
        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

    # Test case for deleting employee details
    def test_TC_PIM_03(self,boot):
        """
        TC ID - TC_Login_04
        Test Objective - Delete an existing employee in the PIM module
        """
        try:
            # Initialize the ActionChains object
            actions = ActionChains(self.driver)

            # Read the test data from the Excel file
            test_username = excel_handler.read_data(2, 7)
            test_password = excel_handler.read_data(2, 8)

            # Enter the username and password
            valid_username = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().username)))
            valid_username.send_keys(test_username)
            valid_password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            valid_password.send_keys(test_password)

            # Click the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
            login_button.click()

            # Click on the PIM menu item
            PIM = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Locators().PIM)))
            actions.move_to_element(PIM).perform()
            PIM.click()

            # Click on the delete button
            delete = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().delete)))
            actions.move_to_element(delete).perform()
            delete.click()

            # Click on the delete confirmation button
            del_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().delete_confirmation)))
            del_button.click()

            # Wait for the delete message to appear
            delete_message = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().delete_toast_message)))

            # Check if the employee details were deleted successfully
            if delete_message.text == Locators().delete_print:
                print("SUCCESS: Employee details deleted successfully")
                excel_handler.write_data(5, 12, Locators().pass_data)
            else:
                print("ERROR: Employee details is not deleted")
                excel_handler.write_data(5, 12, Locators().fail_data)

            # Assert that the delete message matches the expected text
            assert delete_message.text == Locators().delete_print, "Assertion failed: Delete message does not match expected text."

        # Handle any exceptions that may occur
        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)