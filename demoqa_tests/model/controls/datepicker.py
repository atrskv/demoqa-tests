from selene.core.entity import Element
from selene.support.shared import browser


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def set_by_click(self, day='01', month_index='9', year='1998'):
        self.element.click()

        browser.element(f'[class$=year-select] [value="{year}"]').click()
        browser.element(f'[class$=month-select] [value="{month_index}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def set_by_enter(self, day='01', month='Jan', year='1998'):
        self.element.click()


        browser.execute_script(
            '''
                document.querySelector("#dateOfBirthInput")
                .value = ''
            ''')

        self.element.type(f'{month} {day} {year}')
        self.element.press_enter()
        return self
