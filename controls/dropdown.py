from selene.support.shared import browser
from selene import command


class StateDropdown:
    def __init__(self):
        self.element = ...

    def select_state_using_tab(self, state):
        self.element.type(f'{state}').press_tab()

    def select_state_using_click(self, state_index_from_list):
        dropdown_button = browser.element('#state').click()
        browser.element(f'#react-select-3-option-{state_index_from_list}').perform(command.js.click)


class CityDropdown:
    def __init(self):
        self.element = ...

    def select_city_using_click(self, city_index_from_list):
        dropdown_button = browser.element('#city').click()
        browser.element(f'#react-select-4-option-{city_index_from_list}').perform(command.js.click)
