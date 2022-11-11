import os
import pytest
import shutil
from selene import Browser, Config


@pytest.fixture()
def browser():
    browser = Browser(Config(driver))

    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options
    # )
