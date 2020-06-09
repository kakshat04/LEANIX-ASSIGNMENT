from time import sleep
from Project.base.selenium_driver import SeleniumDriver as SD


class CloudServicePage(SD):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.sd = SD(self.driver)

    # locators
    _iamusers_field_xpath = "//span[contains(text(),'AWS IAM Users with Access Key Age')]"
    _iamuser_page_title = "AWS IAM Users with Access Key Age | LeanIX"
    _age_elements_xpath = "//span[contains(@class,'viewLabel')]"
    _age_limit_list = ['n/a', '0', '> 0', '> 12', '> 24', '> 36', '> 48', '> 60']
    _leanix_ldif_bucket_xpath = "//div[contains(@class,'ClusterMap-contentItem') and " \
                                "contains(@title,'LeanIXAccessLDIFBucket')]"
    _leanix_scan_user_xpath = "//div[contains(@class,'ClusterMap-contentItem') and" \
                              " contains(@title,'leanIXScanAgentUser')]"

    def goto_iam_users(self):
        # scroll to
        self.scroll_to(self._iamusers_field_xpath, "xpath")
        sleep(1)
        self.execute_javascript("window.scrollBy(0,200)")
        sleep(3)

        # click
        self.element_click(self._iamusers_field_xpath, "xpath")
        sleep(5)

    def verify_successful_navigation(self):
        title = self.get_page_title()
        print("#*" * 10, title)
        if self._iamuser_page_title in title:
            return True
        else:
            return False

    def verify_result_report(self):
        # Verification 1
        age_range_lst = []
        get_elements = self.get_elements(self._age_elements_xpath, "xpath")
        for element in get_elements:
            age_range_lst.append(element.text)
        for values in self._age_limit_list:
            if values not in age_range_lst:
                return False
        # Verification 2
        if not self.verify_successful_navigation():
            return False
        # Verification 3
        self.switch_to_frame(0)  # Switch Frame
        is_present_1 = self.is_element_present(self._leanix_ldif_bucket_xpath, "xpath")
        # self.element_click((self._leanix_ldif_bucket_xpath, "xpath"))
        # sleep(2)
        is_present_2 = self.is_element_present(self._leanix_scan_user_xpath, "xpath")
        # self.element_click((self._leanix_scan_user_xpath, "xpath"))
        # sleep(2)
        # Back to original frame
        self.switch_to_original_frame()
        sleep(1)

        if not is_present_1 or not is_present_2:
            return False
        return True






