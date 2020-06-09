from time import sleep
from Project.base.selenium_driver import SeleniumDriver as SD


class DataModification(SD):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.sd = SD(self.driver)

    # locators
    _user_image_id = "menuLink"
    _administration_drop_down_xpath = "//div[@id='appNavbarCollapse']//span[text()='Administration']"
    _integration_api_xpath = "//a[contains(@class,'integrationApiLink')]"
    _user_connector = "//a[contains(text(),'cloudockit')]"

    def click_profile_image(self):
        # Click on profile image
        self.element_click(self._user_image_id, "id")

    def select_administration(self):
        try:
            self.click_profile_image()
            sleep(1)
            self.element_click(self._administration_drop_down_xpath, "xpath")
            return True
        except:
            return False

    def integration_api(self):
        try:
            # click on integration api tab
            self.element_click(self._integration_api_xpath, "xpath")
            return True
        except:
            return False

    def expand_user_connector(self):
        try:
            self.element_click(self._user_connector, "xpath")
            return True
        except:
            return False

