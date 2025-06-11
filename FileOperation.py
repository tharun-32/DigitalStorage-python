import os


class FileOperations:
    def add_file(self):
        try:
            file_name = input("enter your file name: ")
            file_path = os.path.join("FileData",file_name)
            with open(file_path, "w") as file:
                no_lines = int(input("enter the no of lines you need to write in file: "))
                print("enter your text")
                for _ in range(no_lines):
                    content = input("->")
                    file.write(content+"\n")
                file.close()
        except Exception:
            print("enter the correct file name")


    def view_file(self):
        try:
            file_name = input("enter your file name: ")
            file_path = os.path.join("FileData",file_name)
            with open(file_path, "r") as file:
                for line in file:
                    print(line.strip())
                file.close()
        except Exception:
            print("enter the correct file name")

    def write_file(self):
        try:
            file_name = input("enter your file name: ")
            file_path = os.path.join("FileData",file_name)
            with open(file_path, "a") as file:
                no_lines = int(input("enter the no of lines you need to write in file: "))
                print("enter your text")
                for _ in range(no_lines):
                    content = input("->")
                    file.write(content+"\n")
                file.close()
        except Exception:
            print("enter the correct file name")

    def delete_file(self):
        try:
            file_name = input("enter your file name: ")
            file_path = os.path.join("FileData",file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                print("file not found")
        except Exception:
            print("enter the correct file name")

    def available_files(self):
        folder_path = "FileData"
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            print("available fies")
            for file in files:
                print("—", file)
        else:
            print("❌ Folder not found.")
    def logout(self):
        exit()
