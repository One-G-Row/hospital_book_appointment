
from sqlalchemy import Column, Integer, String
from ..database.connection import Base, session
from .appointment import Appointment

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable = False)
    specialization = Column(String, nullable = False)
    
    
    @classmethod
    def create(cls, name, specialization):
        new_doctor = cls(name=name, specialization=specialization)
        session.add(new_doctor)
        session.commit()
        return new_doctor
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
        
    @classmethod
    def find_by_id(cls, id):
      return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def find_by_name(cls, name):
      doctor = session.query(cls).filter_by(name=name).first()
      return doctor
      
    @classmethod
    def find_by_specialization(cls, specialization):
      doctor = session.query(cls).filter_by(specialization=specialization).first()
      return doctor
    
    def view_appointments(self):
        return session.query(Appointment).filter_by(doctor_id=self.id).all()  

    def delete(doctor_id):
        session.query(Doctor).filter_by(id=doctor_id).delete()
        session.commit()

    def save(self):
        session.add(self)
        session.commit()

    #def __repr__(self):
        #return f" Doctor(id={self.id}, name={self.name})"
        