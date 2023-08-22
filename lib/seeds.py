#!/usr/bin/env python3
from session import session
from data.idols import bts
from data.types import types, find_type_dict
from faker import Faker
import random

from data.models import Idol, User, idol_user

fake = Faker()

def seed():
    print('Populating the database...')
    def delete_records():
        session.query(idol_user).delete()
        session.query(Idol).delete()
        session.query(User).delete()
        session.commit()

    def create_records():

        users = []
        idols = []
        for idol in bts:
            session.add(idol)
            session.commit()
            idols.append(idol)
        for i in range(20):
            user = User(
                email=fake.email(),
                type=random.choice([type['type'] for type in types])
            )
            user.type_alias=find_type_dict(user.type)['alias']
            user.idols = [idol for idol in idols if user.type in idol.match_type]
            session.add(user)
            session.commit()
            users.append(user)

    delete_records()
    create_records()

seed()
