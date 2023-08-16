from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Idol
from db.session import session

def populate_idols():
    # Jin: INTP, The Thinker, match is ENTJ, ENFJ; 
    idols = []
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
    idols = [jin, jungkook, v, jimin, rm, jhope, suga]
    session.add_all(idols)
    session.commit()