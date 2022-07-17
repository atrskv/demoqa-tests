import allure
from selene import by, be
from selene.support.shared import browser


def test_search_issue_by_partial_text():

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-input').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем вкладку "Issues"'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие нужной issue'):
        browser.all(by.partial_text('#76')).should(be.visible)