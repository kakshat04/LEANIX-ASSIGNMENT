from time import sleep
from Project.base.selenium_driver import SeleniumDriver as SD
import os
import ast


class DataModificationCheck(SD):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.final_values = {}
        # self.sd = SD(self.driver)

    # locators
    _search_tab_xpath = "//lx-quick-search[@id='tourQuickSearch']//input[@type='text']"
    _user_adk_name_1 = "leanIXScanAgentUser"
    _user_adk_name_2 = "LeanIXAccessLDIFBucket"
    _new_user_selection_page_title = "New | LeanIX"
    _href_user_xpath = "//a[contains(@class,'title titleLink') and contains(@href,'/akkDemo/factsheet')]//parent::div"
    _more_properties_xpath = "//span[contains(text(),'more properties')]"
    _access_key_age = "//div[contains(text(),'AccessKeyAge')]//following-sibling::div"
    _violation_level_security = "//div[contains(text(),'violationLevelSecurity')]//following-sibling::div"

    def get_age_and_violation_details(self):
        # Empty dictionary to store age and respective violation for LeanixScanAgentUser
        age_violation = {}

        print("Click on Show more properties..")
        self.execute_javascript("window.scrollBy(0,100)")
        sleep(1)
        self.element_click(self._more_properties_xpath, 'xpath')
        sleep(1)

        print("Verify if 'violationLevelSecurity' is visible in the property..")
        if self.is_element_present(self._violation_level_security, 'xpath'):
            # Get Access Key age
            access_age = self.get_element_text(self._access_key_age, 'xpath')
            print("################", access_age)

            # Get ViolationLevelSecurity value
            vio_value = self.get_element_text(self._violation_level_security, 'xpath')
            print("################", vio_value)

            # Setting dict to {age:value} i.e {67:'medium'} or {13:''}
            age_violation[access_age.split()[0]] = vio_value
            print("Got Age and Security Warn Level..")
            print(age_violation)
            return age_violation
        else:
            return False

    def validate_leanix_scan_agent_user(self):
        print("Enter leanIXScanAgentUser in the search box..")
        self.submit(self._search_tab_xpath, "xpath", self._user_adk_name_1)
        sleep(5)

        print("Verify if we are new user selection page..")
        title = self.get_page_title()
        if self._new_user_selection_page_title in title:
            print("Yes, we are inside new user selection page..")
            print("Click leanIXScanAgentUser..")
            self.perform_action_chains(self._href_user_xpath, 'xpath', 'click')

        print("Get Age and Security Warn Level form leanIXScanAgentUser..")
        leanix_scan_agent_data = self.get_age_and_violation_details()

        print("Verifying it against json data..")
        age_security_dict = None
        if 'age_security_warn_dict' in os.environ:
            # Converting string back to dict
            age_security_dict = ast.literal_eval(os.environ['age_security_warn_dict'])

        print("_________________Code to be Deleted ______________________")
        print(age_security_dict)
        print(type(age_security_dict))
        print(leanix_scan_agent_data)
        print(list(leanix_scan_agent_data.keys())[0])
        print(leanix_scan_agent_data[list(leanix_scan_agent_data.keys())[0]])
        print(age_security_dict[list(leanix_scan_agent_data.keys())[0]])
        print("_________________Code to be Deleted ______________________")

        if list(leanix_scan_agent_data.keys())[0] in age_security_dict and \
                leanix_scan_agent_data[list(leanix_scan_agent_data.keys())[0]] == \
                age_security_dict[list(leanix_scan_agent_data.keys())[0]]:
            return True
        else:
            return False

    def validate_leanix_access_ldif_bucket(self):
        print("Enter LeanIXAccessLDIFBucket in the search box..")
        self.submit(self._search_tab_xpath, "xpath", self._user_adk_name_2)
        sleep(5)

        print("Verify if we are new user selection page..")
        title = self.get_page_title()
        if self._new_user_selection_page_title in title:
            print("Yes, we are inside new user selection page..")
            print("Click LeanIXAccessLDIFBucket..")
            self.perform_action_chains(self._href_user_xpath, 'xpath', 'click')

        # Verify age and violation
        leanix_access_ldif_data = self.get_age_and_violation_details()

        print("Verifying it against json data..")
        age_security_dict = None
        if 'age_security_warn_dict' in os.environ:
            # Converting string back to dict
            age_security_dict = ast.literal_eval(os.environ['age_security_warn_dict'])

        print("_________________Code to be Deleted ______________________")
        print(age_security_dict)
        print(type(age_security_dict))
        print(leanix_access_ldif_data)
        print(list(leanix_access_ldif_data.keys())[0])
        print(leanix_access_ldif_data[list(leanix_access_ldif_data.keys())[0]])
        print(age_security_dict[list(leanix_access_ldif_data.keys())[0]])
        print("_________________Code to be Deleted ______________________")

        if list(leanix_access_ldif_data.keys())[0] in age_security_dict and \
                leanix_access_ldif_data[list(leanix_access_ldif_data.keys())[0]] == \
                age_security_dict[list(leanix_access_ldif_data.keys())[0]]:
            return True
        else:
            return False











