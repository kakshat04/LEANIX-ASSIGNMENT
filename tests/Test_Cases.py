from Project.pages.login_pages import LoginPage
from Project.pages.cloud_service import CloudServicePage
from Project.pages.data_modification import DataModification
from Project.pages.data_modification_check import DataModificationCheck
import unittest
import time
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.csp = CloudServicePage(self.driver)
        self.dm = DataModification(self.driver)
        self.dmc = DataModificationCheck(self.driver)

    # @pytest.mark.run(order=1)
    # def test_invalid_login(self):
    #     self.lp.login_page(email="1002@gmail.com", password="acbacb")
    #     time.sleep(2)
    #     assert self.lp.verify_login_failed() is True  # Verify login not successful

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login_page(email="kumar.akshat04@gmail.com", password="Knight@riders1")
        time.sleep(2)
        assert self.lp.verify_login_successful() is True  # Verify login successful

    @pytest.mark.run(order=3)
    def test_iamuser_on_page(self):
        self.csp.goto_iam_users()
        assert self.csp.verify_successful_navigation() is True

    @pytest.mark.run(order=4)
    def test_verify_page(self):
        assert self.csp.verify_result_report() is True

    @pytest.mark.run(order=5)
    def test_admin_area(self):
        assert self.dm.select_administration() is True

    @pytest.mark.run(order=6)
    def test_goto_integration_api(self):
        assert self.dm.integration_api() is True

    @pytest.mark.run(order=7)
    def test_modify_data(self):
        assert self.dm.expand_user_connector() is True

    @pytest.mark.run(order=8)
    def test_modication_check(self):
        self.dmc.validate_leanix_scan_agent_user()
