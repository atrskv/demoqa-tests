from demoqa_tests.data import User, Gender, States, Cities, Subjects, Hobbies
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
        .set_gender(Gender.Male.value)
        .set_phone(student.phone)

        .set_date_of_birth(
            student.birthday_day,
            student.birthday_month.value,
            student.birthday_year
        )

        .set_hobby(
            Hobbies.sports,
            Hobbies.music,
            Hobbies.reading
        )

        .set_subjects(
            Subjects.chemistry,
            Subjects.history,
            Subjects.computer_science
        )

        .set_avatar(student.avatar)
        .set_adress(student.address)
        .set_state(States.NCR.value)
        .set_city(Cities.Noida.value)
        .submit()
      )

    # THEN
    (
        app.results
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
        f'State and City {States.NCR.name} {Cities.Noida.name}')
    )