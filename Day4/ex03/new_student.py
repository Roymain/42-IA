import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''generate id function'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''student class'''
    name: str
    surname: str
    active: bool = True
    ID: str = field(init=False)
    login: str = field(init=False)

    def __post_init__(self):
        '''post init function'''
        self.ID = generate_id()
        self.login = self.name[0] + self.surname
