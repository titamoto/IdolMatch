from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/idolmatch.db")
Session = sessionmaker(bind=engine)
session = Session()