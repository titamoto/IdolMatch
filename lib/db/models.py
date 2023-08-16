from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.session import session
# from idols import populate_idols

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

    @classmethod
    def persist_result(self):
        session.add(self)
        session.commit()

    def __repr__(self):
        return f'Your type is {self.type}, {self.type_alias}. Your BTS match is {self.idol.name}. ' + \
              f'Disclaimer: relationships with BTS members are not garanteed.'  






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
