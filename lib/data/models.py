from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from .types import types
from session import session

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

idol_user = Table(
    'idol_user',
    Base.metadata,
    Column('id', Integer(), primary_key=True),
    Column('idol_id', ForeignKey('idol.id'), primary_key=False),
    Column('user_id', ForeignKey('user.id'), primary_key=False),
    extend_existing=True,
)

class Idol(Base):
    __tablename__ = 'idol'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    type = Column(String(4))
    type_alias = Column(String())
    match_type = Column(String())

    users = relationship("User", secondary=idol_user, back_populates="idols")

    def __repr__(self):
        return f'{self.name} is {self.type}, {self.type_alias}. His match types are {self.match_type}.'


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    email = Column(String())
    type = Column(String(4))
    type_alias = Column(String())

    idols = relationship("Idol", secondary=idol_user, back_populates="users")

    def persist_result(self):
        # self.idols = []
        # match = session.query(Idol).filter(Idol.match_type[:2] == self.type[:2]).first()
        # self.idols.append(match)
        session.add(self)
        session.commit()

    @classmethod
    def found_email(cls, email):
        if session.query(cls).filter(cls.email == email).first():
            return True  
    
    @classmethod
    def get_result(cls, email):
        return session.query(cls).filter(cls.email == email).first()
 
    @classmethod
    def delete_result(cls, email):
        session.query(cls).filter(cls.email == email).delete()
        session.commit()
        
    def __repr__(self):
        return f'Your type is {self.type}, {self.type_alias}. You match from BTS:{self.idols}'
    
    # def __repr__(self):
    #     return f'Your type is {self.type}, {self.type_alias}. You match from BTS:\n{[idol.name for idol in self.idols if idol.match_type[:2] == self.type[:2]]}'

