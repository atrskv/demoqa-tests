from selene.support.shared import browser


class DatePicker:
    def __init__(self, element):
        self.element = element

    def using_click(self, year='1998', month_index='9', day='01'):
        self.element.click()

        browser.element(f'[class$=year-select] [value="{year}"]').click()
        browser.element(f'[class$=month-select] [value="{month_index}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def using_enter(self, day='Jan', month='01', year='1998'):
        self.element.click()

        browser.execute_script(
            '''
                document.querySelector("#dateOfBirthInput")
                .value = ''
            ''')

        self.element.type(f'{day} {month} {year}')
        self.element.press_enter()
