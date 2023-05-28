import tkinter
import main
import customtkinter

customtkinter.set_appearance_mode("") # how to look your aplication: dark?, light?
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x240")

labelNumber = customtkinter.CTkLabel(root, text = main.lbl_number)
labelNumber.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)

inputNumber = customtkinter.CTkEntry(root)
inputNumber.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)

# -------------------------------------------------------------------
def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
submit = customtkinter.CTkButton(master=root, text="CTkButton", command=button_function)
submit.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


root.mainloop()
