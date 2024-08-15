
# Overview

This repository contains an automated test script for validating the Login and PIM (Personnel Information Management) functionalities of the OrangeHRM portal. The script is written using Python and Selenium WebDriver, with test data managed through Excel files.

# Files and Directories

* test_OrangeHRM.py: The main test script containing the test cases for login and PIM functionalities.

* Locators/OrangeHRM_Locators.py: Contains all the locators and static data required for the test cases.

* Utilities/excel_functions.py: Contains functions for reading from and writing to the Excel files.

* Data/test_data.xlsx: Excel file containing the test data.

# Prerequisites

* Python 3.x

* pip package manager

* Chrome browser installed

* The following Python packages installed via pip:

    * selenium
    * pytest
    * openpyxl
    * webdriver-manager

You can install the required packages using the following command:

```bash
  pip install selenium pytest openpyxl webdriver-manager
```

# How to Run the Tests

1. Clone the Repository: Clone this repository to your local machine.

2. Set Up Excel Data: Ensure that the test_data.xlsx file is correctly formatted and contains the necessary data for the test cases.

3. Run the Tests: Use pytest to run the test cases in the test_OrangeHRM.py script.

```bash
  pytest test_OrangeHRM.py
```
# Test Cases

1. ### Login Tests
* TC_Login_01: Validates successful login to the OrangeHRM portal using valid credentials.
* TC_Login_02: Validates unsuccessful login with invalid credentials.

2. ### PIM Tests
* TC_PIM_02: Validates the ability to edit existing employee details in the PIM module.
* TC_PIM_03: Validates the deletion of an existing employee's details from the PIM module.

# Error Handling

The script includes exception handling to manage common Selenium exceptions like NoSuchElementException and ElementNotVisibleException, ensuring that the test cases provide meaningful error messages in case of failure.

# Logging and Reporting

The script prints success or error messages to the console for each test case, including the specific actions performed (e.g., login success/failure, employee details update/delete status). The test results are also logged in the Excel file for reference.

# Notes

Ensure that the correct ChromeDriver version is being used for your version of the Chrome browser.
Update the Locators.py file with the correct locators and URLs relevant to your OrangeHRM instance.



