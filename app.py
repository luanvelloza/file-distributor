from tkinter import *
from models.file_distributor import File_distributor


def app_interface():
    window = Tk()
    window.title("Distribuidor de Arquivos")
    window.geometry("400x300")
    #window.resizable(False, False)

    frm = Frame(window, width=400, height=300, bg="white")
    frm.place(x=0, y=0)

    # Transition

    label_transition = Label(frm, text="Endereço da pasta de Transição", bg="white", font=('Tahoma', 11, "bold"))
    label_transition.place(x = 15, y = 15)

    input_adr_folder_transition = Entry(frm, width=52, fg="black", border=0, bg="white", font=("Tahoma", 9,))
    input_adr_folder_transition.place(x=16, y=46)
    input_adr_folder_transition.insert(0, text_transition)

    Frame(frm,width=370, height=2, bg="black").place(x=15, y=68)

    # Destination

    label_destination = Label(frm, text="Endereço da pasta de Destino", bg="white", font=('Tahoma', 11, "bold"))
    label_destination.place(x=15, y=98)

    input_adr_folder_destination = Entry(frm, width=52, fg="black", border=0, bg="white", font=("Tahoma", 9,))
    input_adr_folder_destination.insert(0, text_destination)
    input_adr_folder_destination.place(x=15, y=129)

    Frame(frm,width=370, height=2, bg="black").place(x=15, y=151)

    # BNT

    bnt_save = Button(frm, text="Salvar Endereços", command=lambda: dtb.save_src(input_adr_folder_transition.get(), input_adr_folder_destination.get()), pady=10, padx=10, border=1, bg="#17a2b8", fg="white", font=("Tahoma",9, "bold"))
    bnt_save.place(x=15, y=181)

    bnt_action = Button(frm, text="Distribuir", command=lambda: dtb.distribute_files(), pady=10, padx=30, border=1, bg="#28a745", fg="white", font=("Tahoma",9, "bold"))
    bnt_action.place(x=260, y=181)

    bnt_rename = Button(frm, text="Renomear", command=lambda: dtb.rename(), pady=10, padx=30, border=1, bg="#17a2b8", fg="white", font=("Tahoma",9, "bold"))
    bnt_rename.place(x=15, y=231)

    window.mainloop()


if __name__ == "__main__":
    dtb = File_distributor()

    text_transition = "Escreva o endereço da pasta de Transição" if dtb.from_folder == "" else dtb.from_folder
    text_destination = "Escreva o endereço da pasta de Destino" if dtb.to_folder == "" else dtb.to_folder

    app_interface()



