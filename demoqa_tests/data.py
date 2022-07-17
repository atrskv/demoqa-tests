from dataclasses import dataclass
from enum import Enum


@dataclass
class States(Enum):
    NCR = '0'
    Uttar_Pradesh = '1'
    Haryana = '2'
    Rajastan = '3'


@dataclass
class Cities(Enum):
    Delhi = '0'
    Gurgaon = '1'
    Noida = '2'

    Agra = '0'
    Lucknow = '1'
    Merrut = '2'

    Karnal = '0'
    Panipat = '1'

    Jaipur = '0'
    Jaiselmer = '1'


@dataclass
class Subjects:
    history = 'History'
    social_studies = 'Social Studies'
    chemistry = 'Chemistry'
    hindi = 'Hindi'
    english = 'English'
    computer_science = 'Computer Science'


@dataclass
class Hobbies:
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class Gender(Enum):
    Male = '1'
    Female = '2'
    Other = '3'

@dataclass
class Months(Enum):
    January = '0'
    February = '1'
    March = '2'
    April = '3'
    May = '4'
    June = '5'
    July = '6'
    August = '7'
    September = '8'
    October = '9'
    November = '10'
    December = '11'


@dataclass
class User:
    name: str = 'Aleksei'
    lastname: str = 'Torsukov'
    email: str = 'trrskv@gmail.com'
    gender = Gender.Male.value
    phone: str = '8999241221'
    birthday_day = '31'
    birthday_year = '1998'
    birthday_month = Months.October
    subjects = Subjects.history, Subjects.chemistry
    avatar = 'sadcat.png'
    address = 'Saint Petersburg, ...'