from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = False
    browser.config.timeout = 4
    browser.config.window_width = 1200
    browser.config.window_height = 1000


@pytest.fixture(scope='function', autouse=True)
def modal_dialog_close():
    yield
    browser.element('#closeLargeModal').click()
