from selene.support.shared import browser


class TagsInput:
    def __init__(self):
        self.element = ...

    def add_subject_using_tab(self, subject_tag):
        self.element.click()  # No we can type tag
        self.element.type(subject_tag).press_enter()

    def add_subject_using_click(self, subject_tag, subject_index):
        self.element.click()
        self.element.type(subject_tag)
        browser.element(f'#react-select-2-option-{subject_index}').click()
