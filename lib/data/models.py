from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .types import types
from session import session

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

idol_user = Table(
    'idol_user',
    Base.metadata,
    Column('idol_id', ForeignKey('idol.id'), primary_key=True),
    Column('user_id', ForeignKey('user.id'), primary_key=True),
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

    @classmethod    
    def email_found(cls, email_input):
        if session.query(cls).filter(cls.email == email_input).first():
            return True
    
    @classmethod
    def get_result(cls, email):
        return session.query(cls).filter(cls.email == email).all()
    
    @classmethod
    def delete_result(cls, email):
        session.query(cls).filter(cls.email == email).delete()
        session.commit()

    def persist_result(self):
        session.add(self)
        session.commit()

    def find_match(self):
        for idol in self.idols:
            if self.type in [type.strip() for type in idol.match_type.split(',')]:
                return idol.name
            else:
                return 'nobody'
        
    def __repr__(self):
        return f'Your type is {self.type}, {types[self.type]}. You match from BTS is {self.find_match()}'
