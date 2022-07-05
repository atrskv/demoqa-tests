from selene.support.shared import browser


class DatePicker:
    def __init__(self):
        self.element = ...

    def click_the_date(self, year, moth_num, day):
        self.element.click()
        browser.element(f'[class$=year-select] [value="{year}"]').click()
        browser.element(f'[class$=month-select] [value="{moth_num}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def input_the_date(self, day, month_3_first_letters, year):
        self.element.click()
        browser.execute_script(
            '''
                document.querySelector("#dateOfBirthInput")
                .value = ''
            ''')

        self.element.type(f'{day} {month_3_first_letters} {year}')
        self.element.press_enter()
