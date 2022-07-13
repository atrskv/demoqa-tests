from demoqa_tests.data import User, Gender
from demoqa_tests.model import app
from utils import delete_interrupt_elements


def test_register_a_student():

    # GIVEN
    student = User()

    (
        app.form
        .open()
    )

    delete_interrupt_elements()

    # WHEN
    (
        app.form
        .set_name(student.name)
        .set_lastname(student.lastname)
        .set_email(student.email)
        .set_gender(Gender.male.value)
        .set_phone(student.phone)
        .set_date_of_birth
        (
            student.birthday_day,
            student.birthday_month,
            student.birthday_year
        )
        .set_hobby(student.hobbies)
        .set_subjects(student.subjects)
        .set_avatar(student.avatar)
        .set_adress(student.address)
        .set_state(student.state)
        .set_city(student.city)
        .submit()
      )

    # THEN
    (
        app.results
        .should_have_rows_with_exact_texts(
                'Label Values',
        'Student Name Aleksei Torsukov',
        'Student Email trrskv@gmail.com',
        'Gender Male',
        'Mobile 8999241221',
        'Date of Birth 31 October,1998',
        'Subjects History, Chemistry',
        'Hobbies Sports',
        'Picture sadcat.png',
        'Address Saint Petersburg, ...',
        'State and City Rajasthan Jaiselmer')
    )