from selene.support.shared import browser


def delete_interrupt_elements():
    browser.execute_script('''
    document.querySelector('.Advertisement-Section')
    .remove()''')


'''
I don't have google ads, but I really wanted to use browser.execute_script()  :D
'''