import os
import shutil
import json

class File_distributor():
    def __init__(self):
        self.from_folder = ""
        self.to_folder = ""
        self.get_src()

    def distribute_files(self):
        self.get_src()

        if self.from_folder == "" or self.to_folder == "":
            return

        file_names= os.listdir(self.from_folder)

        for name_with_extension in file_names:
            file_extension = os.path.splitext(name_with_extension)[1]
            file_name = os.path.splitext(name_with_extension)[0]

            list_of_names = file_name.split(" - ")
            if len(list_of_names) != 3:
                return
            
            main_folder = list_of_names[0]
            subfolder = list_of_names[1]
            observation = list_of_names[2]
            
            new_file_name = f"{observation}{file_extension}"

            file_origin = f"{self.from_folder}/{name_with_extension}"
            file_destination = f"{self.to_folder}/{main_folder}/{subfolder}/{new_file_name}" 

            if os.path.exists(f"{self.to_folder}/{main_folder}/{subfolder}/{new_file_name}"):
                print(f"O arquivo ({name_with_extension}) não pode ser renomeado para ({new_file_name}), pois, já exite um arquivo com esse nome na pasta de destino")
                continue

            try:
                shutil.move(file_origin, file_destination)
            except FileNotFoundError:
                print(name_with_extension)

    def save_src(self, source = str, destination = str):
        datas = {
            "from_folder": source,
            "to_folder": destination,
        }

        json_str = json.dumps(datas)

        with open("src_save.json", "w") as file:
            file.write(json_str)
        
        self.get_src()


    def get_src(self):

        try:
            with open("src_save.json", "r") as file:
                json_str = file.read()
        except:
            return
        
        datas = json.loads(json_str)

        self.from_folder = datas["from_folder"]
        self.to_folder = datas["to_folder"]

    
    def rename(self):
        self.get_src()
        file_names= os.listdir(self.from_folder)

        for name_with_extension in file_names:
            file_extension = os.path.splitext(name_with_extension)[1]
            file_name = os.path.splitext(name_with_extension)[0]

            list_of_names = file_name.split(" - ")
            if len(list_of_names) != 3:
                return
            
            observation = list_of_names[2]
            
            new_file_name = f"{observation}{file_extension}"

            os.rename(f"{self.from_folder}\{name_with_extension}", f"{self.from_folder}\{new_file_name}")

           

           