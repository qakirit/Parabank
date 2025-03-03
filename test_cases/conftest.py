import pytest
import os
import time
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to determine the result of each test.
    Adds the test result information to the item.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    """
    Capture a screenshot if a test case fails.
    """
    yield
    # Runs after the test execution
    if request.node.rep_call.failed:
        driver = request.node.funcargs.get("setup")  # Get WebDriver instance
        if driver:
            screenshot_dir = "C:\\Users\\kirit\\PycharmProjects\\ParaBank Banking\\Screenshorts"
            os.makedirs(screenshot_dir, exist_ok=True)  # Ensure directory exists
            file_name = f"{request.node.name}_{int(time.time())}.png"
            screenshot_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(screenshot_path)
            print(f"\n[INFO] Screenshot saved at: {screenshot_path}")
