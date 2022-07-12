from selene.support.shared import browser


class TagsInput:
    def __init__(self, element):
        self.element = element

    def set_by_enter(self, *, from_='Chem', to='Chemistry'):
        self.element.click()

        # or user can press tab, but usually we use enter
        self.element.type(from_).press_enter()

    def set_by_click(self, subject_name, subject_index: str = '0'):
        self.element.click()
        self.element.type(subject_name)
        browser.element(f'#react-select-2-option-{subject_index}').click()
