from time import sleep
from Project.base.selenium_driver import SeleniumDriver as SD


class DataModificationCheck(SD):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.sd = SD(self.driver)

    # locators
    _search_tab_xpath = "//lx-quick-search[@id='tourQuickSearch']//input[@type='text']"

    def validate_leanix_scan_agent_user(self):
        # Click on profile image
        # self.enter_keys(self._search_tab_xpath, "xpath", "leanIXScanAgentUser")
        self.submit(self._search_tab_xpath, "xpath", "leanIXScanAgentUser")
        sleep(5)

