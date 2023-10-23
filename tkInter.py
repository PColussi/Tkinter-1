from tkinter import *

def converter():
    try:
        cent = float(entrada_cm.get())
        metros = cent/100
        resultado_label.config(text=f"{cent} cm é igual a {metros} metros ")
    except ValueError:
        resultado_label.config(text="Valor inválido. Insira novamente.")


janela = Tk()

janela.title("Conversor de medidas")

janela.geometry("400x400")

label_cm = Label(janela, text="Centímetros")
label_cm.pack()

entrada_cm = Entry(janela)
entrada_cm.pack()


converter_button = Button(janela, text="Converter", command=converter, )
converter_button.pack()

resultado_label = Label(janela,text="")
resultado_label.pack()


janela.mainloop()
