import GUI

# Variables
lbl_title = "¿Número par o impar?"
lbl_numberInput = "Indique un número: "

# Funciones
def oddOrEven():
    number = int(GUI.inputNumber.get())
    if number%2 == 0:
        message = "El número es par"
    else:
        message = "El número es impar"
    print(number, message)

# función main e invocación
def main():
    GUI()

if __name__ == "__main__":
    main()