from time import sleep
from Project.base.selenium_driver import SeleniumDriver as SD


class LoginPage(SD):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.sd = SD(self.driver)

    # locators
    _email_field_name = "j_username"
    _password_field_name = "j_password"
    _login_button_xpath = "//button[contains(text(),'Login')]"
    _login_success_field_id = "tourWhatsNew"
    _login_failed_class_name = "alert alert-danger"

    def enter_email(self, email):
        # self.sd.enter_keys(self._email_field_id, 'id', email) # When done without Inheritance
        self.clear_text(self._email_field_name, 'name')
        self.enter_keys(self._email_field_name, 'name', email)

    def enter_password(self, pwd):
        # self.sd.enter_keys(self._password_field_id, 'id', pwd) # When done without Inheritance
        self.clear_text(self._password_field_name, 'name')
        self.enter_keys(self._password_field_name, 'name', pwd)

    def click_login_button(self):
        # self.sd.element_click(self._login_link, 'link') # When done without Inheritance
        self.element_click(self._login_button_xpath, 'xpath')

    def login_page(self, email='', password=''):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        sleep(2)

        # #---------------------------- Temporary Code ------------------------ #
        # Clicking Dashboard, because of error in page
        self.element_click("//span[contains(@class,'hideForSmall') and contains(text(),'Dashboard')]", "xpath")

    def verify_login_successful(self):
        is_login_success = self.is_element_present(self._login_success_field_id, 'id')
        if is_login_success:
            # Click on Dashboard
            self.element_click("//span[contains(@class,'hideForSmall') and contains(text(),'Dashboard')]", "xpath")
            sleep(2)
            return True
        else:
            return False

    def verify_login_failed(self):
        is_login_fail = self.is_element_present("//div[contains(text(),'This combination of email and password "
                                                "is not correct')]", 'xpath')
        if is_login_fail:
            return True
        else:
            return False



