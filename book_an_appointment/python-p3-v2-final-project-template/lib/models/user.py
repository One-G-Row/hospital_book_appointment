# lib/models/user.py
from sqlalchemy import Column, Integer, String
from ..database.connection import Base, session
from .appointment import Appointment


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)


    @classmethod
    def create(cls, name, email):
        new_user = cls(name=name, email=email)
        session.add(new_user)
        session.commit()
        return new_user
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
      return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def find_by_name(cls, name):
      return session.query(cls).filter_by(name=name).first()

    def delete(user_id):
     session.query(User).filter_by(id=user_id).delete()
     session.commit()

    #def __repr__(self):
        #return f"<User(name={self.name}, email={self.email})>"
