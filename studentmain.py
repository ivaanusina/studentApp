from student import Student
from studentcontroller import StudentController

students = {}

def add_student():
    print("YOU CHOOSE ADD A STUDENT")
    dni = input("Enter DNI: ")
    name = input("Enter Name: ")
    surnames = input("Enter Surnames: ")
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age. Please enter a valid number.")
        return
    city = input("Enter City: ")
    province = input("Enter Province: ")
    email = input("Enter Email: ")

    if StudentController.addStudent(dni, name, surnames, age, city, province, email):
        print("Student added successfully.")
    else:
        print("Student with this DNI already exists.")

def delete_student():
    dni = input("Enter DNI to delete: ")
    if StudentController.delStudent(dni):
        print("Student with DNI", dni, "deleted successfully.")
    else:
        print("Student with this DNI does not exist.")

def modify_student():
    dni = input("Enter DNI to modify: ")
    if dni in students:
        print("Modification of student with DNI:", dni)
        print("1.- Modify Name")
        print("2.- Modify Surname")
        print("3.- Modify Age")
        print("4.- Modify City")
        print("5.- Modify Province")
        print("6.- Modify Email")
        choice = input("What do you want to modify (1-6): ")
        if choice == "1":
            new_name = input("Enter new Name: ")
            students[dni].setName(new_name)
        elif choice == "2":
            new_surnames = input("Enter new Surnames: ")
            students[dni].setSurnames(new_surnames)
        elif choice == "3":
            try:
                new_age = int(input("Enter new Age: "))
                students[dni].setAge(new_age)
            except ValueError:
                print("Invalid age. Please enter a valid number.")
        elif choice == "4":
            new_city = input("Enter new City: ")
            students[dni].setCity(new_city)
        elif choice == "5":
            new_province = input("Enter new Province: ")
            students[dni].setProvince(new_province)
        elif choice == "6":
            new_email = input("Enter new Email: ")
            students[dni].setEmail(new_email)
        else:
            print("Invalid choice. Please enter a valid option (1-6).")
    else:
        print("Student with this DNI does not exist.")

def search_student():
    dni = input("Enter DNI to search: ")
    if dni in students:
        student = students[dni]
        print("Student found:")
        print("DNI:", student.getDni())
        print("Name:", student.getName())
        print("Surnames:", student.getSurnames())
        print("Age:", student.getAge())
        print("City:", student.getCity())
        print("Province:", student.getProvince())
        print("Email:", student.getEmail())
    else:
        print("Student with this DNI does not exist.")

while True:
    print("STUDENT CRUD")
    print("----------------------------")
    print("1.- Add a student")
    print("2.- Delete a student")
    print("3.- Modify a student")
    print("4.- Search a student")
    print("5.- Exit")
    option = input("Choose option: ")

    if option == "1":
        add_student()
    elif option == "2":
        delete_student()
    elif option == "3":
        modify_student()
    elif option == "4":
        search_student()
    elif option == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose a valid option (1-5).")