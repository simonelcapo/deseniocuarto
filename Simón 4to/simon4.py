from tkinter import *
from clientes import *
from mascotas import *
from database import *
from agregar_mascotas import abrir_agregar_mascotas
from agragar_clientes import abrir_nuevos_clientes
from estilos import *

# defino la ventana principal de mi programa 
root= Tk()
root.geometry("500x700")
marco_principal = Frame(root)
menubar=Menu(root)
menubasedata=Menu(menubar, tearoff=0)
menubasedata.add_command(label="crear BBDD", command= crear_base_datos)
menubasedata.add_command(label="salir", command= lambda: root.destroy())
menubar.add_cascade(label="BBDD", menu = menubasedata)