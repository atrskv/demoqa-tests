from selene.support.shared import browser


class TagsInput:
    def __init__(self, element):
        self.element = element

    def set_by_enter(self, values, to='Chemistry'):
        self.element.click()
        for value in values:
            self.element.type(value).press_enter()
        return self

    def set_by_click(self, subject_name, subject_index: str = '0'):
        self.element.click()
        self.element.type(subject_name)
        browser.element(f'#react-select-2-option-{subject_index}').click()
