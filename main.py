from tkinter import filedialog, font, Label, Text, Frame, StringVar, ttk
from xml.dom import minidom
from webbrowser import *
from tkinter import *
import tkinter as tk
import datetime
import os
#Lista que obtendra los datos
#--------------------XXXXXXXXXXXXXX---XXXXX------XXXXX---XXXXXXXXXX-------XXXXX---XXXXXXXXXXXXXXXX------------------
#--------------------XXXXXXXXXXXXXX---XXXXX------XXXXX---XXXXXXXXXX-------XXXXX---XXXXXXXXXXXXXXXX------------------
#--------------------XXXXX------------XXXXX------XXXXX---XXXXXXXXXXXX-----XXXXX---XXXXX------XXXXX------------------
#--------------------XXXXX------------XXXXX------XXXXX---XXXXX--XXXXX-----XXXXX---XXXXX------XXXXX------------------
#--------------------XXXXXXXXXXXXXX---XXXXX------XXXXX---XXXXX----XXXXX---XXXXX---XXXXX-----------------------------
#--------------------XXXXXXXXXXXXXX---XXXXX------XXXXX---XXXXX-----XXXXX--XXXXX---XXXXX------XXXXX------------------
#--------------------XXXXX------------XXXXX------XXXXX---XXXXX-----XXXXXXXXXXXX---XXXXX------XXXXX------------------
#--------------------XXXXX------------XXXXXXXXXXXXXXXX---XXXXX-------XXXXXXXXXX---XXXXXXXXXXXXXXXX------------------
#--------------------XXXXX------------XXXXXXXXXXXXXXXX---XXXXX-------XXXXXXXXXX---XXXXXXXXXXXXXXXX------------------
class Lista:
    def __init__(self):
        self.inicio = None  
        self.longitud = 0
    
    def devolver_valor(self, empezar):
        tmp = self.inicio
        cont = 1
        while cont < empezar:
            cont += 1
            tmp = tmp.siguiente
        return tmp      

    def nodo_a_mostrar(self):
        tmp = self.inicio
        largo = 0
        while largo < self.longitud:
            largo += 1
            tmp = tmp.siguiente
    
    def limpiar_lista(self):
        self.inicio = None
    
    def lista_vacia(self):
        vacia = True
        if self.longitud == 0:
            return vacia
        else:
            vacia = False
            return False     
    
    def agregar_valor(self, nuevo):        
        if self.inicio is None:
            self.inicio = nuevo
            self.inicio.siguiente = self.inicio
            self.longitud += 1
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.longitud += 1
            else:
                tmp = self.inicio            
                while tmp.siguiente != self.inicio:
                    tmp = tmp.siguiente
                tmp.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.longitud+=1

#Parte para la Matriz Ortogonal (nodo) -> recorre la matriz  
class Nodo(object):
    def __init__(self, dato, fila, columna):
        self.pos_left = None
        self.pos_right = None
        self.pos_down = None
        self.pos_up = None
        self.dato = dato
        self.fila = fila
        self.columna = columna

class Titulo(object):
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None
        self.anterior = None
        self.ingreso = None

class Objeto_Titulo(object):
    def __init__(self):
        self.inicio = None
        self.longitud = 0

    def agregar_valor(self, nuevo):    
        if self.lista_vacia() == True:
            self.inicio = nuevo
        else:
            if int(nuevo.numero) < int(self.inicio.numero):
                nuevo.siguiente = self.inicio
                self.inicio.anterior = nuevo
                self.inicio = nuevo
            else:
                tmp = self.inicio
                while tmp.siguiente != None:
                    if int(nuevo.numero) < int(tmp.siguiente.numero):
                        nuevo.siguiente = tmp.siguiente
                        tmp.siguiente.anterior = nuevo
                        nuevo.anterior = tmp
                        break
                    tmp = tmp.siguiente
                if tmp.siguiente == None:
                    tmp.siguiente = nuevo
                    nuevo.anterior = tmp
                
    
    def devolver_valor(self, numero):
        tmp = self.inicio        
        while tmp != None:
            if tmp.numero == numero:
                return tmp
            tmp = tmp.siguiente
        return None
    
    def lista_vacia(self):
        if self.inicio == None:
            return True
        else:
            return False

