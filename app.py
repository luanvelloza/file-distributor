# Criar uma interface com TkWinter e concenta-la com o File_distributor
from tkinter import *

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
input_adr_folder_transition.insert(0, "Trocar por uma variavel")

Frame(frm,width=370, height=2, bg="black").place(x=15, y=68)

# Destination

label_destination = Label(frm, text="Endereço da pasta de Destino", bg="white", font=('Tahoma', 11, "bold"))
label_destination.place(x=15, y=98)

input_adr_folder_destination = Entry(frm, width=52, fg="black", border=0, bg="white", font=("Tahoma", 9,))
input_adr_folder_destination.insert(0, "Trocar por uma variavel")
input_adr_folder_destination.place(x=15, y=129)

Frame(frm,width=370, height=2, bg="black").place(x=15, y=151)

# BNT

bnt_save = Button(frm, text="Salvar Endereços", command=window.destroy, pady=7, padx=2, border=1, bg="#17a2b8", fg="white", font=("Tahoma",9, "bold"))
bnt_save.place(x=15, y=211)

bnt_action = Button(frm, text="Distribuir", command=window.destroy, pady=7, padx=30, border=1, bg="#28a745", fg="white", font=("Tahoma",9, "bold"))
bnt_action.place(x=260, y=211)

window.mainloop()



