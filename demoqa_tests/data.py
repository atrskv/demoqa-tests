from dataclasses import dataclass
from enum import Enum


@dataclass
class States(Enum):
    ncr = '0'
    uttar_pradesh = '1'
    haryana = '2'
    rajastan = '3'


@dataclass
class Cities(Enum):
    jaipyr = '0'
    jaiselmer = '1'


@dataclass
class Subjects:
    history = 'History'
    social_studies = 'Social Studies'
    chemistry = 'Chemistry'


@dataclass
class Hobbies:
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class Gender(Enum):
    male = '1'
    female = '2'
    other = '3'


@dataclass
class User:
    name: str = 'Aleksei'
    lastname: str = 'Torsukov'
    email: str = 'trrskv@gmail.com'
    gender = Gender.male.value
    phone: str = '8999241221'
    birthday_day = '31'
    birthday_year = '1998'
    birthday_month = '9'
    subjects = Subjects.history, Subjects.chemistry
    avatar = 'sadcat.png'
    hobbies = Hobbies.sports
    address = 'Saint Petersburg, ...'
    state = States.rajastan.value
    city = Cities.jaiselmer.value
