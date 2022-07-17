import json

import allure
from allure import attachment_type
from allure_commons.types import Severity


def test_attachments():
    allure.attach('Text content', name='Content from text', attachment_type=attachment_type.TEXT)
    allure.attach('<h1>html</h1>', name='Html', attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({'first': 1, 'second': 2}), name='Json', attachment_type=attachment_type.JSON)


def test_labels():
    allure.dynamic.tag('web')
    allure.dynamic.feature('Задачи')
    allure.dynamic.story('Авторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.link('https://github.com/', name='Testing')
    allure.dynamic.description('Desc')
    allure.dynamic.description_html('<h2>lalala</h2>')
    allure.dynamic.issue('https://github.com/', name='Issue')
    allure.dynamic.title('Title')
    allure.dynamic.mro()
    allure.dynamic.parent_suite('Parent_suite')
    allure.dynamic.sub_suite('Sub')
    allure.dynamic.testcase('https://github.com/', 'TC1')
    allure.dynamic.suite('Suite #1')
    pass


@allure.tag('web')
@allure.feature('Задачи')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.severity(Severity.CRITICAL)
@allure.link('https://github.com/', name='Testing')
@allure.label('owner', 'torsukov')
@allure.title('Title #1')
@allure.description('Desc #2')
@allure.description_html('<p>lalalala</p>')
@allure.epic('Epicname')
@allure.suite('Suite #2')
@allure.sub_suite('Sub_Suite')
@allure.parent_suite('Parent Suite')
@allure.issue('https://github.com/', name='Issue')
@allure.testcase('https://github.com/', name='TC3')
def test_decorator_labels():
    pass
