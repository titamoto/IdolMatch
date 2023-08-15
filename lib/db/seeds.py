#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from test import questions
# import random

from models import Idol, User, Test

if __name__ == '__main__':
    engine = create_engine('sqlite:///idolmatch.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Idol).delete()
    session.query(User).delete()
    session.query(Test).delete()

    fake = Faker()

    # Jin: INTP, The Thinker, match is ENTJ, ENFJ; 
    jin = Idol(
        name='Jin',
        type='INTP',
        type_alias='The Thinker',
        match_type='ENTJ, ENFJ'
    )
   # Jungkook: INTP, The Thinker, match is ENTJ, ENFJ
    jungkook = Idol(
        name='Jungkook',
        type='INTP',
        type_alias='The Thinker',
        match_type='ENTJ, ENFJ'
    )
    # Suga: ISTP, The Crafter, match is ESTJ, ESFJ;
    suga = Idol(
        name='Suga',
        type='ISTP',
        type_alias='The Crafter',
        match_type='ESTJ, ESFJ'
    )
    # J-Hope: INFJ, The Advocate, match is ENFP, ENTP;
    jhope = Idol(
        name='J-Hope',
        type='INFJ',
        type_alias='The Advocate',
        match_type='ENFP, ENTP'
    )
    # RM: ENFP, The Champion, match is INTJ, INFJ;
    rm = Idol(
        name='RM',
        type='ENFP',
        type_alias='The Champion',
        match_type='INTJ, INFJ'
    )
   # Jimin: ESTP, The Persuader, match is ISFJ, ISTJ;
    jimin = Idol(
        name='Jimin',
        type='ESTP',
        type_alias='The Persuader',
        match_type='ISFJ, ISTJ'
    )
    # V: INFP, The Mediator, ENTJ, ENFJ;
    v = Idol(
        name='V',
        type='INFP',
        type_alias='The Mediator',
        match_type='ENTJ, ENFJ'
    )



    

