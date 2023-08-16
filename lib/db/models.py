from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from session import session
from idols import populate_idols

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Idol(Base):
    __tablename__ = 'idol'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    type = Column(String(4))
    type_alias = Column(String())
    match_type = Column(String())

    users = relationship("User", back_populates="idol")

    def __repr__(self):
        return f'Idol(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'type={self.type}) ' + \
            f'alias={self.match_type}'


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    email = Column(String())
    type = Column(String(4))
    type_alias = Column(String())

    idol_id = Column(Integer(), ForeignKey('idol.id'))
    idol = relationship("Idol", back_populates="users")
    # test = relationship("Test", back_populates="user", uselist=False)

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'email={self.email}, ' + \
            f'type={self.type}) ' + \
            f'alias={self.match_type}'
    
    @classmethod    
    def email_found(cls, email_input):
        if session.query(cls).filter(cls.email == email_input).first():
            return True






# class Test(Base):
#     __tablename__ = 'question'

#     id = Column(Integer(), primary_key=True)
#     question = Column(String())
#     answer = Column(Integer())

#     user_id = Column(Integer(), ForeignKey("user.id"))
#     # many-to-one scalar for preventing possible bugs
#     parent = relationship("Parent", back_populates="child")

#     def __repr__(self):
#         return f'Test(id={self.id}, ' + \
#             f'question={self.question}, ' + \
#             f'answer={self.answer})'
