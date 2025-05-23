from fuzzywuzzy import fuzz
import unicodedata
import os
import shutil
import json
import tkinter as tk
from tkinter import messagebox

class File_distributor():
    def __init__(self):
        self.from_folder = ""
        self.to_folder = ""
        self.get_src()
    
    def clear_name(self, name: str) -> str:
        """
            Normalize the employee's name: remove accents, eliminate unnecessary words ('de', 'da', 'do', 'das', 'dos'), and convert all characters to lowercase.

            Input:
                - name (Employee's name)
                
            Output:
                - name (Processed employee's name).
        """
        stopwords = {"de", "da", "do", "das", "dos"} 
        name = unicodedata.normalize("NFKD", name).encode("ASCII", "ignore").decode("ASCII")
        name =  " ".join(name.split())
        name = name.lower()
        name = " ".join([word for word in name.split() if word not in stopwords])
        return name

    def validate_name_match(self, first_name: str, second_name: str, similarity_score: int = 85) -> bool:
        """
            Compare two names based on similarity score and return a boolean value.

            Input:
                - first_name (First employee's name)
                - second_name (Second employee's name)
                - similarity_score (Similarity rate: 100% means exactly the same, 0% means completely different)
                
            Output:
                - bool (Boolean indicating whether the name matches the given similarity threshold).
        """
        first_name = self.clear_name(first_name)
        second_name = self.clear_name(second_name)

        similarity = fuzz.ratio(first_name, second_name)

        if similarity >= similarity_score:
            return True
        else:
            return False

    def check_addresses(self, *addresses: str) -> None:
        """
            Check if the file paths exist on the computer. If not, return a ValueError.

            Input:
                - *addresses (File paths)
        """
        for address in addresses:
            if not os.path.exists(address):
                raise ValueError(f"Endereço invalido: {address}")

    def save_src(self, source: str, destination: str) -> None:
        """
            Verify and save the source and destination folder paths in a JSON file named "src_save.json" at the project root.

            Input:
                - source (Source path)
                - destination (Destination path)
        """
        source = os.path.normpath(source)
        destination = os.path.normpath(destination)

        self.check_addresses(source, destination)
        
        datas = {
            "from_folder": source,
            "to_folder": destination,
        }

        json_str = json.dumps(datas)

        with open("src_save.json", "w") as file:
            file.write(json_str)
        
        self.get_src()

    def get_src(self) -> None:
        """
            Retrieve the source and destination paths from the "src_save.json" file at the project root and store them in the class variables: from_folder and to_folder.
        """
        empty_path = os.path.exists("src_save.json")
        if not empty_path:
            self.from_folder = ""
            self.to_folder = ""
            return

        try:
            with open("src_save.json", "r") as file:
                json_str = file.read()
        except:
            raise Exception(f"Não foi possivel recuperar o endereço do arquivo src_save.json")
        
        datas = json.loads(json_str)

        self.from_folder = datas["from_folder"]
        self.to_folder = datas["to_folder"]
                
    def _find_pdfs_files(self, address_file) -> list:
        """
            Identify PDF files in a directory and extract information from their filenames.

            Input:
                - address_file (str): Path to the directory containing the files.

            Output:
                - list: A list of dictionaries with extracted details, including:
                    - employee_name (str): Employee's name.
                    - origin_address (str): Full path of the file.
                    - subfolder (str or None): Subfolder, if applicable.
                    - new_file_name (str): Processed filename.
        """
        pdf_files = []

        for file_name in os.listdir(address_file):
            full_path = os.path.join(address_file, file_name)
            is_pdf = os.path.isfile(full_path) and file_name.lower().endswith(".pdf")
            if is_pdf:
                parts = file_name.split("; ")
                
                info_pdf = {}
                if len(parts) == 3:
                    info_pdf = {
                        "employee_name": parts[0],
                        "origin_address": full_path,
                        "subfolder": parts[1],
                        "new_file_name": parts[2],
                    }
                elif len(parts) == 2:
                    info_pdf = {
                        "employee_name": parts[0],
                        "origin_address": full_path,
                        "subfolder": None,
                        "new_file_name": parts[1],
                    }
                else:
                    continue
                
                pdf_files.append(info_pdf)
       
        pdf_files = sorted(pdf_files, key=lambda x: x["employee_name"])
        return pdf_files

    def _list_folders(self, address_file) -> list:
        """
            Identify subfolders in a directory and extract information from their names.

            Input:
                - address_file (str): Path to the directory where the subfolders are located.

            Output:
                - list: A list of dictionaries with extracted details, including:
                    - folder_name (str): Name of the subfolder.
                    - full_path (str): Full path of the subfolder.
        """
        folder_list = []

        for folder_name in os.listdir(address_file):
            full_path = os.path.join(address_file, folder_name)
            if os.path.isdir(full_path):
                info_dir = {
                        "name": folder_name,
                        "address": full_path
                    }
                folder_list.append(info_dir)
        
        folder_list = sorted(folder_list, key=lambda x: x["name"])
        return folder_list

    def rename(self) -> None:
        """
            Retrieve the source folder and rename PDF files within it.

            Process:
                - Obtain the source directory.
                - If the source folder is empty, return.
                - List all PDF file names in the source folder.
                - Rename each file based on processed file names.

            Output:
                - None: Files are renamed within the source folder. 
        """
        self.get_src()

        if self.from_folder == "":
            raise ValueError("Informe o endereço de origem.")

        pdf_files_list = self._find_pdfs_files(self.from_folder)
        
        for pdf in pdf_files_list:
                pdf_address = pdf["origin_address"]
                new_file_name = os.path.join(self.from_folder, pdf["new_file_name"])                     
                
                os.rename(pdf_address, new_file_name)

    def _move_pdf(self, origin_address, final_path) -> None:
        """
            Move a PDF file from one directory to another, verifying the existence of the destination file and requesting confirmation if it already exists.

            Input:
                - origin_address (str): Path to the original PDF file.
                - final_path (str): Destination path for the PDF file.

            Output:
                - None: The file is moved to the destination if confirmed by the user.
        """
        if os.path.exists(final_path):
            root = tk.Tk()
            root.withdraw()
            resp = messagebox.askyesno("Confirmação", f"O arquivo '{os.path.basename(final_path)}' já existe. Deseja sobrescrevê-lo?")

            if not resp:
                return
        
        try:
            shutil.move(origin_address, final_path)
        except Exception as e:
            raise OSError(f"Erro inesperado ao mover o arquivo: {e}")
            
    def distribute_files(self) -> None:
        """
            Distribute PDF files among corresponding folders based on naming criteria.

            Input:
                - No direct arguments (uses class attributes).

            Process:
                - Retrieve the source and destination directories for the PDF files.
                - Identify PDF files in the source folder.
                - List available folders in the destination directory.
                - Check for matches between file names and folder names.
                - If a corresponding subfolder exists, adjust the destination path.
                - Move the files to the appropriate folder.

            Output:
                - None: Files are correctly distributed into the corresponding folders.
        """
        self.get_src()

        if self.from_folder == "" or self.to_folder == "":
            raise ValueError("Informe os endereços de origem e destino.")

        pdf_files_list = self._find_pdfs_files(self.from_folder)
        folder_list = self._list_folders(self.to_folder)
        
        for pdf in pdf_files_list:
            for folder in folder_list:
                if not self.validate_name_match(pdf["employee_name"], folder["name"]):
                    continue

                pdf_origin_address = pdf["origin_address"]
                new_pdf_name = pdf["new_file_name"]
                target_folder_path = folder["address"]                

                if pdf["subfolder"]:
                    subfolders_list = self._list_folders(folder["address"])
                    for target_subfolder in subfolders_list:
                        if self.validate_name_match(pdf["subfolder"], target_subfolder["name"]):
                            target_folder_path = target_subfolder["address"]
                            break 
    
                final_pdf_path = os.path.join(target_folder_path, new_pdf_name)

                self._move_pdf(pdf_origin_address, final_pdf_path)