from selene.support.shared import browser
from selene import by, have, command
from utils import delete_interrupt_elements
import os


def test_register_a_student():

    # GIVEN
    browser.open('/automation-practice-form')
    delete_interrupt_elements()

    # WHEN
    browser.element('#firstName').type('Aleksei')
    browser.element('#lastName').type('Torsukov')

    browser.element('#userEmail').type('trrskv@gmail.com')

    male = browser.element('[for="gender-radio-1"] ')

    '''
         I didn't use #gender-radio-1, 
         because "Other element would receive the click..."
    '''

    male.click()

    mobile_phone = browser.element('#userNumber').type('8999241221')
    mobile_phone.click()

    calendar_open = browser.element('#dateOfBirthInput')
    calendar_open.click()

    browser.element('[class$=year-select] [value="1998"]').click()
    browser.element('[class$=month-select] [value="9"]').click()
    browser.element('.react-datepicker__day--031').click()

    hobby_checkbox = browser.element(by.text('Sports'))
    hobby_checkbox.perform(command.js.scroll_into_view).click()

    subject = browser.element('#subjectsInput')
    subject.click()
    subject.type('Social Studies').press_tab()

    avatar = browser.element('#uploadPicture')
    avatar.send_keys(os.path.abspath('resources/sadcat.png'))

    browser.element('#currentAddress').type('Saint Petersburg, ...')

    state_dropdown = browser.element('#react-select-3-input')
    state_dropdown.type('Rajasthan').press_tab()

    city_dropdown = browser.element('#react-select-4-input')
    city_dropdown.type('Jaiselmer').press_tab()

    browser.element('#submit').perform(command.js.click)

    '''
    I can't click using browser.element('#submit').click() :(
    '''

    # THEN
    browser.element('.modal-content').all('tr').should(have.exact_texts
        ('Label Values',
         'Student Name Aleksei Torsukov',
         'Student Email trrskv@gmail.com',
         'Gender Male',
         'Mobile 8999241221',
         'Date of Birth 31 October,1998',
         'Subjects Social Studies',
         'Hobbies Sports',
         'Picture sadcat.png',
         'Address Saint Petersburg, ...',
         'State and City Rajasthan Jaiselmer'))

    '''
    OR we can use f-strings with variables, but I used variables only for selectors readability 
    '''