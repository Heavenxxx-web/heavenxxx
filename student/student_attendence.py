def add_student():
    print("you are on add student function")


def update_student():
    print("you are on update student function")

def delete_student():
    print("you are on ")
def view_students():
    print("you are on view students function")
def take_attendance():
    print("you are on take attendance function")
def view_attendance():
    print("you are on view attendance function")
def exit_program():
    print("you are on exit program function")

print("Enter 1 to add a student")
print()
print("Enter 2 to update Student")
print()
print("Enter 3 to delete a student")
print()
print("Enter 4 to view students")
print()
print("Enter 5 to take attendance")
print()
print("Enter 6 to view attendance")
print("Enter 7 to exit")

while True:
    option = input("Enter Menu No:")
    if option == "1":
        add_student()
    elif option == "2":
        update_student()
    elif option == "3":
        delete_student()
    elif option == "4":
        view_students()
    elif option == "5":
        take_attendance()
    elif option == "6":
        view_attendance()
    elif option == "7":
        print("Exiting the program")
    else:
        print("Invalid option, please try again.")
        break