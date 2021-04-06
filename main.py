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
        self.opciones_bot = Frame(self.root, borderwidth = 8, relief = 'groove')
        self.opciones_bot.place(x = 0, y = 0, width = 1100, height = 45)      
        self.inicial_a = Frame(self.root, borderwidth = 8, relief = 'sunken', bg="white")
        self.inicial_a.place(x = 15 , y = 55, width = 350, height = 350)
        self.primer_label = Label(text = 'Matriz "A"')
        self.primer_label.configure({'backgroun':'lightgray'})
        self.primer_label.config(justify = 'center', fg = 'blue', font = ('Arial', 15))
        self.primer_label.place(x = 140, y = 420)
        self.secundario_b = Frame(self.root, borderwidth = 8, relief = 'sunken', bg="white")
        self.secundario_b.place(x = 735 , y = 55, width = 350, height = 350)
        self.segundo_label = Label(text = 'Matriz "B"')
        self.segundo_label.configure({'backgroun':'lightgray'})
        self.segundo_label.config(justify = 'center', fg = 'blue', font = ('Arial', 15))
        self.segundo_label.place(x = 880, y = 420)
        self.tercer_c = Frame(self.root, borderwidth = 8, relief = 'sunken', bg="gray")
        self.tercer_c.place(x = 375 , y = 175, width = 350, height = 350)
        self.segundo_label = Label(text = 'Resultado')
        self.segundo_label.configure({'backgroun':'lightgray'})
        self.segundo_label.config(justify = 'center', fg = '#6495ED', font = ('Arial', 15))
        self.segundo_label.place(x = 510, y = 130)
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
        self.root.mainloop()
    
    def herramientas_p(self):
        mat_dar = []
        self.nuevo_bot()
        self.clear_f()
        self.opc_da = Label(self.opciones_bot, text = 'Opciones')
        self.opc_da.grid(padx = 5, row = 0, column = 0)
        for a in range(self.matriz.longitud):
            mat_dar.append(str(self.matriz.devolver_valor(a + 1).val_in))
        self.most_mtrs = ttk.Combobox(self.opciones_bot, values = mat_dar)
        self.most_mtrs.set(mat_dar[0])
        self.most_mtrs.grid(padx = 4, row = 0, column = 1)
        self.opc_da2 = Label(self.opciones_bot, text = 'Seleccionar')
        self.opc_da2.grid(padx = 4, row = 0, column = 2)
        self.most_mtrs2 = ttk.Combobox(self.opciones_bot, values = mat_dar)
        self.most_mtrs2.set(mat_dar[1])
        self.most_mtrs2.grid(padx = 4, row = 0, column = 3)
        self.most_rst = Button(self.opciones_bot, text = 'Mostrar', command = lambda: self.resultado_mostrar(), bg = 'lightgray')
        self.most_rst.grid(padx = 4, row = 0, column = 4)

    def herramientas_de_graficar_a(self):
        mat_dar = []
        self.nuevo_bot()
        self.opc_da = Label(self.opciones_bot, text = 'Opciones')
        self.opc_da.grid(padx = 5,row = 0, column = 0)
        for a in range(self.matriz.longitud):
            mat_dar.append(str(self.matriz.devolver_valor(a + 1).val_in))
        self.most_mtrs = ttk.Combobox(self.opciones_bot, values = mat_dar)
        self.most_mtrs.set(mat_dar[0])
        self.most_mtrs.grid(padx = 4, row = 0, column = 1)
        self.most_rst = Button(self.opciones_bot, text = 'Mostrar', command = lambda: self.resultado_mostrar(), bg = 'lightgray')
        self.most_rst.grid(padx=5, row = 0, column = 2)

    def herramientas_agregar_linea(self):
        self.labelFila = Label(self.opciones_bot, text = 'Fila')
        self.labelFila.grid(padx = 4, row = 0, column = 2)
        self.filaEntry = Entry(self.opciones_bot, width = 2)
        self.filaEntry.grid(padx = 3, row = 0, column = 3 )
        self.labelColumna = Label(self.opciones_bot, text = 'Columna')
        self.labelColumna.grid(padx = 4, row = 0, column = 4)
        self.columnaEntry = Entry(self.opciones_bot, width = 2)
        self.columnaEntry.grid(padx = 3, row = 0, column = 5 )
        self.labelCa = Label(self.opciones_bot, text = 'Longitud')
        self.labelCa.grid(padx = 4, row = 0, column = 6)
        self.cantidadEntry = Entry(self.opciones_bot, width = 2)
        self.cantidadEntry.grid(padx = 3, row = 0, column = 7 )
        self.most_rst = Button(self.opciones_bot, text = 'Mostrar', command = lambda: self.resultado_mostrar(), bg = 'lightgray')
        self.most_rst.grid(padx = 4, row = 0, column = 8)

    def herramientas_de_graficar_b(self):
        mat_dar = []
        self.nuevo_bot()  
        self.opc_da = Label(self.opciones_bot, text = 'Opciones')
        self.opc_da.grid(padx = 5,row = 0, column = 0)
        for a in range(self.matriz.longitud):
            mat_dar.append(str(self.matriz.devolver_valor(a + 1).val_in))
        self.most_mtrs = ttk.Combobox(self.opciones_bot, values = mat_dar)
        self.most_mtrs.set(mat_dar[0])
        self.most_mtrs.grid(padx = 5, row = 0, column = 1)
        if self.seleccion_ltrs == 'area_limpiar':            
            self.coordenanda1 = Label(self.opciones_bot, text = 'Inicio')
            self.coordenanda1.grid(padx = 4, row = 0, column = 2)
            self.x_1_A = Entry(self.opciones_bot, width = 2)
            self.x_1_A.grid(padx = 3, row = 0, column = 3 )
            self.y_1_A = Entry(self.opciones_bot, width = 2)
            self.y_1_A.grid(padx = 4, row = 0, column = 4 )
            self.coordenanda2 = Label(self.opciones_bot, text = 'Fin')
            self.coordenanda2.grid(padx= 5, row = 0, column = 5)
            self.x_1_B = Entry(self.opciones_bot, width = 2)
            self.x_1_B.grid(padx = 3, row =0, column = 6 )
            self.y_1_B = Entry(self.opciones_bot, width = 2)
            self.y_1_B.grid(padx = 4, row =0, column = 7 )            
            self.most_rst = Button(self.opciones_bot, text = 'Mostrar', command = lambda: self.resultado_mostrar(), bg = 'lightgray')
            self.most_rst.grid(padx = 4, row = 0, column = 8)
        if self.seleccion_ltrs == 'horiz_li':
            self.herramientas_agregar_linea()
        if self.seleccion_ltrs == 'vert_li':
            self.herramientas_agregar_linea()
        if self.seleccion_ltrs == 'ag_rec':
            #------------------------------------------------------
            #------------------------------------------------------
            self.coordenanda1 = Label(self.opciones_bot, text = '"X"')
            self.coordenanda1.grid(padx = 5, row = 0, column = 2)
            self.x_1_A = Entry(self.opciones_bot, width = 2)
            #***********************************************
            self.x_1_A.grid(padx = 3, row = 0, column = 3)
            #------------------------------------------------------
            #------------------------------------------------------
            self.coordenanda1_b2 = Label(self.opciones_bot, text = '"Y"')
            self.coordenanda1_b2.grid(padx = 5, row = 0, column = 4)
            self.y_1_A = Entry(self.opciones_bot, width = 2)
            #***********************************************
            self.y_1_A.grid(padx = 6, row = 0, column = 5)
            #------------------------------------------------------
            #------------------------------------------------------
            self.anchura = Label(self.opciones_bot, text = 'Ancho')
            self.anchura.grid(padx = 5, row = 0, column = 7)
            self.entrada_ancho = Entry(self.opciones_bot, width = 2)
            self.entrada_ancho.grid(padx = 3, row = 0, column = 8)
            #------------------------------------------------------
            self.altitud = Label(self.opciones_bot, text = 'Alto')
            self.altitud.grid(padx = 5, row = 0, column = 10)
            self.entrada_dar = Entry(self.opciones_bot, width = 2)
            self.entrada_dar.grid(padx = 3, row = 0, column = 11)
            #------------------------------------------------------
            self.most_rst = Button(self.opciones_bot, text = 'Mostrar', command = lambda: self.resultado_mostrar(), bg = 'lightgray')
            self.most_rst.grid(padx = 5, row = 0, column = 17)
        if self.seleccion_ltrs == 'ag_triangulo':
            self.coordenanda1 = Label(self.opciones_bot, text = 'Inicio')
            self.coordenanda1.grid(padx = 5, row = 0, column = 2)
            self.x_1_A = Entry(self.opciones_bot, width = 2)
            self.x_1_A.grid(padx = 3, row = 0, column = 3)
            self.y_1_A = Entry(self.opciones_bot, width = 2)
            self.y_1_A.grid(padx = 5, row = 0, column = 4)
            self.fls_cls = Label(self.opciones_bot, text = 'Ancho x Alto')
            self.fls_cls.grid(padx = 5, row = 0, column = 5)
            self.datoentry = Entry(self.opciones_bot, width = 2)
            self.datoentry.grid(padx = 3, row = 0, column = 6)
            self.most_rst = Button(self.opciones_bot, text = 'Mostrar', command = lambda: self.resultado_mostrar(), bg = 'lightgray')
            self.most_rst.grid(padx = 5, row = 0, column = 7)

    def desarrollador(self):
        print('Universidad de San Carlos de Guatemala')
        print('                        Facultad de Ingenieria')
        print('             Ingenieria en Ciencias & Sistemas')
        print('Introduccion a la Programacion & Computacion 2')
        print('Seccion:  -------------------------------->  D')
        print('Juan Francisco Urina Silva')
        print('201906051')

    def bot_a_seleccionar(self, valor):
        if valor == 1:
            self.nuevo_bot()
            self.clear_f()          
            self.herramientas_de_graficar_a()
            self.root.title("Proyecto - 201906051 | Giro Horizontal")
            self.seleccion_ltrs = 'horizontal'
        if valor == 2:
            self.nuevo_bot()
            self.clear_f()
            self.herramientas_de_graficar_a()
            self.root.title("Proyecto - 201906051 | Giro Vertical")
            self.seleccion_ltrs = 'vertical'
        if valor == 3:
            self.nuevo_bot()
            self.clear_f()
            self.herramientas_de_graficar_a()
            self.root.title("Proyecto - 201906051 | Transpuesta")
            self.seleccion_ltrs = 'transpuesta'
        if valor == 4:
            self.nuevo_bot()
            self.clear_f()
            self.root.title("Proyecto - 201906051 | Limpiar Area (Trabajo)")
            self.seleccion_ltrs = 'area_limpiar'
            self.herramientas_de_graficar_b()
        if valor == 5:
            self.nuevo_bot()
            self.clear_f()
            self.root.title("Proyecto - 201906051 | Linea Horizontal")
            self.seleccion_ltrs = 'horiz_li'
            self.herramientas_de_graficar_b()
        if valor == 6:
            self.nuevo_bot()
            self.clear_f()
            self.root.title("Proyecto - 201906051 | Linea Vertical")
            self.seleccion_ltrs = 'vert_li'
            self.herramientas_de_graficar_b()
        if valor == 7:
            self.clear_f()
            self.nuevo_bot()
            self.root.title("Proyecto - 201906051 | Rectangulo")
            self.seleccion_ltrs = 'ag_rec'
            self.herramientas_de_graficar_b()
        if valor == 8:            
            self.nuevo_bot()
            self.clear_f()
            self.root.title("Proyecto - 201906051 | Triangulo Rectangulo")
            self.seleccion_ltrs = 'ag_triangulo'
            self.herramientas_de_graficar_b()
        if valor == 9:        
            self.nuevo_bot()
            self.clear_f()
            self.root.title("Proyecto - 201906051 | Union")
            self.seleccion_ltrs = 'union_m'
            self.herramientas_p()
        if valor == 10:     
            self.nuevo_bot()
            self.clear_f()
            self.root.title("Proyecto - 201906051 | Interseccion")
            self.seleccion_ltrs = 'interseccion_m'
            self.herramientas_p()
        if valor == 11:
            self.nuevo_bot()
            self.clear_f()
            self.root.title("Proyecto - 201906051 | Diferencia")
            self.seleccion_ltrs = 'dife_m'
            self.herramientas_p()
        if valor == 12:
            self.nuevo_bot()
            self.clear_f()
            self.root.title("Proyecto - 201906051 | Diferencia Simetrica")
            self.seleccion_ltrs = 'mtz_sim'
            self.herramientas_p()
                
    def resultado_mostrar(self):
        if self.seleccion_ltrs =='horizontal':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            self.vlt_horiz(mtrs_nom)
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")
            dsk = '-'
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Giro Horizontal</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td></td></tr>\n'
        if self.seleccion_ltrs == 'vertical':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            self.vlt_vert(mtrs_nom)
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")
            dsk = '-'
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Giro Vertical</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td></td></tr>\n'
        if self.seleccion_ltrs == 'transpuesta':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            self.tranponer_matriz(mtrs_nom)
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")
            dsk = '-'
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Transpuesta</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td></td></tr>\n'
        if self.seleccion_ltrs == 'area_limpiar':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            dsk = '-'
            if self.x_1_A.get().isdigit() and self.y_1_A.get().isdigit() and self.x_1_B.get().isdigit() and self.y_1_B.get().isdigit():
                dsk = self.agregar_nuevo(mtrs_nom,int(self.x_1_A.get()), int(self.y_1_A.get()),int(self.x_1_B.get()), int(self.y_1_B.get()))
            else:
                dsk = 'Error'
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")            
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Borrado</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td></td></tr>\n'
        if self.seleccion_ltrs == 'horiz_li':
            self.clear_f()            
            mtrs_nom = self.most_mtrs.get()
            dsk = '-'
            if self.filaEntry.get().isdigit() and self.columnaEntry.get() and self.cantidadEntry.get().isdigit():
                dsk = self.agregar_nuevo(mtrs_nom,int(self.filaEntry.get()), int(self.columnaEntry.get()),int(self.filaEntry.get()), int(self.columnaEntry.get())+int(self.cantidadEntry.get())-1)
            else:
                dsk = 'Error'
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")            
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Linea Vertical</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td></td></tr>\n'
        if self.seleccion_ltrs == 'vert_li':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            dsk = '-'
            if self.filaEntry.get().isdigit() and self.columnaEntry.get() and self.cantidadEntry.get().isdigit():
                dsk = self.agregar_nuevo(mtrs_nom,int(self.filaEntry.get()), int(self.columnaEntry.get()),int(self.filaEntry.get())+int(self.cantidadEntry.get())-1, int(self.columnaEntry.get()))
            else:
                dsk = 'Error'
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")            
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Linea Horizontal</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td></td></tr>\n'
        if self.seleccion_ltrs =='ag_rec':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()            
            dsk = '-'
            if self.x_1_A.get().isdigit() and self.y_1_A.get().isdigit() and self.entrada_ancho.get().isdigit() and self.entrada_dar.get().isdigit():
                dsk = self.agregar_rectangulo(mtrs_nom,int(self.x_1_A.get()), int(self.y_1_A.get()), int(self.x_1_A.get()) + int(self.entrada_dar.get())-1, int(self.y_1_A.get()) + int(self.entrada_ancho.get())-1)
            else:
                dsk = 'Error'
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")            
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Rectangulo</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td></td></tr>\n'
        if self.seleccion_ltrs =='ag_triangulo':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()            
            dsk = '-'
            if self.x_1_A.get().isdigit() and self.y_1_A.get().isdigit() and self.datoentry.get().isdigit():
                self.agregar_triangulo_rectangulo(mtrs_nom,int(self.x_1_A.get()), int(self.y_1_A.get()), int(self.x_1_A.get()) + int(self.datoentry.get()) -1, int(self.y_1_A.get()) + int(self.datoentry.get()) -1, int(self.datoentry.get()))
            else:
                dsk = 'Error'
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")            
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Triangulo Rectangulo</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td></td></tr>\n'
        if self.seleccion_ltrs =='union_m':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            mtrs_nom2 = self.most_mtrs2.get()
            self.unir_matrices(mtrs_nom, mtrs_nom2)
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")
            dsk = '-'
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Union</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td><h3 class="codatos">'+mtrs_nom2+'</h3></td></tr>\n'
        if self.seleccion_ltrs =='interseccion_m':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            mtrs_nom2 = self.most_mtrs2.get()
            self.matriz_interseccion(mtrs_nom, mtrs_nom2)
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")
            dsk = '-'
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Interseccion</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td><h3 class="codatos">'+mtrs_nom2+'</h3></td></tr>\n'
        if self.seleccion_ltrs =='dife_m':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            mtrs_nom2 = self.most_mtrs2.get()
            self.diferenciar_matrices(mtrs_nom, mtrs_nom2)
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")
            dsk = '-'
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Diferencia</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td><h3 class="codatos">'+mtrs_nom2+'</h3></td></tr>\n'
        if self.seleccion_ltrs =='mtz_sim':
            self.clear_f()
            mtrs_nom = self.most_mtrs.get()
            mtrs_nom2 = self.most_mtrs2.get()
            self.matric_diferencia_simet(mtrs_nom, mtrs_nom2)
            fecha_hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")
            dsk = '-'
            self.acciones_a_hacer +='<tr><td><h3 class="codatos">'+fecha_hora+'</h3></td><td><h3 class="codatos">'+dsk+'</h3></td><td><h3 class="codatos">Diferencia Simetrica</h3></td><td><h3 class="codatos">'+mtrs_nom+'</h3></td><td><h3 class="codatos">'+mtrs_nom2+'</h3></td></tr>\n'

    def lista_matriz(self, val_in):
        for a in range(self.matriz.longitud):
            if val_in == self.matriz.devolver_valor(a + 1).val_in:
                return self.matriz.devolver_valor(a + 1)            

    def vlt_horiz(self, valor_inicial):        
        nueva_matriz_usar = self.lista_matriz(valor_inicial)
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        for a in range(x + 1):
            for b in range(y + 1):
                card_c = Entry(self.inicial_a, width = 3)
                card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    card_c.insert(0,'A')
                    card_c.configure({'backgroun':'black'})
                    card_c.config(justify = 'center', fg = 'white')
                if a == 0 and b > 0:
                    card_c.insert(0, b)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    card_c.insert(0, a)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None:
                    card_c.insert(0,'*')
                    card_c.configure({'background': "#454545"})
                    card_c.config(justify = 'center', fg = 'white')
                valor_nuevo_c = Entry(self.tercer_c, width = 3)    
                valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    valor_nuevo_c.insert(0,'A')
                    valor_nuevo_c.configure({'backgroun':'black'})
                    valor_nuevo_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    valor_nuevo_c.insert(0, b)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    valor_nuevo_c.insert(0, a)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(x - a + 1, b) != None:
                    valor_nuevo_c.insert(0,'*')
                    valor_nuevo_c.configure({'background': "#454545"})
                    valor_nuevo_c.config(justify = 'center', fg = 'white')
                        
    def vlt_vert(self, valor_inicial):        
        nueva_matriz_usar = self.lista_matriz(valor_inicial)
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        for a in range(x + 1):
            for b in range(y + 1):
                card_c = Entry(self.inicial_a, width = 3)
                card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    card_c.insert(0,'A')
                    card_c.configure({'backgroun':'black'})
                    card_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    card_c.insert(0,b)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    card_c.insert(0, a)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None:
                    card_c.insert(0,'*')
                    card_c.configure({'background': "#454545"})
                    card_c.config(justify = 'center', fg = 'white')
                valor_nuevo_c = Entry(self.tercer_c, width = 3)    
                valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    valor_nuevo_c.insert(0,'A')
                    valor_nuevo_c.configure({'backgroun':'black'})
                    valor_nuevo_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    valor_nuevo_c.insert(0, b)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    valor_nuevo_c.insert(0,a)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, y - b + 1) != None:
                    valor_nuevo_c.insert(0,'*')
                    valor_nuevo_c.configure({'background': "#454545"})
                    valor_nuevo_c.config(justify = 'center', fg = 'white')
    
    def tranponer_matriz(self, valor_inicial):        
        nueva_matriz_usar = self.lista_matriz(valor_inicial)
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        for a in range(x + 1):
            for b in range(y + 1):
                card_c = Entry(self.inicial_a, width = 3)
                card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    card_c.insert(0,'A')
                    card_c.configure({'backgroun':'black'})
                    card_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    card_c.insert(0, b)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    card_c.insert(0, a)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None:
                    card_c.insert(0,'*')
                    card_c.configure({'background': "#454545"})
                    card_c.config(justify = 'center', fg = 'white')
        for a in range(y + 1):
            for b in range(x + 1):
                valor_nuevo_c = Entry(self.tercer_c, width = 3)    
                valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    valor_nuevo_c.insert(0,'A')
                    valor_nuevo_c.configure({'backgroun':'black'})
                    valor_nuevo_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    valor_nuevo_c.insert(0, b)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    valor_nuevo_c.insert(0, a)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(b, a) != None:
                    valor_nuevo_c.insert(0,'*')
                    valor_nuevo_c.configure({'background': "#454545"})
                    valor_nuevo_c.config(justify = 'center', fg = 'white')
    
    def agregar_nuevo(self, valor_inicial, x_1_A, y_1_A, x_1_B, y_1_B):
        nueva_matriz_usar = self.lista_matriz(valor_inicial)
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        for a in range(x + 1):
            for b in range(y + 1):
                card_c = Entry(self.inicial_a, width = 3)
                card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    card_c.insert(0,'A')
                    card_c.configure({'backgroun':'black'})
                    card_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    card_c.insert(0, b)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    card_c.insert(0, a)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None:
                    card_c.insert(0,'*')
                    card_c.configure({'background': "#454545"})
                    card_c.config(justify = 'center', fg = 'white')
        for a in range(x + 1):
            for b in range(y + 1):        
                if (x_1_A <= x and x_1_B <= x) and (y_1_A <= y and y_1_B <= y):
                    if x_1_A <= x_1_B and y_1_A <= y_1_B:    
                        valor_nuevo_c = Entry(self.tercer_c, width = 3)    
                        valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)                
                        if a == 0 and b == 0:
                            valor_nuevo_c.insert(0,'A')
                            valor_nuevo_c.configure({'backgroun':'black'})
                            valor_nuevo_c.config(justify = 'center',fg = 'white')
                        if a == 0 and b > 0:
                            valor_nuevo_c.insert(0, b)
                            valor_nuevo_c.configure({'backgroun':'white'})
                            valor_nuevo_c.config(justify = 'center',fg = 'gray')
                        if a > 0 and b == 0:
                            valor_nuevo_c.insert(0, a)
                            valor_nuevo_c.configure({'backgroun':'white'})
                            valor_nuevo_c.config(justify = 'center',fg = 'gray')
                        if nueva_matriz_usar.obtener_nodo(a, b) != None:
                            valor_nuevo_c.insert(0,'*')
                            valor_nuevo_c.configure({'background': "#454545"})
                            valor_nuevo_c.config(justify = 'center', fg = 'white')
                            #-----------------------------------agrega linea-----------------------------------
                            #-----------------------------------agrega linea-----------------------------------
                            #-----------------------------------agrega linea-----------------------------------
                            #-----------------------------------agrega linea-----------------------------------
                            if (a >= (x_1_A) and a <= (x_1_B)) and (b >= (y_1_A) and b <= (y_1_B)):
                                valor_nuevo_c.configure({'backgroun':'#454545'})
                        if (a >= (x_1_A) and a <= (x_1_B)) and (b >= (y_1_A) and b <= (y_1_B)):
                            valor_nuevo_c.configure({'backgroun':'#454545'})
                    else:
                        return 'Error: Error de Matriz'
                else:
                    return 'Error: Error Coordenadas'
        return '-'

    def agregar_rectangulo(self, valor_inicial, x_1_A, y_1_A, x_1_B, y_1_B):            
        nueva_matriz_usar = self.lista_matriz(valor_inicial)
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        for a in range(x+1):
            for b in range(y+1):
                card_c = Entry(self.inicial_a, width = 3)
                card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b ==0:
                    card_c.insert(0,'A')
                    card_c.configure({'backgroun':'black'})
                    card_c.config(justify = 'center',fg = 'white')
                if a == 0 and b>0:
                    card_c.insert(0,b)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b==0:
                    card_c.insert(0,a)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None:
                    card_c.insert(0,'*')
                    card_c.configure({'background': "#454545"})
                    card_c.config(justify = 'center', fg = 'white')
        if x_1_A>0 and x_1_B>0 and y_1_A>0 and y_1_B>0:
            for a in range(x+1):
                for b in range(y+1):
                    if (x_1_A<=x and x_1_B<=x) and (y_1_A<=y and y_1_B<=y):
                        if x_1_A<x_1_B and y_1_A<y_1_B:
                            valor_nuevo_c = Entry(self.tercer_c, width = 3)    
                            valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)                
                            if a == 0 and b ==0:
                                valor_nuevo_c.insert(0,'A')
                                valor_nuevo_c.configure({'backgroun':'black'})
                                valor_nuevo_c.config(justify = 'center',fg = 'white')
                            if a == 0 and b>0:
                                valor_nuevo_c.insert(0,b)
                                valor_nuevo_c.configure({'backgroun':'white'})
                                valor_nuevo_c.config(justify = 'center',fg = 'gray')
                            if a > 0 and b==0:
                                valor_nuevo_c.insert(0,a)
                                valor_nuevo_c.configure({'backgroun':'white'})
                                valor_nuevo_c.config(justify = 'center',fg = 'gray')
                            if nueva_matriz_usar.obtener_nodo(a, b) != None:
                                valor_nuevo_c.insert(0,'*')
                                valor_nuevo_c.configure({'background': "#454545"})
                                valor_nuevo_c.config(justify = 'center', fg = 'white')
                                if (a==(x_1_A)) and (b>=(y_1_A) and b<=(y_1_B)):
                                    valor_nuevo_c.configure({'backgroun':'#454545'})
                                if (a==(x_1_B)) and (b>=(y_1_A) and b<=(y_1_B)):
                                    valor_nuevo_c.configure({'backgroun':'#454545'})
                                if (a>=(x_1_A) and a<=(x_1_B)) and (b==(y_1_A)):
                                    valor_nuevo_c.configure({'backgroun':'#454545'})
                                if (a>=(x_1_A) and a<=(x_1_B)) and (b==(y_1_B)):
                                    valor_nuevo_c.configure({'backgroun':'#454545'})
                            if (a==(x_1_A)) and (b>=(y_1_A) and b<=(y_1_B)):
                                    valor_nuevo_c.configure({'backgroun':'#454545'})
                            if (a==(x_1_B)) and (b>=(y_1_A) and b<=(y_1_B)):
                                valor_nuevo_c.configure({'backgroun':'#454545'})
                            if (a>=(x_1_A) and a<=(x_1_B)) and (b==(y_1_A)):
                                valor_nuevo_c.configure({'backgroun':'#454545'})
                            if (a>=(x_1_A) and a<=(x_1_B)) and (b==(y_1_B)):
                                valor_nuevo_c.configure({'backgroun':'#454545'})
                        else:
                            return 'Error'
                    else:
                        return 'Error'
            return '-'
        else:
            return 'Error'
    
    def agregar_triangulo_rectangulo(self, valor_inicial, x_1_A, y_1_A, x_1_B, y_1_B, cantidad):            
        nueva_matriz_usar = self.lista_matriz(valor_inicial)
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        cont = 1
        x_col = int(y_1_A) + 1
        t_fil = int(x_1_A) + 1
        for a in range(x + 1):
            for b in range(y + 1):
                card_c = Entry(self.inicial_a, width = 3)
                card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    card_c.insert(0,'A')
                    card_c.configure({'backgroun':'black'})
                    card_c.config(justify = 'center',fg = 'white')
                if a == 0 and b>0:
                    card_c.insert(0,b)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b==0:
                    card_c.insert(0,a)
                    card_c.configure({'backgroun':'white'})
                    card_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None:
                    card_c.insert(0,'*')
                    card_c.configure({'background': "#454545"})
                    card_c.config(justify = 'center', fg = 'white')
        if x_1_A > 0 and x_1_B > 0 and y_1_A > 0 and y_1_B > 0:
            for a in range(x + 1):
                for b in range(y + 1):
                    if (x_1_A <= x and x_1_B <= x) and (y_1_A <= y and y_1_B <= y):
                        if x_1_A < x_1_B and y_1_A < y_1_B:
                            valor_nuevo_c = Entry(self.tercer_c, width = 3)    
                            valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)                
                            if a == 0 and b == 0:
                                valor_nuevo_c.insert(0,'A')
                                valor_nuevo_c.configure({'backgroun':'black'})
                                valor_nuevo_c.config(justify = 'center',fg = 'white')
                            if a == 0 and b > 0:
                                valor_nuevo_c.insert(0,b)
                                valor_nuevo_c.configure({'backgroun':'white'})
                                valor_nuevo_c.config(justify = 'center',fg = 'gray')
                            if a > 0 and b == 0:
                                valor_nuevo_c.insert(0, a)
                                valor_nuevo_c.configure({'backgroun':'white'})
                                valor_nuevo_c.config(justify = 'center',fg = 'gray')
                            if nueva_matriz_usar.obtener_nodo(a, b) != None:
                                valor_nuevo_c.insert(0,'*')
                                valor_nuevo_c.configure({'background': "#454545"})
                                valor_nuevo_c.config(justify = 'center', fg = 'white')
                                if (a == (x_1_B)) and (b >= (y_1_A) and b <= (y_1_B)):
                                    valor_nuevo_c.configure({'backgroun':'#454545'})
                                if (a >= (x_1_A) and a <= (x_1_B)) and (b == (y_1_A)):
                                    valor_nuevo_c.configure({'backgroun':'#454545'})     
                                
                                if (a > (x_1_A) and a < (x_1_B)) and (x_col == b) and (t_fil == a) and (b > (y_1_A) and b < (y_1_B)):
                                    valor_nuevo_c.configure({'backgroun':'#454545'})
                                    x_col += 1   
                                    t_fil += 1       
                            if (a == (x_1_B)) and (b >= (y_1_A) and b <= (y_1_B)):
                                valor_nuevo_c.configure({'backgroun':'#454545'})
                            if (a >= (x_1_A) and a <= (x_1_B)) and (b == (y_1_A)):
                                valor_nuevo_c.configure({'backgroun':'#454545'})                  
                            if (a > (x_1_A) and a < (x_1_B)) and (x_col == b) and (t_fil == a) and (b > (y_1_A) and b < (y_1_B)):
                                valor_nuevo_c.configure({'backgroun':'#454545'})           
                                x_col += 1      
                                t_fil += 1
                        else:
                            return 'Error'
                    else:
                        return 'Error'
            return '-'
        else:
            return 'Error'

    def unir_matrices(self, valor_inicial, valor_secundario):        
        nueva_matriz_usar = self.lista_matriz(valor_inicial)        
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        mat_s2 = self.lista_matriz(valor_secundario)
        x_a = int(mat_s2.filas)
        y_a = int(mat_s2.columnas)
        if x >= x_a:
            fila = x
        else:
            fila = x_a
        if y >= y_a:
            columna = y
        else:
            columna = y_a
        for a in range(fila+1):
            for b in range(columna+1):
                if a < x+1 and b < y+1:
                    card_c = Entry(self.inicial_a, width = 3)
                    card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                    if a == 0 and b == 0:
                        card_c.insert(0,'A')
                        card_c.configure({'backgroun':'black'})
                        card_c.config(justify = 'center',fg = 'white')
                    if a == 0 and b > 0:
                        card_c.insert(0, b)
                        card_c.configure({'backgroun':'white'})
                        card_c.config(justify = 'center',fg = 'gray')
                    if a > 0 and b == 0:
                        card_c.insert(0, a)
                        card_c.configure({'backgroun':'white'})
                        card_c.config(justify = 'center',fg = 'gray')
                    if nueva_matriz_usar.obtener_nodo(a, b) != None:
                        card_c.insert(0,'*')
                        card_c.configure({'background': "#454545"})
                        card_c.config(justify = 'center', fg = 'white')
                if a < x_a+1 and b < y_a+1:
                    car_d = Entry(self.secundario_b, width = 3)
                    car_d.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                    if a == 0 and b == 0:
                        car_d.insert(0,'A')
                        car_d.configure({'backgroun':'black'})
                        car_d.config(justify = 'center',fg = 'white')
                    if a == 0 and b > 0:
                        car_d.insert(0, b)
                        car_d.configure({'backgroun':'white'})
                        car_d.config(justify = 'center',fg = 'gray')
                    if a > 0 and b == 0:
                        car_d.insert(0, a)
                        car_d.configure({'backgroun':'white'})
                        car_d.config(justify = 'center',fg = 'gray')
                    if mat_s2.obtener_nodo(a, b) != None:
                        car_d.insert(0,'*')
                        car_d.configure({'background': "#454545"})
                        car_d.config(justify = 'center', fg = 'white')
                valor_nuevo_c = Entry(self.tercer_c, width = 3)
                valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    valor_nuevo_c.insert(0,'A')
                    valor_nuevo_c.configure({'backgroun':'black'})
                    valor_nuevo_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    valor_nuevo_c.insert(0, b)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    valor_nuevo_c.insert(0, a)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center', fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None or mat_s2.obtener_nodo(a, b) != None:
                    valor_nuevo_c.insert(0,'*')
                    valor_nuevo_c.configure({'background': "#454545"})
                    valor_nuevo_c.config(justify = 'center', fg = 'white')

    def matriz_interseccion(self, valor_inicial, valor_secundario):        
        nueva_matriz_usar = self.lista_matriz(valor_inicial)        
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        mat_s2 = self.lista_matriz(valor_secundario)
        x_a = int(mat_s2.filas)
        y_a = int(mat_s2.columnas)
        if x >= x_a:
            fila = x
        else:
            fila = x_a
        if y >= y_a:
            columna = y
        else:
            columna = y_a
        for a in range(fila + 1):
            for b in range(columna + 1):
                if a < x+1 and b < y + 1:
                    card_c = Entry(self.inicial_a, width = 3)
                    card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                    if a == 0 and b == 0:
                        card_c.insert(0,'A')
                        card_c.configure({'backgroun':'black'})
                        card_c.config(justify = 'center',fg = 'white')
                    if a == 0 and b > 0:
                        card_c.insert(0, b)
                        card_c.configure({'backgroun':'white'})
                        card_c.config(justify = 'center',fg = 'gray')
                    if a > 0 and b == 0:
                        card_c.insert(0, a)
                        card_c.configure({'backgroun':'white'})
                        card_c.config(justify = 'center',fg = 'gray')                    
                    if nueva_matriz_usar.obtener_nodo(a, b) != None:
                        card_c.insert(0,'*')
                        card_c.configure({'background': "#454545"})
                        card_c.config(justify = 'center', fg = 'white')
                if a < x_a+1 and b < y_a + 1:
                    car_d = Entry(self.secundario_b, width = 3)
                    car_d.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                    
                    if a == 0 and b == 0:
                        car_d.insert(0,'A')
                        car_d.configure({'backgroun':'black'})
                        car_d.config(justify = 'center',fg = 'white')
                    if a == 0 and b > 0:
                        car_d.insert(0, b)
                        car_d.configure({'backgroun':'white'})
                        car_d.config(justify = 'center',fg = 'gray')
                    if a > 0 and b == 0:
                        car_d.insert(0, a)
                        car_d.configure({'backgroun':'white'})
                        car_d.config(justify = 'center',fg = 'gray')
                    if mat_s2.obtener_nodo(a, b) != None:
                        car_d.insert(0,'*')
                        car_d.configure({'background': "#454545"})
                        car_d.config(justify = 'center', fg = 'white')
                valor_nuevo_c = Entry(self.tercer_c, width = 3)
                valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    valor_nuevo_c.insert(0,'A')
                    valor_nuevo_c.configure({'backgroun':'black'})
                    valor_nuevo_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    valor_nuevo_c.insert(0, b)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    valor_nuevo_c.insert(0, a)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None and mat_s2.obtener_nodo(a, b) != None:
                    valor_nuevo_c.insert(0,'*')
                    valor_nuevo_c.configure({'background': "#454545"})
                    valor_nuevo_c.config(justify = 'center', fg = 'white')
        
    def diferenciar_matrices(self, valor_inicial, valor_secundario):        
        nueva_matriz_usar = self.lista_matriz(valor_inicial)        
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        mat_s2 = self.lista_matriz(valor_secundario)
        x_a = int(mat_s2.filas)
        y_a = int(mat_s2.columnas)
        if x >= x_a:
            fila = x
        else:
            fila = x_a
        if y >= y_a:
            columna = y
        else:
            columna = y_a
        for a in range(fila + 1):
            for b in range(columna + 1):
                if a < x + 1 and b < y + 1:
                    card_c = Entry(self.inicial_a, width = 3)
                    card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                    if a == 0 and b == 0:
                        card_c.insert(0,'A')
                        card_c.configure({'backgroun':'black'})
                        card_c.config(justify = 'center', fg = 'white')
                    if a == 0 and b > 0:
                        card_c.insert(0, b)
                        card_c.configure({'backgroun':'white'})
                        card_c.config(justify = 'center', fg = 'gray')
                    if a > 0 and b == 0:
                        card_c.insert(0, a)
                        card_c.configure({'backgroun':'white'})
                        card_c.config(justify = 'center',fg = 'gray')                    
                    if nueva_matriz_usar.obtener_nodo(a, b) != None:
                        card_c.insert(0,'*')
                        card_c.configure({'background': "#454545"})
                        card_c.config(justify = 'center', fg = 'white')
                if a < x_a + 1 and b < y_a + 1:
                    car_d = Entry(self.secundario_b, width = 3)
                    car_d.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                    if a == 0 and b == 0:
                        car_d.insert(0,'A')
                        car_d.configure({'backgroun':'black'})
                        car_d.config(justify = 'center',fg = 'white')
                    if a == 0 and b > 0:
                        car_d.insert(0, b)
                        car_d.configure({'backgroun':'white'})
                        car_d.config(justify = 'center',fg = 'gray')
                    if a > 0 and b == 0:
                        car_d.insert(0, a)
                        car_d.configure({'backgroun':'white'})
                        car_d.config(justify = 'center',fg = 'gray')
                    if mat_s2.obtener_nodo(a, b) != None:
                        car_d.insert(0,'*')
                        car_d.configure({'background': "#454545"})
                        car_d.config(justify = 'center', fg = 'white')
                valor_nuevo_c = Entry(self.tercer_c, width = 3)
                valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    valor_nuevo_c.insert(0,'A')
                    valor_nuevo_c.configure({'backgroun':'black'})
                    valor_nuevo_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    valor_nuevo_c.insert(0, b)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    valor_nuevo_c.insert(0, a)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None:
                    valor_nuevo_c.insert(0,'*')
                    valor_nuevo_c.configure({'background': "#454545"})
                    valor_nuevo_c.config(justify = 'center', fg = 'white')
                    if mat_s2.obtener_nodo(a, b) != None:                        
                        valor_nuevo_c.configure({'background': "white"})                        
                        valor_nuevo_c.delete(0, tk.END)
                        
    def clear_f(self):
        try:
            for child in self.inicial_a.winfo_children():
                child.destroy()
            for child in self.secundario_b.winfo_children():
                child.destroy()
            for child in self.tercer_c.winfo_children():
                child.destroy()
        except: 
            print('Error')
    
    def nuevo_bot(self):
        try:
            for child in self.opciones_bot.winfo_children():
                child.destroy()
        except: 
            print('Error')

    def matric_diferencia_simet(self, valor_inicial, valor_secundario):        
        nueva_matriz_usar = self.lista_matriz(valor_inicial)        
        x = int(nueva_matriz_usar.filas)
        y = int(nueva_matriz_usar.columnas)
        mat_s2 = self.lista_matriz(valor_secundario)
        x_a = int(mat_s2.filas)
        y_a = int(mat_s2.columnas)
        if x >= x_a:
            fila = x
        else:
            fila = x_a
        if y >= y_a:
            columna = y
        else:
            columna = y_a
        for a in range(fila+1):
            for b in range(columna+1):
                if a < x + 1 and b < y + 1:
                    card_c = Entry(self.inicial_a, width = 3)
                    card_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                    if a == 0 and b == 0:
                        card_c.insert(0,'A')
                        card_c.configure({'backgroun':'black'})
                        card_c.config(justify = 'center',fg = 'white')
                    if a == 0 and b > 0:
                        card_c.insert(0, b)
                        card_c.configure({'backgroun':'white'})
                        card_c.config(justify = 'center',fg = 'gray')
                    if a > 0 and b == 0:
                        card_c.insert(0, a)
                        card_c.configure({'backgroun':'white'})
                        card_c.config(justify = 'center',fg = 'gray')                    
                    if nueva_matriz_usar.obtener_nodo(a, b) != None:
                        card_c.insert(0,'*')
                        card_c.configure({'background': "#454545"})
                        card_c.config(justify = 'center', fg = 'white')
                if a < x_a+1 and b < y_a + 1:
                    car_d = Entry(self.secundario_b, width = 3)
                    car_d.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                    if a == 0 and b == 0:
                        car_d.insert(0,'A')
                        car_d.configure({'backgroun':'black'})
                        car_d.config(justify = 'center',fg = 'white')
                    if a == 0 and b > 0:
                        car_d.insert(0, b)
                        car_d.configure({'backgroun':'white'})
                        car_d.config(justify = 'center',fg = 'gray')
                    if a > 0 and b == 0:
                        car_d.insert(0, a)
                        car_d.configure({'backgroun':'white'})
                        car_d.config(justify = 'center',fg = 'gray')
                    if mat_s2.obtener_nodo(a, b) != None:
                        car_d.insert(0,'*')
                        car_d.configure({'background': "#454545"})
                        car_d.config(justify = 'center', fg = 'white')
                valor_nuevo_c = Entry(self.tercer_c, width = 3)
                valor_nuevo_c.grid(padx = 5, pady = 5, row = a, column = b, columnspan = 1)
                if a == 0 and b == 0:
                    valor_nuevo_c.insert(0,'A')
                    valor_nuevo_c.configure({'backgroun':'black'})
                    valor_nuevo_c.config(justify = 'center',fg = 'white')
                if a == 0 and b > 0:
                    valor_nuevo_c.insert(0, b)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if a > 0 and b == 0:
                    valor_nuevo_c.insert(0, a)
                    valor_nuevo_c.configure({'backgroun':'white'})
                    valor_nuevo_c.config(justify = 'center',fg = 'gray')
                if nueva_matriz_usar.obtener_nodo(a, b) != None:
                    valor_nuevo_c.insert(0,'*')
                    valor_nuevo_c.configure({'background': "#454545"})
                    valor_nuevo_c.config(justify = 'center', fg = 'white')
                    if mat_s2.obtener_nodo(a, b) != None:
                        valor_nuevo_c.configure({'background': "white"})                        
                        valor_nuevo_c.delete(0, tk.END)
                if mat_s2.obtener_nodo(a, b) != None:
                    valor_nuevo_c.insert(0,'*')
                    valor_nuevo_c.configure({'background': "#454545"})
                    valor_nuevo_c.config(justify = 'center', fg = 'white')
                    if nueva_matriz_usar.obtener_nodo(a, b) != None:                        
                        valor_nuevo_c.configure({'background': "white"})                        
                        valor_nuevo_c.delete(0, tk.END)

    def XML_OPCION(self):
        print('Cargando Archivo')
        time.sleep(0.5)
        print('.  .  .  .  .  .')
        time.sleep(0.5)
        try:
            archivo = filedialog.askopenfilename(title = "XML: ", filetypes = (("XML File", "*.xml"),("all files","*.*")))        
            arch_sep = minidom.parse(archivo)        
            try:
                archivo_name = arch_sep.getElementsByTagName('matriz')
                for matriz in archivo_name:            
                    csls_lns = 0
                    valor_inicial = matriz.getElementsByTagName('nombre')[0]
                    nom = valor_inicial.firstChild.data
                    fila = matriz.getElementsByTagName('filas')[0]
                    fil = fila.firstChild.data
                    columna = matriz.getElementsByTagName('columnas')[0]
                    col = columna.firstChild.data
                    novo_mat = Matriz_Ortogonal(nom, fil, col)
                    datos = matriz.getElementsByTagName('imagen')[0]
                    racises = datos.firstChild.data
                    separacion_por_saltos = racises.split('\n')
                    try:
                        del separacion_por_saltos[0]
                        del separacion_por_saltos[len(separacion_por_saltos) - 1]
                    except:
                        print('Error')
                    for a in range(len(separacion_por_saltos)):
                        fil_de_nd = list(separacion_por_saltos[a])
                        col_de_nd = 1
                        for b in range(len(fil_de_nd)):                    
                            if fil_de_nd[b] == '-' or fil_de_nd[b]=='*':                        
                                if fil_de_nd[b] == '*':
                                    novo_mat.agregar_valor('*',(a + 1),col_de_nd)
                                    csls_lns += 1
                                col_de_nd += 1
                    self.matriz.agregar_valor(novo_mat)
                    hora = datetime.datetime.today().strftime("%Y-%m-%d ::-::  %H:%M:%S")
                    casilla = ((int(fil)*int(col)) - csls_lns)
                    self.matriz_modificar +='<tr><td><h3 class="codatos">'+hora+'</h3></td><td><h3 class="codatos">'+nom+'</h3></td><td><h3 class="codatos">'+str(csls_lns)+'</h3></td><td><h3 class="codatos">'+str(casilla)+'</h3></td></tr>\n'
                self.matriz.nodo_a_mostrar()
                self.matriz.devolver_valor(1).obtener_fila()
            except:
                print('Error')
        except:
            print('Error')
        print('Archivo XML Cargado con Exito')
        
    def pdfandpdf(self):
        try:
            os.system('Desktop\IPC2_Proyecto2_201906051.pdf')            
        except:
            print('Error: ARCHIVO NO ENCONTRADO')

    def creacion_html(self):
        print('Procesando')
        time.sleep(0.5)
        print('.  .  .  .')
        time.sleep(0.5)
        f = open('Desktop\C.201906051_Proyecto2\Reporte_IPC2_Proyecto2.html', 'w')
        mensaje = '''<!DOCTYPE html>
        <html lang="en"><head><title>Reporte | Proyecto 2 IPC 2</title><link rel="icon" href="https://es.seaicons.com/wp-content/uploads/2016/06/NFSShift-logo-2-icon.png">
        <style>
        body{background-image: url("https://elandroidelibre.elespanol.com/wp-content/uploads/2020/10/Fondos-pantalla-Huawei-Mate-40-10.jpg");background-repeat:no-repeat;background-attachment: fixed;} 
        h1{text-align:center; color: white; font-weight: bold; margin:left;} h2{text-align:center; color: gray;margin:left;} h3{text-align:left; margin-left: 30%; color: #483D8B;} 
        .dates{text-align:left; margin-left: 30%; color: #2F4F4F;} h4{text-align:left; margin-left: 30%; color: #6A5ACD;} .totas{text-align:right; margin-right: 35%; margin-top: -40px; color: #008B8B;} 
        h6{color: white; text-align: right; margin-right: 5%; font-size: 15px; margin-bottom: -25px;}
        .codatos{color: white; text-align: left; font-size: 14px;}
        .coencabezado{color: #008B8B; text-align: left; font-size: 14px;}
        table{width: 50%; text-align: left; margin-left: 25%; margin:left; margin-right: 25%;}
        </style></head><body><h1>Reporte ::-:: IPC2-P2</h1><h2>Matrices Cargadas</h2>
        <table><tr><th><strong><h3 class="coencabezado">Dia - Hora</h3></strong></th><th><strong><h3 class="coencabezado">Matriz</h3></strong></th><th><strong><h3 class="coencabezado">Celdas Llenas</h3></strong></th><th><strong><h3 class="coencabezado">Celdas Vacias</h3></strong></th></tr>'''
        #print(self.matriz_modificar)
        mensaje += self.matriz_modificar
        mensaje += '''</table>'''
        #print(self.acciones_a_hacer)
        mensaje += '''<h2>Operaciones</h2><table><tr><th><strong><h3 class="coencabezado">Dia - Hora</h3></strong></th><th><strong><h3 class="coencabezado">Error</h3></strong></th><th><strong><h3 class="coencabezado">Operacion</h3></strong></th><th><strong><h3 class="coencabezado">Matriz "A"</h3></strong></th><th><strong><h3 class="coencabezado">Matriz "B"</h3></strong></th></tr>'''
        mensaje += self.acciones_a_hacer
        mensaje += '''</table></body><h6>Juan F. Urbina S.</h6><h6>201906051</h6></html>'''
        f.write(mensaje)
        f.close()
        print('Abriendo "Reporte_IPC2_Proyecto2"')
        time.sleep(1.5)
        os.startfile('Desktop\C.201906051_Proyecto2\Reporte_IPC2_Proyecto2.html')
        
        

iniciar = inicio()