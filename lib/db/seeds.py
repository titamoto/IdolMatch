#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
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

    questions = [
                'makes lists 1 2 3 4 5 relies on memory',
                 'sceptical 1 2 3 4 5 wants to believe',
                 'bored by time alone 1 2 3 4 5 needs time alone',
                 'accepts things as they are 1 2 3 4 5unsatisfied with the ways things are',
                 'keeps a clean room 1 2 3 4 5 just puts stuff where ever',
                 'thinks "robotic" is an insult 1 2 3 4 5 strives to have a mechanical mind',
                 'energetic 1 2 3 4 5 mellow',
                 'prefer to take multiple choice test 1 2 3 4 5 prefer essay answers',
                 'chaotic 1 2 3 4 5 organized',
                 'easily hurt 1 2 3 4 5 thick-skinned',
                 'works best in groups 1 2 3 4 5 works best alone',
                 'focused on the present 1 2 3 4 5 focused on the future',
                 'plans far ahead 1 2 3 4 5 plans at the last minute',
                 "wants people's respect 1 2 3 4 5 wants their love",
                 'gets worn out by parties 1 2 3 4 5 gets fired up by parties',
                 'fits in 1 2 3 4 5 stands out',
                 'keeps options open 1 2 3 4 5 commits',
                 'wants to be good at fixing things 1 2 3 4 5 wants to be good at fixing people',
                 'talks more 1 2 3 4 5 listens more',
                 'when describing an event, will tell people what happened 1 2 3 4 5 when describing an event, will tell people what it meant',
                 'gets work done right away 1 2 3 4 5 procrastinates',
                 'follows the heart 1 2 3 4 5 follows the head',
                 'stays at home 1 2 3 4 5 goes out on the town',
                 'wants the big picture 1 2 3 4 5 wants the details',
                 'improvises 1 2 3 4 5 prepares',
                 'bases morality on justice 1 2 3 4 5 bases morality on compassion',
                 'finds it difficult to yell very loudly 1 2 3 4 5 yelling to others when they are far away comes naturally',
                 'theoretical 1 2 3 4 5 empirical',
                 'works hard 1 2 3 4 5 plays hard',
                 'uncomfortable with emotions 1 2 3 4 5 values emotions',
                 'likes to perform in front of other people 1 2 3 4 5 avoids public speaking',
                 'likes to know "who?", "what?", "when?" 1 2 3 4 5 likes to know "why?'
                 ]
