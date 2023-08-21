#!/usr/bin/env python3
from session import session
from data.idols import bts
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
        test_user = User(email='user@test.com', type='ENTJ', type_alias=find_type_dict('ENTJ')['alias'])
        users = []
        idols = []
        for i in range(20):
            user = User(
                email=fake.email(),
                type=random.choice([type['type'] for type in types])
            )
            user.type_alias=find_type_dict(user.type)['alias']
            # user.idols = [idol for idol in idols if idol.match_type[:2] == user.type]
            session.add(user)
            session.commit()
            users.append(user)

        for idol in bts:
            idol.users = [user for user in users if idol.match_type[:2] == user.type[:2]]
            session.add(idol)
            session.commit()
            idols.append(idol)


        session.add(test_user)
        session.commit()

    delete_records()
    create_records()

