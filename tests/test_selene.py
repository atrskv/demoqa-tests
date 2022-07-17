from selene import by, be
from selene.support.shared import browser


def test_search_issue_by_partial_text():

    # GIVEN
    browser.open('https://github.com')

    # WHEN
    browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()

    # THEN
    browser.all(by.partial_text('#76')).should(be.visible)