from selene.support.shared import browser


def delete_all_the_useless_elements():
    browser.execute_script('''
    document.querySelector('footer').remove()
    document.querySelector('#close-fixedban').remove()
    ''')
