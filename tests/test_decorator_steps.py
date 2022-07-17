import allure
from selene import by, be
from selene.support.shared import browser


@allure.step('Открываем главную страницу')
def open_browser():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_repo(repo):
    browser.element('.header-search-input').type(repo).press_enter()


@allure.step('Открываем репозиторий')
def open_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем вкладку "Issues"')
def issues_open():
    browser.element('#issues-tab').click()


@allure.step('Проверяем, что на странице видна issue с номером {num}')
def should_see_issue_with_number(num):
    browser.element(by.partial_text(num)).should(be.visible)


def test_search_issue_by_partial_text():
    open_browser()
    search_repo('eroshenkoam/allure-example')
    open_repo('eroshenkoam/allure-example')
    issues_open()
    should_see_issue_with_number('#76')
