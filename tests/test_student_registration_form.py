from selene.support.shared import browser
from selene import by, have, command
from utils import delete_interrupt_elements, resource
from controls import datepicker, tags_input, dropdown, table_modal_content


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

    datepicker_using_keyboard = datepicker.DatePicker()
    datepicker_using_keyboard.element = browser.element('#dateOfBirthInput')
    datepicker_using_keyboard.input_the_date('31', 'Oct', '1998')
    '''
    OR:
    datepicker_using_mouse = DatePicker()
    datepicker_using_mouse.element = browser.element('#dateOfBirthInput')
    datepicker_using_mouse.click_the_date('1998', '9', '31')
    '''

    hobby_checkbox = browser.element(by.text('Sports'))
    hobby_checkbox.perform(command.js.scroll_into_view).click()

    subject = tags_input.TagsInput()
    subject.element = browser.element('#subjectsInput')
    subject.add_subject_using_tab('Social')
    '''
    OR:
    add_subject = TagsInput()
    add_subject.element = browser.element('#subjectsInput')
    add_subject.add_subject_using_click('Social', '0')
    '''

    avatar = browser.element('#uploadPicture')
    avatar.send_keys(resource('sadcat.png'))

    browser.element('#currentAddress').type('Saint Petersburg, ...')

    state_dropdown = dropdown.StateDropdown()
    state_dropdown.select_state_using_click('3')

    city_dropdown = dropdown.CityDropdown()
    city_dropdown.select_city_using_click('1')

    browser.element('#submit').perform(command.js.click)
    '''
    I can't click using browser.element('#submit').click() :(
    '''

    # THEN
    table = table_modal_content.Table()

    table.rows = browser.element('.modal-content').all('tr')
    table.rows.should(have.exact_texts('Label Values',
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
