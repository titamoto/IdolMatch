#!/usr/bin/env python3
from db.session import session
from db.idols import populate_idols
# from faker import Faker
# import random

from db.models import Idol, User

# fake = Faker()

def seed():

    def delete_records():
        session.query(Idol).delete()
        session.query(User).delete()
        session.commit()

    def create_records():
        populate_idols()
        test_user = User(email='user@test.com', type='ENTJ')
        session.add(test_user)
        session.commit()


    if __name__ == '__main__':
        delete_records()
        create_records()






    

