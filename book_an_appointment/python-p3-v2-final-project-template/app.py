# main.py
from lib.database.connection import session, Base, engine
from lib.models.doctor import Doctor
from lib.models.user import User
from lib.models.appointment import Appointment

Base.metadata.create_all(engine)

def main():
    # user input
    user_name = input("Enter user's name: ")
    user_email = input("Enter user's email: ")
    doctor_name = input("Enter doctor's name: ")
    doctor_specialization = ("Enter doctor's specialization: ")
    appointment_date = input("Enter appointment date: ")
    appointment_time = input("Enter appointment time: ")

    # Create a doctor
    new_doctor = Doctor(name=doctor_name, specialization=doctor_specialization)
    session.add(new_doctor)
    session.commit()
    doctor_id = new_doctor.id  

    # Create a user
    new_user = User(name=user_name, email=user_email)
    session.add(new_user)
    session.commit()
    user_id = new_user.id  

    # Create an appointment
    new_appointment = Appointment(date=appointment_date, time=appointment_time, doctor_id=doctor_id, user_id=user_id)
    session.add(new_appointment)
    session.commit()
    appointment_id = new_appointment.id 

    
    doctors = session.query(Doctor).all()
    users = session.query(User).all()
    appointments = session.query(Appointment).all()

    
    session.close()

    
    print("\nDoctors:")
    for doctor in doctors:
        print(f'Doctor {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}')

    print("\nUsers:")
    for user in users:
       print(f'User {user.id}, Name: {user.name}, Email: {user.email}')

    print("\nAppointments:")
    for appointment in appointments:
         print(f'Appointment {appointment.id}, Date: {appointment.date}, Time: {appointment.time},'
              f'Doctor ID: {appointment.doctor_id}, User ID: {appointment.user_id}')

if __name__ == "__main__":
    main()



