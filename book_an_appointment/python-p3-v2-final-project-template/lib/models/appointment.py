# lib/models/appointment.py
from sqlalchemy import Column, Integer, String, ForeignKey
from lib.database.connection import Base, session

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    
    #book _appointment/ create an appointment
    @classmethod
    def book_appointment(cls, user_id, doctor_id, date, time):
        try:
            new_appointment = cls(user_id=user_id, doctor_id = doctor_id, date=date, time=time)
            session.add(new_appointment)
            session.commit()
        except Exception as e:
            print(f"Error booking appointment: {str(e)}")
            session.rollback()  

    #view all appointments
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()
    
    #view appointments based on the user id provided
    def view_appointments(self):
        return session.query(Appointment).filter_by(user_id=self.id).all()
    
    #cancel/delete an appointment
    def cancel_appointment(appointment_id):
        session.query(Appointment).filter_by(id=appointment_id).delete()
        session.commit()

    def __repr__(self):
        return f"<Appointment(date={self.date}, time={self.time}, doctor_id={self.doctor_id}, user_id={self.user_id})>"
