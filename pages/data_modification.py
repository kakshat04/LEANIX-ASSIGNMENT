from time import sleep
from Project.base.selenium_driver import SeleniumDriver as SD
from Project.utility.write_to_json import WriteJson


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
    _inbound_text_area_xpath = "/html/body//div[2]/div[2]/div[1]//div[1]/textarea"

    def navigate_integration_api(self):
        try:
            print("Now, after successful report validation, moving to data enhancement... :)")
            print("Navigating to Administration Page now..")
            # Click on profile image
            self.element_click(self._user_image_id, "id")
            sleep(1)

            # Select Administration from drop down
            self.element_click(self._administration_drop_down_xpath, "xpath")
            sleep(1)

            print("Click on integration api tab...")
            # click on integration api tab
            self.element_click(self._integration_api_xpath, "xpath")
            sleep(1)

            print("Click on user connector..")
            # Click on user connector
            self.element_click(self._user_connector, "xpath")
            sleep(5)
            return True
        except:
            return False

    def data_modify_security_warn_level(self):
        """
        This method will update json file with required Security Warn Level, based on Access Key age
        "" for 0 .. 30 days
        "low" for 31 .. 60 days
        "medium" for more than 60 days

        :return:
        """

        print("Modifying json file as following - '' for 0-30 days, 'low' for 31-60 days, 'medium' for >60 days")
        # Modify data with required security warn levels
        modify_json = WriteJson()
        json_data = modify_json.write_security_warn_level()
        sleep(2)

        # update in inbound
        print("$$$$$$$$$$$$$$$$")
        print(type(json_data))
        self.enter_text_in_textarea(self._inbound_text_area_xpath, 'xpath', str(json_data))





