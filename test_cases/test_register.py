import pytest
import os
import time

from Base_pages.Register_Page import Register
from selenium.webdriver.common.by import By
from utilities.read_property import Read_Config
from utilities.data_generator import generate_combined_username
from utilities.custom_logger import LogMaker


class Test_Register:
    project_url = Read_Config.get_url()

    first_name = Read_Config.get_first()
    last_name = Read_Config.get_last()
    address = Read_Config.get_address()
    city = Read_Config.get_city()
    state = Read_Config.get_state()
    zip = Read_Config.get_zip()
    customer_ssn = Read_Config.get_ssn()
    password = Read_Config.get_password()
    confirm_pass = Read_Config.get_confirm()
    logger = LogMaker.log_gen()

    def test_title_verification(self, setup, request):
        self.logger.info("******* Test Case: Title Verification ***********")
        self.driver = setup
        try:
            self.driver.get(self.project_url)
            act_title = self.driver.title
            assert "ParaBank | Administration " in act_title, f"Title mismatch: {act_title}"
        except AssertionError as e:
            self._capture_screenshot(request, "test_title_verification")
            raise e

    def test_register_valid(self, setup, request):
        self.logger.info("******* Test Case: Test Register with Valid Data ***********")
        self.driver = setup
        try:
            self.driver.get(self.project_url)
            self.obj_Register = Register(self.driver)

            username = generate_combined_username()

            time.sleep(2)
            self.obj_Register.click_on_registerlink()
            self.obj_Register.enter_first_name(self.first_name)
            self.obj_Register.enter_last_name(self.last_name)
            self.obj_Register.enter_address(self.address)
            self.obj_Register.enter_city(self.city)
            self.obj_Register.enter_state(self.state)
            self.obj_Register.enter_zip(self.zip)
            self.obj_Register.enter_customer_ssn(self.customer_ssn)

            self.obj_Register.enter_username(username)
            self.obj_Register.enter_password(self.password)
            self.obj_Register.enter_confirm_password(self.confirm_pass)
            self.obj_Register.click_submit()

            exp_title = 'ParaSoft Demo Website'
            time.sleep(2)
            act_title = self.driver.find_element(By.XPATH, "//h1[text()='ParaSoft Demo Website']").text
            print(act_title)

            assert exp_title in act_title, f"Register Test Case Failed: {act_title}"
        except AssertionError as e:
            self._capture_screenshot(request, "test_register_valid")
            raise e

    def _capture_screenshot(self, request, test_name):
        """
        Capture a screenshot and save it in the Screenshots folder.
        :param request: pytest request object
        :param test_name: Name of the test for the screenshot filename
        """
        screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        file_name = f"{test_name}_{int(time.time())}.png"
        screenshot_path = os.path.join(screenshot_dir, file_name)
        self.driver.save_screenshot(screenshot_path)
        self.logger.error(f"Screenshot saved at: {screenshot_path}")
