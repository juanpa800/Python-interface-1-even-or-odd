from tkinter import *
import main
import customtkinter

customtkinter.set_appearance_mode("") # how to look your aplication: dark?, light?
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x640")

# titulo
labelNumber = customtkinter.CTkLabel(root, text = main.lbl_title, font=("CTkFont",23) )
labelNumber.place(relx=0.5, rely=0.1, anchor=CENTER)

# label e inputs iniciales
labelNumber = customtkinter.CTkLabel(root, text = main.lbl_numberInput)
labelNumber.place(relx=0.3, rely=0.2, anchor=CENTER)

inputNumber = customtkinter.CTkEntry(root)
inputNumber.place(relx=0.7, rely=0.2, anchor=CENTER)

# botón de aceptar
submit = customtkinter.CTkButton(master=root, text="Aceptar", command=main.oddOrEven)
submit.place(relx=0.5, rely=0.3, anchor=CENTER)

# variable respuesta
_varMessage = StringVar()
labelMessage = customtkinter.CTkLabel(root, textvariable = _varMessage, font=("CTkFont",23), text_color="#406b40")
labelMessage.place(relx=0.5, rely=0.4, anchor=CENTER)


root.mainloop()
