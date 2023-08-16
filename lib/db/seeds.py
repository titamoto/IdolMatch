#!/usr/bin/env python3
from session import session
from test import questions
from idols import populate_idols
# from faker import Faker
# import random

from models import Idol, User

# fake = Faker()

def delete_records():
    session.query(Idol).delete()
    session.query(User).delete()
    session.commit()

def create_records():
    populate_idols()
    # test_user = User(email='user@test.com', type='ENTJ', type_alias='', idol_id='')


if __name__ == '__main__':
    delete_records()
    create_records()






    

