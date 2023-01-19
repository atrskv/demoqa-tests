import allure

from demoqa_tests.data import User, Gender, States, Cities, Subjects, Hobbies
from demoqa_tests.model import app
from utils.utils import delete_interrupt_elements


student = User()


@allure.title('Register a student')
def test_register_a_student(browser_management):

    # GIVEN:
    with allure.step('Открыть форму регистрации студента'):
        (
            app.form
            .open()
        )

    delete_interrupt_elements()

    # WHEN:
    with allure.step('Заполнить поле "Name"'):
        (
            app
            .form.set_name(student.name)
        )

    with allure.step('Заполнить поле "Lastname"'):
        (
            app
            .form.set_lastname(student.lastname)
        )

    with allure.step('Заполнить поле "Email"'):
        (
            app
            .form.set_email(student.email)
        )

    with allure.step('Заполнить поле "Gender"'):
        (
            app
            .form.set_gender(Gender.Male.value)
        )

    with allure.step('Заполнить поле "Mobile"'):
        (
            app
            .form.set_phone(student.phone)
        )

    with allure.step('Заполнить поле "Date of Birth"'):
        (
            app
            .form
            .set_date_of_birth(

                student.birthday_day,
                student.birthday_month.value,
                student.birthday_year
            )
        )

    with allure.step('Заполнить поле "Subjects"'):
        (
            app
            .form
            .set_hobby(

                Hobbies.sports,
                Hobbies.music,
                Hobbies.reading
            )
        )

    with allure.step('Заполнить поле "Hobbies"'):
        (
            app
            .form
            .set_subjects(

                Subjects.chemistry,
                Subjects.history,
                Subjects.computer_science
            )
        )

    with allure.step('Загрузить аватар в формате PNG'):
        (
            app
            .form
            .set_avatar(student.avatar)
        )

    with allure.step('Заполнить поле "Current Address"'):
        (
            app
            .form
            .set_adress(student.address)
        )

    with allure.step('Заполнить поле "State"'):
        (
            app
            .form
            .set_state(States.NCR.value)
        )

    with allure.step('Заполнить поле "City"'):
        (
            app
            .form
            .set_city(Cities.Noida.value)
        )

    with allure.step('Нажать на кнопку "Submut"'):
        (
            app
            .form
            .submit()
        )

    # THEN:
    with allure.step('Проверить результаты в модальном окне'):
        (
            app
            .results
            .should_have_rows_with_exact_texts(
            'Label Values',
            f'Student Name {student.name} {student.lastname}',
            f'Student Email {student.email}',
            f'Gender {Gender.Male.name}',
            f'Mobile {student.phone}',
            f'Date of Birth {student.birthday_day} {student.birthday_month.name},{student.birthday_year}',
            f'Subjects {Subjects.chemistry}, {Subjects.history}, {Subjects.computer_science}',
            f'Hobbies {Hobbies.sports}, {Hobbies.music}, {Hobbies.reading}',
            f'Picture {student.avatar}',
            f'Address {student.address}',
            f'State and City {States.NCR.name} {Cities.Noida.name}'
        )
    )
