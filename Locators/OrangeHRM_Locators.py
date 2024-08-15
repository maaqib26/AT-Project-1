"""
OrangeHRM_Locators.py - Script to store web element locators
"""
class Locators:
    username = "username"
    password = "password"
    submit_button = "//button[@type='submit']"
    logout_dropdown = 'oxd-userdropdown-tab'
    logout = 'Logout'
    PIM = 'PIM'
    firstname = 'firstName'
    lastname = 'lastName'
    middlename = 'middleName'
    edit = "//div[@class='oxd-table-card'][2]//button[1]"
    delete = "//div[@class='oxd-table-card'][2]//button[2]"
    delete_confirmation = "//div[@class='orangehrm-modal-footer']//button[2]"
    save = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//form//button"
    success_toast_message = "//div[@id='oxd-toaster_1']//p[text()='Successfully Updated']"
    delete_toast_message = "//div[@id='oxd-toaster_1']//p[text()='Successfully Deleted']"
    delete_print = 'Successfully Deleted'
    success_print = 'Successfully Updated'
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    excel_file = "E:\\Workspace\\GUVI\\PAT-Projects\\AT-Project-1\\Data\\test_data.xlsx"
    # sheet_number = "Sheet1"
    sheet_number = "Test_Data"
    pass_data = "TEST PASS"
    fail_data = "TEST FAILED"
