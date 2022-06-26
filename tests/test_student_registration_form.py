from selene.support.shared import browser
from selene import be, have  # command


data = ['English', 'Computer Science', 'Social Studies']


def test_fill_all_the_fields():
    browser.open('/automation-practice-form')
    delete_all_the_useless_elements()

    browser.element('#firstName').should(be.blank).type('Aleksei')
    browser.element('#lastName').should(be.blank).type('Torsukov')
    browser.element('#userEmail').should(be.blank).type('trrskv@gmail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('8999241221')
    browser.element('#dateOfBirthInput').click()
    browser.element('option[value="9"]').click()
    browser.element('option[value="1998"]').click()
    browser.element('.react-datepicker__day--031').click()

    for subject in data:
        browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()

    browser.element('label[for="hobbies-checkbox-3"]').click()  # .perform(command.js.scroll_into_view)
    browser.element('#uploadPicture').type(
        '/Users/torsukov/Documents/demoqa-tests/tests/images/sadcat.png'
    )
    browser.element('#currentAddress').type('Saint Petersburg, ...')
    browser.element('#state input').type('Rajasthan').press_tab()
    browser.element('#city input').type('Jaiselmer').press_tab()
    browser.element('#submit').click()

    browser.element('tbody').should(have.text('Aleksei Torsukov'))
    browser.element('tbody').should(have.text('trrskv@gmail.com'))
    browser.element('tbody').should(have.text('Male'))
    browser.element('tbody').should(have.text('8999241221'))
    browser.element('tbody').should(have.text('31 October,1998'))
    browser.element('tbody').should(have.text('English, Computer Science, Social Studies'))
    browser.element('tbody').should(have.text('Music'))
    browser.element('tbody').should(have.text('sadcat.png'))
    browser.element('tbody').should(have.text('Saint Petersburg, ...'))
    browser.element('tbody').should(have.text('Rajasthan Jaiselmer'))


def delete_all_the_useless_elements():
    browser.execute_script('''
    document.querySelector('footer').remove()
    document.querySelector('#close-fixedban').remove()
    ''')
