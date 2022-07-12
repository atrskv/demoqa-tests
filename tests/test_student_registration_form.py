from selene.support.shared import browser
from selene import by, have, command
from utils import delete_interrupt_elements, resource
from demoqa_tests.controls import datepicker, tags_input, dropdown, modal_content


def test_register_a_student():

    # GIVEN
    browser.open('/automation-practice-form')
    delete_interrupt_elements()

    # WHEN
    browser.element('#firstName').type('Aleksei')
    browser.element('#lastName').type('Torsukov')

    browser.element('#userEmail').type('trrskv@gmail.com')

    male = browser.element('[for="gender-radio-1"] ')

    male.click()

    mobile_phone = browser.element('#userNumber').type('8999241221')
    mobile_phone.click()

    calendar = datepicker.DatePicker(browser.element('#dateOfBirthInput'))
    calendar.set_by_click('31', '9', '1998')

    '''
    OR:
    calendar = datepicker.DatePicker(browser.element('#dateOfBirthInput'))
    calendar.set_by_enter('31', 'Oct', '1998')
    '''

    hobby_checkbox = browser.element(by.text('Sports'))
    hobby_checkbox.perform(command.js.scroll_into_view).click()

    subject = tags_input.TagsInput(browser.element('#subjectsInput'))
    subject.set_by_click('History')

    '''
    OR:
    subject = tags_input.TagsInput(browser.element('#subjectsInput'))
    subject.set_by_enter(from_='His')
    '''

    avatar = browser.element('#uploadPicture')
    avatar.send_keys(resource('sadcat.png'))

    browser.element('#currentAddress').type('Saint Petersburg, ...')

    state = dropdown.Dropdown(browser.element('#state'))
    state.set_by_click('#react-select-3-option-3')

    '''
    state = dropdown.Dropdown(browser.element('#react-select-3-input'))
    state.set_by_enter('Haryana')
    '''

    city = dropdown.Dropdown(browser.element('#city'))
    city.set_by_click('#react-select-4-option-1')

    '''
    OR:
    city = dropdown.Dropdown(browser.element('#react-select-4-input'))
    city.set_by_enter('Karnal')
    '''

    browser.element('#submit').perform(command.js.click)

    # THEN
    table = modal_content.Table(browser.element('.modal-content').all('tr'))
    table.rows.should(have.exact_texts('Label Values',
         'Student Name Aleksei Torsukov',
         'Student Email trrskv@gmail.com',
         'Gender Male',
         'Mobile 8999241221',
         'Date of Birth 31 October,1998',
         'Subjects History',
         'Hobbies Sports',
         'Picture sadcat.png',
         'Address Saint Petersburg, ...',
         'State and City Rajasthan Jaiselmer'))

