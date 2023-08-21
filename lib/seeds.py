#!/usr/bin/env python3
from session import session
from data.idols import populate_idols
from data.types import types, find_type_dict
from faker import Faker
import random

from data.models import Idol, User

fake = Faker()

def seed():

    def delete_records():
        session.query(Idol).delete()
        session.query(User).delete()
        session.commit()


    def create_records():
        populate_idols()
        test_user = User(email='user@test.com', type='ENTJ', type_alias=find_type_dict('ENTJ')['alias'])
        users = []
        for i in range(20):
            user = User(
                email=fake.email(),
                type=random.choice([type['type'] for type in types])
            )
            user.type_alias=find_type_dict(user.type)['alias']
            session.add(user)
            session.commit()
            users.append(user)

        session.add(test_user)
        session.commit()

    delete_records()
    create_records()






    

