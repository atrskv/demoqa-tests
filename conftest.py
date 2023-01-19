import os

from selene.support.shared import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from dotenv import load_dotenv

from utils import attach

# DEFAULT_BROWSER_VERSION = "100.0"
#
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_version',
#         default='100.0'
#     )

#
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()


# @pytest.fixture(scope='function')
# def setup_browser(request):
#     browser_version = request.config.getoption('--browser_version')
#     browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": browser_version,
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#     options.capabilities.update(selenoid_capabilities)
#
#     login = os.getenv('LOGIN')
#     password = os.getenv('PASSWORD')
#
#     driver = webdriver.Remote(
#         command_executor=f"https://{login}:{password}@selenoid:4444/wd/hub",
#         options=options
#     )
#
#     browser = Browser(Config(driver))
#
#     yield browser
#
#     attach.add_html(browser)
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#
#     # attach.add_video(browser)
#
#     browser.quit()



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = False
    browser.config.timeout = 4
    browser.config.window_width = 1366
    browser.config.window_height = 768

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)

    browser.quit()