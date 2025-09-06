import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.geometry("520x580")
ventana.title("Formulario de Registro")

# Variables
var_genero = tk.IntVar()

# Función para limpiar los campos
def borrar_valores():
    tbNombres.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

# Función para guardar los valores en un archivo TXT
def guardar_valores():
    nombres = tbNombres.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    # Determinar género
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    else:
        genero = "No especificado"

    # Crear cadena de datos
    datos = (
        f"nombres: {nombres}, apellidos: {apellidos}, edad: {edad}, "
        f"estatura: {estatura}, telefono: {telefono}, genero: {genero}"
    )

    # Guardar en archivo (modo 'a' para agregar sin sobrescribir)
    with open("302040.txt", "a", encoding="utf-8") as archivo:
        archivo.write(datos + "\n")

    # Mostrar mensaje de confirmación
    messagebox.showinfo("Información", "Datos guardados con éxito:\n\n" + datos)

    # Limpiar campos
    borrar_valores()

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombres").pack()
tbNombres = tk.Entry(ventana)
tbNombres.pack()

tk.Label(ventana, text="Apellidos").pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

tk.Label(ventana, text="Edad").pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

tk.Label(ventana, text="Estatura").pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

tk.Label(ventana, text="Teléfono").pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

tk.Label(ventana, text="Género").pack()
tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1).pack()
tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2).pack()

# Botones
tk.Button(ventana, text="Borrar valores", command=borrar_valores).pack(pady=5)
tk.Button(ventana, text="Guardar", command=guardar_valores).pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
