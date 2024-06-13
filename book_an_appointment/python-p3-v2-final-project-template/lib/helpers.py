# lib/helpers.py
from .models.doctor import Doctor
from .models.user import User
from .models.appointment import Appointment
from .database.connection import session

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
def create_new_user(name, email):
    user = User.create(name, email)
    print([user.name, user.email])

def create_new_doctor(name, specialization):
    doctor = Doctor.create(name, specialization)
    print([doctor.name, doctor.specialization])

def find_doctor_by_name(name):
    doctor = Doctor.find_by_name(name)
    print([doctor.name, doctor.specialization]) if doctor else print(
        f'Doctor {name} not found. Please enter available doctor name.')
    
def find_doctor_by_id(id):
    doctor = Doctor.find_by_id(id)
    print([doctor.name, doctor.specialization]) if doctor else print(
        f'Doctor {id} not found. Please enter available doctor id.')
def find_doctor_by_specialization(specialization):
    doctor = Doctor.find_by_specialization(specialization)
    print([doctor.id, doctor.name, doctor.specialization]) if doctor else print(
        f'Doctor {specialization} not found. Please enter available doctor specialization.')
    
def find_user_by_name(name):
    user = User.find_by_name(name)
    print((user.id, user.name, user.email)) if user else print(
        f'User {name} not found. Please enter available user name.')
    
def find_user_by_id(id):
    user = User.find_by_id(id)
    print((user.id, user.name, user.email)) if user else print(
        f'User {id} not found. Please enter available user id.')
    
def book_user_appointment(user_id, doctor_id, date, time):
    """ user_id = input("Enter your user ID: ")
    doctor_id = input("Enter the doctor ID: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    time = input("Enter the time (HH:MM): ") """

    try:
        new_appointment = Appointment.book_appointment(user_id, doctor_id, date, time)
        appointment_id = new_appointment.id
        user = User.find_by_id(user_id)
        user.book_appointment_id = appointment_id
        session.commit()
        print("Appointment booked successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error booking appointment: {str(e)}")
    
def view_available_appointments(user_id):
    appointments = session.query(Appointment).filter_by(user_id=user_id).all()
    for appointment in appointments:
            print({f'Appointment {appointment.id}, Date: {appointment.date}, Time: {appointment.time}, Doctor ID: {appointment.doctor_id}, User ID: {appointment.user_id}'})
        
def view_all_appointments(user_id):
    appointments = Appointment.get_all()
    for appointment in appointments:
            print({f'Appointment {appointment.id}, Date: {appointment.date}, Time: {appointment.time}, Doctor ID: {appointment.doctor_id}, User ID: {appointment.user_id}'})

def view_available_doctors(doctor_id):
    doctors = session.query(Doctor).all()
    for doctor in doctors:
        print({f'Doctor {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}'})

def cancel_an_appointment(appointment_id):
    appointment = Appointment.cancel_appointment(appointment_id)
    print(f"Appointment {appointment_id} canceled successfully!")

def view_available_users(user_id):
    users = session.query(User).all()
    for user in users:
        print({f'User {user.id}, Name: {user.name}, Email: {user.email}'})

def delete_user(user_id):
    user = User.delete(user_id)
    print(f"User {user_id} deleted successfully!")

def delete_doctor(doctor_id):
    doctor = Doctor.delete(doctor_id)
    print(f"Doctor {doctor_id} deleted successfully!")