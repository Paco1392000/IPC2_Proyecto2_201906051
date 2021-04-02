from tkinter import filedialog, ttk, font
from xml.dom import minidom
from tkinter import *
import tkinter as tk
import os
class Lista:
    def __init__(self):
        self.longitud = 0
        self.inicio_lista = None
    def devolver_valor(self, comienzo):
        tmp = self.inicio_lista
        cont = 1
        while cont < comienzo:
            cont += 1
            tmp = tmp.siguiente
        return tmp
    def agregar_valor(self, valor):
        if self.inicio_lista is None:
            self.inicio_lista = valor
            self.inicio_lista.siguiente = self.inicio_lista
            self.longitud += 1
        else:
            if self.inicio_lista.siguiente == self.inicio_lista:
                self.inicio_lista.siguiente = valor
                valor.siguiente = self.inicio_lista
                self.longitud += 1
            else:
                tmp = self.inicio_lista
                while tmp.siguiente != self.inicio_lista:
                    tmp = tmp.siguiente
                tmp.siguiente = valor
                valor.siguiente = self.inicio_lista
                self.longitud += 1
    
#Parte para la Matriz Ortogonal (nodo) -> recorre la matriz  
class Nodo(object):
    def __init__(self, dato_obtenido, fila, columna):
        print()
        self.arr = None
        self.ab = None
        self.iz = None
        self.der = None
        self.fila = fila
        self.columna = columna
        self.dato_obtenido = dato_obtenido
class Titulo(object):
    def __init__(self, cantidad):
        self.siguiente = None
        self.anterior = None
        self.ingreso = None
        self.cantidad = cantidad
#Lista para los titulos que se obtendran (encabezados)
class Objeto_Titulo(object):
    def __init__(self):
        self.longitud = 0
        self.inicio_lista = None
    #Verificamos si la lista esta vacia
    def sin_valor(self):
        if self.inicio_lista != None:
            return False
        else:
            return True
    #Retorno de la posicion
    def valor_retornar(self, po):
        tmp = self.inicio_lista
        while tmp != None:
            if tmp.po == po:
                return tmp
        return None
    #metodo para agregar valores
    def agregar_valor(self, valor):
        if self.sin_valor() == None:
            self.inicio_lista = valor
        else:
            if int(valor.cantidad) < int(self.inicio_lista.cantidad):
                valor.siguiente = self.inicio_lista
                self.inicio_lista.anterior = valor
                self.inicio_lista = valor
            else:
                tmp = self.inicio_lista
                while tmp.siguiente != None:
                    if int(valor.cantidad) < int(tmp.siguiente.cantidad):
                        valor.siguiente = tmp.siguiente
                        tmp.siguiente.anterior = valor
                        valor.anterior = tmp
                        break
                    tmp = tmp.siguiente
                if tmp.siguiente == None:
                    tmp.siguiente = valor
                    valor.anterior = tmp
                        
                        
#Donde Correra el programa         
#Donde Correra el programa         
#Donde Correra el programa         
#Donde Correra el programa         
#Donde Correra el programa         
class inicio():
    def __init__(self):
        self.seleccion = None
        self.matriz = Lista()
        self.pestana = Tk()
        self.pestana.title('Proyecto')
        self.opc = Menu(self.pestana)
        self.pestana.config(menu = self.opc)
        self.cargando_menu = Menu(self.opc, tearoff = 0)
        
        self.pestana.mainloop()
        
        
iniciar = inicio()