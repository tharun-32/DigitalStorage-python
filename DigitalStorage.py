from UserLogs import UserLogs
from FileOperation import FileOperations

# Digital storage for files with security
print("""Welcome to Digital Storage
Your files are Safe and Secure
      """)

# Log in or Register for new user
print("""1. SignIn
2. SignUp
      """)

while True:
    userLoginChoice = int(input("> "))
    # creating object to access UserLogs class
    user = UserLogs()
    if userLoginChoice == 1:
        print("Sign In")
        print(user.SignIn())
        print("\n")
        break
    else:
        print("Sign Up")
        print(user.SignUp())
        print("\n")
        break

while True:
    print("""enter the file operation
    1. show Available file
    2. Add file
    3. View file
    4. Write file
    5. Delete file
    6. Logout""")
    file_operation = int(input("> "))
    file = FileOperations()
    if file_operation == 1:
        file.available_files()
        print("\n")
    if file_operation == 2:
        file.add_file()
        print("\n")
    elif file_operation == 3:
        file.view_file()
        print("\n")
    elif file_operation == 4:
        file.write_file()
        print("\n")
    elif file_operation == 5:
        file.delete_file()
        print("\n")
    elif file_operation == 6:
        file.logout()



