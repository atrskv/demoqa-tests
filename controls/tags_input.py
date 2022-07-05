from selene.support.shared import browser


class TagsInput:
    def __init__(self, element):
        self.element = element

    def using_enter(self, beginning_of_a_word='Social'):
        self.element.click()

        # or user can press tab, but usually we use enter
        self.element.type(beginning_of_a_word).press_enter()

    def using_click(self, subject_name='Social Studies', subject_index='0'):
        self.element.click()
        self.element.type(subject_name)
        browser.element(f'#react-select-2-option-{subject_index}').click()
