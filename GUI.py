import tkinter
import main
import customtkinter

customtkinter.set_appearance_mode("") # how to look your aplication: dark?, light?
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x640")

# titulo
labelNumber = customtkinter.CTkLabel(root, text = main.lbl_title, font=("CTkFont",23) )
labelNumber.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

labelNumber = customtkinter.CTkLabel(root, text = main.lbl_numberInput)
labelNumber.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)

inputNumber = customtkinter.CTkEntry(root)
inputNumber.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)

# Use CTkButton instead of tkinter Button
submit = customtkinter.CTkButton(master=root, text="Aceptar", command=main.oddOrEven)
submit.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


root.mainloop()
