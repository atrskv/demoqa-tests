from selene.support.shared import browser
from selene import by, have, command
from utils import delete_interrupt_elements, resource
from controls import datepicker, tags_input, dropdown, modal_content


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
    calendar.using_enter('Oct', '31', '1998')
    '''
    OR:
    calendar = datepicker.DatePicker(browser.element('#dateOfBirthInput'))
    calendar.using_click('1998', '9', '31')
    '''

    hobby_checkbox = browser.element(by.text('Sports'))
    hobby_checkbox.perform(command.js.scroll_into_view).click()

    subject = tags_input.TagsInput(browser.element('#subjectsInput'))
    subject.using_enter('Histo')  # History
    '''
    OR:
    subject = tags_input.TagsInput(browser.element('#subjectsInput'))
    subject.using_click('Social Studies', '0')  # subject and index
    '''

    avatar = browser.element('#uploadPicture')
    avatar.send_keys(resource('sadcat.png'))

    browser.element('#currentAddress').type('Saint Petersburg, ...')

    state = dropdown.Dropdown(browser.element('#state'))
    state.using_click('#react-select-3-option-3')
    '''
    OR:
    state = dropdown.Dropdown(browser.element('#react-select-3-input'))
    state.using_enter('Haryana')
    '''

    city = dropdown.Dropdown(browser.element('#city'))
    city.using_click('#react-select-4-option-1')
    '''
    OR:
    city = dropdown.Dropdown(browser.element('#react-select-4-input'))
    city.using_enter('Karnal')
    '''

    browser.element('#submit').perform(command.js.click)
    '''
    I can't click using browser.element('#submit').click() :(
    '''

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

