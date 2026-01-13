# gui.py
import tkinter as tk
from tkinter import messagebox
from calculo import CalculadoraPeso
from mensajes import mensaje_imc

def calcular():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        calculadora = CalculadoraPeso(peso, altura)
        mensaje = mensaje_imc(calculadora.imc)
        messagebox.showinfo(
            "Resultado",
            f"Tu IMC es: {calculadora.imc:.2f}\n{mensaje}"
        )
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos")

def iniciar_gui():
    global entry_peso, entry_altura

    root = tk.Tk()
    root.title("Calculadora de IMC")

    tk.Label(root, text="Peso (kg):").grid(row=0, column=0, padx=5, pady=5)
    entry_peso = tk.Entry(root)
    entry_peso.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Altura (m):").grid(row=1, column=0, padx=5, pady=5)
    entry_altura = tk.Entry(root)
    entry_altura.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(root, text="Calcular IMC", command=calcular)\
        .grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()