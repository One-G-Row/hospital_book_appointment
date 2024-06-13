# lib/cli.py

from .helpers import (
    exit_program,
    create_new_user,
    create_new_doctor,
    view_available_doctors,
    find_doctor_by_id,
    find_doctor_by_name,
    find_doctor_by_specialization,
    view_available_users,
    find_user_by_name,
    find_user_by_id,
    book_user_appointment,
    view_all_appointments,
    view_available_appointments,
    cancel_an_appointment, 
    delete_doctor,
    delete_user
   
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            user = input("Enter user name: ")
            email = input("Enter user email: ")
            create_new_user(user, email)
        elif choice == "2":
            doctor = input("Enter doctor name: ")
            specialization = input("Enter doctor specialization: ")
            create_new_doctor(doctor, specialization)
        elif choice == "3":
            doctor = ("List of available doctors: ")
            view_available_doctors(doctor)
        elif choice == "4":
            id = input("Enter the doctor's id: ")
            find_doctor_by_id(id)
        elif choice == "5":
            name = input("Enter the doctor's name: ")
            find_doctor_by_name(name)
        elif choice == "6":
            specialization = input("Enter the doctor's specialization: ")
            find_doctor_by_specialization(specialization)
        elif choice == "7":
            user = ("List of available users: ")
            view_available_users(user)
        elif choice == "8":
            name = input("Enter the user's name: ")
            find_user_by_name(name)
        elif choice == "9":
            id = input("Enter the user's id: ")
            find_user_by_id(id)
        elif choice == "10":
            user_id = input("Enter user ID: ")
             
            doctor_id = input("Enter doctor ID: ")
            
            date = input("Enter appointment date (YYYY-MM-DD): ")
            
            time = input("Enter appointment time (HH:MM): ")

            prompt = input("Book an appointment? (y/n): ")
            
            if prompt.lower() == "y":
                print(f"user_id: {user_id}") 
                print(f"doctor_id: {doctor_id}") 
                print(f"date: {date}") 
                print(f"time: {time}") 
                book_user_appointment(user_id, doctor_id, date, time)
                print("Appointment booked successfully!")
            else:
                print("No appointments booked.")
        elif choice == "11":
            appointment= ("List of all appointments: ")
            view_all_appointments(appointment)
        elif choice == "12":
            user_id = input("Enter user ID: ")
            if user_id == user_id:
                view_available_appointments(user_id)
            else:
                print("No booked appointments found.")
        elif choice == "13":
             appointment_id = input("Enter appointment ID: ")  
             cancel_an_appointment(appointment_id)    
        elif choice == "14":
            doctor_id = input("Enter doctor ID: ")
            delete_doctor(doctor_id)
        elif choice == "15":
            user_id = input("Enter user ID: ")
            delete_user(user_id)      
        else:
            print("Invalid choice. Please try again.")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create new user")
    print("2. Create new doctor")
    print("3. List of available doctors")
    print("4. Find doctor by id")
    print("5. Find doctor by name")
    print("6. Find doctor by specialization")
    print("7. List of available users")
    print("8. Find user by name")
    print("9. Find user by id")
    print("10. Book an appointment")
    print("11. View all appointments")
    print("12. View user appointments")
    print("13. Cancel an appointment")
    print("14. Delete doctor")
    print("15. Delete user")


if __name__ == "__main__":
    main()
