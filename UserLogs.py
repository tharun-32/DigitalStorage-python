import json
import os
from getpass import getpass


class UserLogs:
    def SignUp(self):
        user_name = input("username: ")
        password = getpass("password: ")
        # checks whether json file is present if not creates a new dictionary to save user logs
        if os.path.exists("userlogs.json"):
            with open("userlogs.json", "r") as file:  # reads the json file
                try:
                    userlogs = json.load(
                        file
                    )  # converts the json file into python dictionary to add user name and password
                except (
                    json.JSONDecodeError
                ):  # this catches the error of file empty or some error converting
                    userlogs = {}  # if error creates fresh dictionary
        else:
            userlogs = {}

        userlogs[user_name] = password  # stores the logs to dictionary

        with open("userlogs.json", "w") as file:  # to write the file
            json.dump(
                userlogs, file, indent=4
            )  # this converts the dictionary back to json file
        return "User Registed Successfully"

    def SignIn(self):
        # checks whether json file is present if not creates a new dictionary to save user logs
        if os.path.exists("userlogs.json"):
            with open("userlogs.json", "r") as file:  # reads the json file
                try:
                    userlogs = json.load(
                        file
                    )  # converts the json file into python dictionary to add user name and password
                except (
                    json.JSONDecodeError
                ):  # this catches the error of file empty or some error converting
                    userlogs = {}  # if error creates fresh dictionary
        else:
            userlogs = {}

        while True:
            user_name = input("username: ")
            if user_name in userlogs:
                password = getpass("password: ")
                if userlogs[user_name] == password:
                    return "Login is successfully"
                else:
                    print("wrong password")
            else:
                print("username not found")
