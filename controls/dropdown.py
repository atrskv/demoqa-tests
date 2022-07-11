from selene.support.shared import browser
from selene import command


class Dropdown:
    def __init__(self, element):
        self.element = element

    def using_enter(self, locality='Haryana'):
        self.element.type(locality).press_enter()

    def using_click(self, selector='#react-select-3-option-0'):
         self.element.click()  # dropdown opened
         browser.element(selector).perform(command.js.click)


# class CityDropdown:
#     def __init(self):
#         self.element = ...
#
#     def select_city_using_click(self, city_index_from_list):
#         dropdown_button = browser.element('#city').click()
#         browser.element(f'#react-select-4-option-{city_index_from_list}').perform(command.js.click)
