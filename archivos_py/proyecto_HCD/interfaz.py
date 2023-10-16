import tkinter as tk

#?Aqui puedo poner la funcion:

def calcular_imc():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())

    imc = peso / (altura ** 2)

    if 0 < imc < 18.5:
        resultado.config(text=f"Su IMC es: {imc:.2f}, Usted esta en infrapeso")

    elif 18.5 <= imc <= 24.9:
        resultado.config(text=f"Su IMC es: {imc:.2f}, Usted esta en su peso ideal")

    elif 18.5 <= imc <= 24.9:
        resultado.config(text=f"Su IMC es: {imc:.2f}, Usted esta en sobrepeso")

    else:
        resultado.config(text=f"Su IMC es: {imc:.2f}, Usted tiene obesidad")
# Crear la ventana:

ventana = tk.Tk()
ventana.title("Calculadora de IMC")

# Etiquetas
label_peso = tk.Label(ventana, text="Peso (kg):")
label_altura = tk.Label(ventana, text="Altura (m):")
resultado = tk.Label(ventana, text="")

# Campos de entrada
entry_peso = tk.Entry(ventana)
entry_altura = tk.Entry(ventana)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular IMC", command=calcular_imc)

# Diseño de la interfaz
label_peso.pack()
entry_peso.pack()
label_altura.pack()
entry_altura.pack()
boton_calcular.pack()
resultado.pack()

# Iniciar la ventana
ventana.mainloop()
