#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from test import questions
from idols import populate_idols
# import random

from models import Idol, User, Test

engine = create_engine('sqlite:///idolmatch.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

if __name__ == '__main__':
    pass

def delete_records():
    session.query(Idol).delete()
    session.query(User).delete()
    session.query(Test).delete()
    session.commit()

def create_records():
    populate_idols()
    





    

