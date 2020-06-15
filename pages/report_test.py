from time import sleep
from Project.base.selenium_driver import SeleniumDriver as SD
from Project.utility.read_from_json import ReadJson
from Project.utility.custom_logging import custom_logger as cl
import logging


class ReportTest(SD):
    log = cl(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.sd = SD(self.driver)

    # age_mapping  --> {age range: xpath}
    _age_map = {
                   'n/a': "//span[contains(@class,'circle withBorder') and contains(@style,'rgb(255, 255, 255)')]",
                   '0': "//span[contains(@class,'circle') and contains(@style,'rgb(239, 239, 239)')]",
                   '> 0': "//span[contains(@class,'circle') and contains(@style,'rgb(191, 224, 245)')]",
                   '> 12': "//span[contains(@class,'circle') and contains(@style,'rgb(143, 184, 210)')]",
                   '> 24': "//span[contains(@class,'circle') and contains(@style,'rgb(96, 145, 176)')]",
                   '> 36': "//span[contains(@class,'circle') and contains(@style,'rgb(48, 105, 141)')]",
                   '> 48': "//span[contains(@class,'circle') and contains(@style,'rgb(0, 65, 106)')]",
                   '> 60': "//span[contains(@class,'circle') and contains(@style,'rgb(0, 65, 106)')]"
    }
    _age_limit_list = ['n/a', '0', '> 0', '> 12', '> 24', '> 36', '> 48', '> 60']
    _verification_lst = [1, 13, 25, 37, 49, 61]

    _iamuser_page_title = "AWS IAM Users with Access Key Age | LeanIX"

    # locators
    _iamusers_field_xpath = "//span[contains(text(),'AWS IAM Users with Access Key Age')]"
    _age_elements_xpath = "//span[contains(@class,'viewLabel')]"
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

    def get_age_attribute_bg_clr(self):
        attr_dict = {}

        # Read user ages from json - list
        json_read = ReadJson()
        property_details_dict = json_read.get_user_property_details()

        print("Dictionary of ADK_Name and AccessKeyAge received from JSON File..")
        self.log.info("Dictionary of ADK_Name and AccessKeyAge received from JSON File..")
        print(property_details_dict)
        self.log.info(property_details_dict)

        # Verify the age falls in which category of _age_limit_list
        # Verify range in report - index + 2
        for adk, age in property_details_dict.items():
            if age == 'n/a':
                xpath = self._age_map['n/a']
            elif age == '0':
                # If age is n/a or 0
                xpath = self._age_map['0']
            else:
                num = 0
                i = 0
                j = 0
                # print(age, num, i, j)
                while j < len(self._verification_lst) - 1:
                    j += 1
                    if self._verification_lst[i] <= int(age) < self._verification_lst[j]:
                        num = self._verification_lst[i]
                        break
                    i += 1
                if num == 0:
                    num = self._verification_lst[-1]

                # +2, as _age_limit_list is 2 more than _verification_lst
                age_index = self._verification_lst .index(num) + 2

                # dictionary - age:xpath -- bg color
                xpath = self._age_map[self._age_limit_list[age_index]]

            # Find age bg color on report based on xpath
            attr_dict[adk] = self.get_attribute(xpath, 'xpath', 'style')  # {adk_name: style} from age range

        print("Dictionary of ADK_Name(from json) and respective age limit Style value(in the report)..")
        self.log.info("Dictionary of ADK_Name(from json) and respective age limit Style value(in the report)..")
        print(attr_dict)
        self.log.info(attr_dict)

        return attr_dict

    def get_aws_box_attribute_bg_clr(self):
        # AWS box bg color verify
        attr_dict = {}

        self.switch_to_frame(0)  # Switch Frame

        print("Creating Dictionary of ADK_Name and Style Value(from AWS BOX)...")
        self.log.info("Creating Dictionary of ADK_Name and Style Value(from AWS BOX)...")

        scan_agent_user_bg = self.get_attribute(self._leanix_scan_user_xpath, 'xpath', 'style')
        scan_agent_user_title = self.get_attribute(self._leanix_scan_user_xpath, 'xpath', 'title')
        attr_dict[scan_agent_user_title] = scan_agent_user_bg  # {adk_title(name): style}

        access_ldif_bucket_bg = self.get_attribute(self._leanix_ldif_bucket_xpath, 'xpath', 'style')
        access_ldif_bucket_title = self.get_attribute(self._leanix_ldif_bucket_xpath, 'xpath', 'title')
        attr_dict[access_ldif_bucket_title] = access_ldif_bucket_bg  # {adk_title(name): style}

        # Back to original frame
        self.switch_to_original_frame()

        print(attr_dict)
        self.log.info(attr_dict)

        return attr_dict

    def verify_result_report(self):
        print("Make sure we navigated to the correct page, to avoid unnecessary executions")
        title = self.get_page_title()
        if self._iamuser_page_title in title:
            age_attr_btn_dict = self.get_age_attribute_bg_clr()
            aws_box_attr_dict = self.get_aws_box_attribute_bg_clr()

            print("-----------------------")
            print(age_attr_btn_dict)
            print(aws_box_attr_dict)

            # This will verifyrespective age limit Style value correct color code for all ADK_Name in the box
            print("Verifying ADK name -> matches from JSON file and respective bg color -> matches age range above..")
            self.log.info("Verifying ADK name -> matches from JSON file and "
                          "respective bg color -> matches age range above..")

            for i in range(len(aws_box_attr_dict.keys())):
                if not list(age_attr_btn_dict.keys())[i] in list(aws_box_attr_dict.keys())[i]:
                    msg = "Report Verification Failed.." \
                          "Mismatch in Age Range Color Code and respective AWS User Color Code or " \
                          "User name in AWS does not match with appropriate ADK name from the json file for that " \
                          "respective age"
                    print(msg)
                    self.log.error(msg)
                    return False
            msg = "Report Verification Successful.." \
                  "Match in Age Range Color Code and respective AWS User Color Code or " \
                  "User name in AWS matches with appropriate ADK name from the json file for that " \
                  "respective age"
            print(msg)
            self.log.info(msg)
            return True