class Matriz(object):
    def __init__(self, val_in, filas, columnas):
        self.siguiente = None
        self.filas = filas
        self.val_in = val_in
        self.columnas = columnas
        self.titulo_fila_s = Objeto_Titulo()
        self.titulo_columna_s = Objeto_Titulo()

    
    def agregar_valor(self, dato, fila, columna):
        nuevo = Nodo(dato, fila, columna)
        titulo_fila = self.titulo_fila_s.devolver_valor(fila)
        if titulo_fila == None:
            titulo_fila = Titulo(fila)
            titulo_fila.ingreso = nuevo
            self.titulo_fila_s.agregar_valor(titulo_fila)            
        else:
            if int(nuevo.columna) < int(titulo_fila.ingreso.columna):
                nuevo.pos_right = titulo_fila.ingreso
                titulo_fila.ingreso.pos_left = nuevo
                titulo_fila.ingreso = nuevo
            else:
                tmp = titulo_fila.ingreso
                while tmp.pos_right !=None:
                    if int(nuevo.columna) < int(tmp.pos_right.columna):
                        nuevo.pos_right = tmp.pos_right
                        tmp.pos_right.pos_left = nuevo
                        nuevo.pos_left = tmp
                        tmp.pos_right = nuevo
                        break
                    tmp = tmp.pos_right
                if tmp.pos_right == None:
                    tmp.pos_right = nuevo
                    nuevo.pos_left = tmp
        titulo_columna = self.titulo_columna_s.devolver_valor(columna)
        if titulo_columna == None:
            titulo_columna = Titulo(columna)
            self.titulo_columna_s.agregar_valor(titulo_columna)
            titulo_columna.ingreso = nuevo
        else: 
            if int(nuevo.fila) < int(titulo_columna.ingreso.fila):
                nuevo.pos_down = titulo_columna.ingreso
                titulo_columna.ingreso.pos_up = nuevo
                titulo_columna.ingreso = nuevo
            else:
                tmp = titulo_columna.ingreso
                while tmp.pos_down != None:
                    if int(nuevo.fila) < int(tmp.pos_down.fila):
                        nuevo.pos_down = tmp.pos_down
                        tmp.pos_down.pos_up = nuevo
                        nuevo.pos_up = tmp
                        tmp.pos_down = nuevo
                        break
                    tmp = tmp.pos_down
                if tmp.pos_down == None:
                    tmp.pos_down = nuevo
                    nuevo.pos_up = tmp
                    
    def obtener_fila(self):
        titulo_fila = self.titulo_fila_s.inicio
        while(titulo_fila != None):
            tmp = titulo_fila.ingreso
            while(tmp != None):
                tmp = tmp.pos_right
            titulo_fila = titulo_fila.siguiente
    
    def obtener_columna(self):
        titulo_columna = self.titulo_columna_s.inicio
        
        while titulo_columna != None:
            tmp = titulo_columna.ingreso
            while tmp != None:
                tmp = tmp.pos_right
            titulo_columna = titulo_columna.siguiente
    
    def obtener_nodo(self, fila, columna):
        titulo_fila = self.titulo_fila_s.inicio
        while(titulo_fila != None):
            tmp = titulo_fila.ingreso
            while tmp != None:
                if tmp.fila == fila and tmp.columna == columna:
                    return tmp
                tmp = tmp.pos_right
            titulo_fila = titulo_fila.siguiente

#---------------------XXXXXXXXXXXXXX---XXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---------------------------------
#---------------------XXXXXXXXXXXXXX---XXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---------------------------------
#---------------------XXXX-------XXX---XXX--------XXX---XXX-----------XXX---XXX--------------------------------------------------
#---------------------XXXX-------XXX---XXX--------XXX---XXX-----------XXX---XXX--------------------------------------------------
#---------------------XXXXXXXXXXXXXX---XXXXXXXXXXXXXX---XXX-----------XXX---XXX----XXXXXXXXXXXXX---------------------------------
#---------------------XXXXXXXXXXXXXX---XXXXXXXXXXXXXX---XXX-----------XXX---XXX----XXXXXXXXXXXXX---------------------------------
#---------------------XXXX-------------XXX----XXX-------XXX-----------XXX---XXX----XXX-------XXX---------------------------------
#---------------------XXXX-------------XXX------XXX-----XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---------------------------------
#---------------------XXXX-------------XXX--------XXX---XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXXXXXX---------------------------------    
class inicio():
    def __init__(self):
        self.matriz_modificar = ''
        self.acciones_a_hacer = ''
        self.seleccion_ltrs = ''
        self.matriz = Lista()            

        self.root = Tk()
        ancho_ventana = 1100
        alto_ventana = 530
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root.title("Proyecto")
        self.menubar = Menu(self.root)
        
        self.root.config(menu = self.menubar)
        self.root.resizable(False, False)
        self.root.geometry(posicion)
        self.root.config(bg = 'lightgray')
        self.menu_inicial = Menu(self.menubar, tearoff = 0)
        self.menu_inicial.add_command(label="Seleccionar XML", command = lambda: self.XML_OPCION())
        
        
        
        self.root.mainloop()
        

iniciar = inicio()