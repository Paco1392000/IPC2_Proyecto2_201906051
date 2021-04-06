from tkinter import filedialog, font, Label, Text, Frame, StringVar, ttk
from xml.dom import minidom
from tkinter import *
import tkinter as tk
import webbrowser
import datetime
import time
import os
#--------------------XXXXXXXXXXXXXX---XXXXX------XXXXX---XXXXXXXXXX-------XXXXX---XXXXXXXXXXXXXXXX------------------
#--------------------XXXXXXXXXXXXXX---XXXXX------XXXXX---XXXXXXXXXX-------XXXXX---XXXXXXXXXXXXXXXX------------------
#--------------------XXXXX------------XXXXX------XXXXX---XXXXXXXXXXXX-----XXXXX---XXXXX------XXXXX------------------
#--------------------XXXXX------------XXXXX------XXXXX---XXXXX--XXXXX-----XXXXX---XXXXX------XXXXX------------------
#--------------------XXXXXXXXXXXXXX---XXXXX------XXXXX---XXXXX----XXXXX---XXXXX---XXXXX-----------------------------
#--------------------XXXXXXXXXXXXXX---XXXXX------XXXXX---XXXXX-----XXXXX--XXXXX---XXXXX------XXXXX------------------
#--------------------XXXXX------------XXXXX------XXXXX---XXXXX-----XXXXXXXXXXXX---XXXXX------XXXXX------------------
#--------------------XXXXX------------XXXXXXXXXXXXXXXX---XXXXX-------XXXXXXXXXX---XXXXXXXXXXXXXXXX------------------
#--------------------XXXXX------------XXXXXXXXXXXXXXXX---XXXXX-------XXXXXXXXXX---XXXXXXXXXXXXXXXX------------------
#Lista que obtendra los datos
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

#---------------------------------XXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXX--------------------
#---------------------------------XXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXXXXXXXXXXXXXXXX--------------------
#---------------------------------XXXXXXXXXXXXXXXXXXXXXXX--------------------XXXXX---------XXXXX--------------------
#---------------------------------XXXXX----XXXXX----XXXXX---XXXXXXXXXXXXXX---XXXXX---------XXXXX--------------------
#---------------------------------XXXXX----XXXXX----XXXXX---XXXXXXXXXXXXXX---XXXXX---------XXXXX--------------------
#---------------------------------XXXXX----XXXXX----XXXXX---XXXXXXXXXXXXXX---XXXXX---------XXXXX--------------------
#---------------------------------XXXXX----XXXXX----XXXXX--------------------XXXXX---------XXXXX--------------------
#---------------------------------XXXXX----XXXXX----XXXXX--------------------XXXXXXXXXXXXXXXXXXX--------------------
#---------------------------------XXXXX----XXXXX----XXXXX--------------------XXXXXXXXXXXXXXXXXXX--------------------
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

class Matriz_Ortogonal(object):
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

#-----------------------------XXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXX---XXXXX--XXXXXXX--------------------------------------------
#-----------------------------XXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXX---XXXXXXXXXXXXXXXX------------------------------------------
#-----------------------------XXXXX-----XXXXXXX----------XXXXX---------XXXXXXXX---XXXXXX-----------------------------------------
#-----------------------------XXXXX-------XXXXXX---------XXXXX---------XXXXXXX-----XXXXX-----------------------------------------
#-----------------------------XXXXX---------XXXX---------XXXXX---------XXXXXX----------------------------------------------------
#-----------------------------XXXXX-------XXXXXX---------XXXXX---------XXXXX-----------------------------------------------------
#-----------------------------XXXXX-----XXXXXXX----------XXXXX---------XXXXX-----------------------------------------------------
#-----------------------------XXXXXXXXXXXXXXXX-----XXXXXXXXXXXXXXXXX---XXXXX-----------------------------------------------------
#-----------------------------XXXXXXXXXXXXXXX------XXXXXXXXXXXXXXXXX---XXXXX-----------------------------------------------------
if os.path.isdir('Desktop/C.201906051_Proyecto2/'):
    print('Confirmando Existencia del Directorio')
    time.sleep(0.8)
    print('...............................................')
    time.sleep(0.5)
    print('                                 Ruta Existente')
