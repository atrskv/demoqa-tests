from selene import command, by, have
from selene.support.shared import browser
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.modal_content import Table
from demoqa_tests.model.controls.tags_input import TagsInput
from utils.utils import resource


class StudentRegistrationForm:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def set_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def set_lastname(self, value):
        browser.element('#lastName').type(value)
        return self

    def set_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def set_gender(self, value):
        browser.element(f'[for="gender-radio-{value}"]').click()
        return self

    def set_phone(self, value):
        browser.element('#userNumber').type(value).click()
        return self

    def set_date_of_birth(self, day: str, month_index, year: str):
        DatePicker(browser.element('#dateOfBirthInput')).set_by_click(day, month_index, year)
        return self

    def set_hobby(self, *values):
        for value in values:
            browser.element(by.text(value)).perform(command.js.scroll_into_view).click()
        return self

    def set_subjects(self, *values):
        TagsInput(browser.element('#subjectsInput')).set_by_enter(*values)
        return self

    def set_avatar(self, path):
        browser.element('#uploadPicture').send_keys(resource(path))
        return self

    def set_adress(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def set_state(self, state_index: str):
        Dropdown(browser.element('#state')).set_by_click(f'#react-select-3-option-{state_index}')
        return self

    def set_city(self, city_index: str):
        Dropdown(browser.element('#city')).set_by_click(f'#react-select-4-option-{city_index}')
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)

class ModalDialog:
    def __init__(self):
        self.element = browser.element('.modal-content')
        self.table = Table(browser.element('.modal-content').all('tr'))

    def should_have_rows_with_exact_texts(self, *texts):
        self.table.rows.should(have.exact_texts(*texts))