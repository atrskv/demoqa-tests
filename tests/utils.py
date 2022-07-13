from selene.support.shared import browser


def delete_interrupt_elements():
    browser.execute_script('''
    document.querySelector('.Advertisement-Section')
    .remove()
    '''
    )

'''
I don't have google ads, but I really wanted to use browser.execute_script()  :D
'''

def resource(path):
    import demoqa_tests
    from pathlib import Path
    return str(
        Path(demoqa_tests.__file__)
        .parent
        .parent
        .joinpath(f'resources/{path}')
    )