else:
    print('Confirmando Existencia del Directorio')
    time.sleep(0.8)
    print('...............................................')
    time.sleep(0.5)
    print('                             Creando Directorio')
    time.sleep(0.5)
    print('...............................................')
    time.sleep(0.5)
    directorio_nuevo = 'Desktop/C.201906051_Proyecto2'
    os.mkdir(directorio_nuevo)
    time.sleep(0.5)
    print('                              Directorio Creado')

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
        alto_ventana = 530
        ancho_ventana = 1100
        self.matriz = Lista()            
        self.root = Tk()
        self.seleccion_ltrs = ''
        self.acciones_a_hacer = ''
        self.matriz_modificar = ''
        x_ventana = self.root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root.title("Proyecto - 201906051 | INICIO")
        self.menubar = Menu(self.root)
        self.root.config(menu = self.menubar)
        self.root.resizable(False, False)
        self.root.geometry(posicion)
        self.root.config(bg = 'lightgray')
        self.menu_inicial = Menu(self.menubar, tearoff = 0)
        self.menu_inicial.add_command(label="Seleccionar XML", command = lambda: self.XML_OPCION())        
        self.opciones_dar = Menu(self.menubar, tearoff = 0)
        self.opciones_dar.add_command(label  ="Clear", command = lambda: self.bot_a_seleccionar(4))
        self.opciones_dar.add_command(label = "Diferencia", command = lambda: self.bot_a_seleccionar(11))
        self.opciones_dar.add_command(label = "Diferencia Simetrica", command = lambda: self.bot_a_seleccionar(12))
        self.opciones_dar.add_command(label = "Girar Horizontalmente", command = lambda: self.bot_a_seleccionar(1))
        self.opciones_dar.add_command(label = "Girar Verticalmente", command = lambda: self.bot_a_seleccionar(2))
        self.opciones_dar.add_command(label = "Inerseccion", command = lambda: self.bot_a_seleccionar(10))
        self.opciones_dar.add_command(label = "Linea Horizontal", command = lambda: self.bot_a_seleccionar(5))
        self.opciones_dar.add_command(label = "Linea Vertical", command = lambda: self.bot_a_seleccionar(6))
        self.opciones_dar.add_command(label = "Rectangulo", command = lambda: self.bot_a_seleccionar(7))
        self.opciones_dar.add_command(label = "Transpuesta", command = lambda: self.bot_a_seleccionar(3))
        self.opciones_dar.add_command(label = "Triangulo Rectangulo", command = lambda: self.bot_a_seleccionar(8))
        self.opciones_dar.add_command(label = "Union", command = lambda: self.bot_a_seleccionar(9))
        self.documentacion_html = Menu(self.menubar, tearoff = 0)
        self.documentacion_html.add_command(label = "Generar HTML", command = lambda: self.creacion_html())
        self.menu_ayuda = Menu(self.menubar, tearoff = 0)
        self.menu_ayuda.add_command(label="Documentacion", command = lambda: self.pdfandpdf())
        self.menu_ayuda.add_command(label="Desarrollador", command = lambda: self.desarrollador())
        self.menubar.add_cascade(label = "Cargar", menu = self.menu_inicial)
        self.menubar.add_cascade(label = "Funciones", menu = self.opciones_dar)
        self.menubar.add_cascade(label = "Documentacion", menu = self.documentacion_html)
        self.menubar.add_cascade(label = "Ayuda", menu = self.menu_ayuda)
        
        
        
        self.root.mainloop()
        
        
        
        
    def desarrollador(self):
        print('Universidad de San Carlos de Guatemala')
        print('                        Facultad de Ingenieria')
        print('             Ingenieria en Ciencias & Sistemas')
        print('Introduccion a la Programacion & Computacion 2')
        print('Seccion:  -------------------------------->  D')
        print('Juan Francisco Urina Silva')
        print('201906051')
        
    def pdfandpdf(self):
        try:
            os.system('Desktop\IPC2_Proyecto2_201906051.pdf')            
        except:
            print('Error: ARCHIVO NO ENCONTRADO')

iniciar = inicio()