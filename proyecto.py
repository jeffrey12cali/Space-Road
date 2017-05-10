from tkinter import*
from PIL import ImageTk, Image
import time

fondo = Image.open("fondo.jpg")
contador = 1



def menu():
	global fondo
	#evento para le selección de jugador
	def select_move(event):
		if event.keysym == "Up":
			background.coords(selecter, 211, 330)
		elif event.keysym == "Down":
			background.coords(selecter, 211, 427)
	#evento para elegir el número de jugadores
	def enter(event):
		if background.coords(selecter) == [211.0, 330.0]:
			principal.destroy()
			nombre()
		elif background.coords(selecter) == [211.0, 427.0]:
			print("down")
	#Declaración de la variables que se utilizarán en el canvas
	titulo_img = Image.open("titulo.png")
	players = Image.open("players.png")
	seleccionador = Image.open("seleccionador.png")
	fondo = fondo.resize((800, 600))
    #generar la ventana del menú
	principal = Tk()
	principal.geometry("800x600")
	principal.title("Space Road")
	principal.resizable(0,0)
    #Generar Canvas
	background = Canvas(principal, width=800, height=600)
	background.pack()
	#Integrar fondo al canvas
	background.fondo = ImageTk.PhotoImage(fondo)
	background.create_image(0, 0, image=background.fondo, anchor='nw')
	#Integrar título al canvas
	background.titulo = ImageTk.PhotoImage(titulo_img)
	background.create_image(125, 20, image=background.titulo, anchor="nw")
	#Integrar la selección de jugadores al canvas
	background.players = ImageTk.PhotoImage(players)
	background.create_image(0, 0, image=background.players, anchor="nw")
	#Integrar el seleccionador
	background.seleccionador = ImageTk.PhotoImage(seleccionador)
	selecter = background.create_image(211, 330, image=background.seleccionador, anchor="nw")
	#Movimiento al seleccionador
	background.bind_all("<KeyPress-Up>", select_move)
	background.bind_all("<KeyPress-Down>", select_move)
	background.bind_all("<KeyPress-Return>", enter)
	principal.mainloop()

def nombre():
	#Evento para la aparición de la insturcción
	def siguiente(event):
		global contador
		if contador == 1:
			press_enter = nameground.create_image(0, 0, image=p_enter, anchor="nw")
			contador = 2
	#Definición de la función para pasar a la ventana de niveles
	def pasar(event):
		nombre.destroy()
		nivel()
	#Declaración de la variables que se utilizarán en el canvas
	question = Image.open("question2.png")
	press = Image.open("press enter.png")
	#Generar la ventana
	nombre = Tk()
	nombre.geometry("800x600")
	nombre.title("Space Road")
	nombre.resizable(0,0)
	#Generar Canvas
	nameground = Canvas(nombre, width=800, height=600)
	nameground.place(x=0, y=0)
	#Integrar fondo al canvas
	nameground.fondo = ImageTk.PhotoImage(question)
	nameground.create_image(0, 0, image=nameground.fondo, anchor="nw")
	#Añadir caja de texto al canvas
	name = Entry(nameground, bg="#3c115e", bd=0, fg="#94d0ff", font="System 42", width=13, justify=CENTER)
	name.place(x=180, y=302)
	#Añadir imagen de instrucción
	p_enter = ImageTk.PhotoImage(press)
	#Evento para continuar
	nameground.bind_all("<Key>", siguiente)
	nameground.bind_all("<KeyPress-Return>", pasar)

	nombre.mainloop()

def nivel():
	global fondo
	#Definición de la función para mover el seleccionador hacia abajo
	def move_down(event):
		if levelground.coords(selecter) >= [198, 191] and levelground.coords(selecter) < [198, 475]:
			levelground.move(selecter, 0, 71)
	#Definición de la función para mover el seleccionador hacia arriba
	def move_up(event):
		if levelground.coords(selecter) <= [198, 475] and levelground.coords(selecter) > [198, 191]:
			levelground.move(selecter, 0, -71)
	#Definición de la función para entrar al nivel seleccionado
	def enter_lvl(event):
		if levelground.coords(selecter) == [198, 191]:
			print("level 1")
		elif levelground.coords(selecter) == [198, 262]:
			print("level 2")
		elif levelground.coords(selecter) == [198, 333]:
			print("level 3")
		elif levelground.coords(selecter) == [198, 404]:
			print("level 4")
		elif levelground.coords(selecter) == [198, 475]:
			print("level 5")
	#Declaración de las variables que se utilizarán en el canvas
	fondo = fondo.resize((800, 600))
	levels = Image.open("levels.png")
	seleccionador = Image.open("seleccionador.png")
	#Generar la ventana
	niveles = Tk()
	niveles.geometry("800x600")
	niveles.title("Space Road")
	niveles.resizable(0,0)
	#Generar canvas
	levelground = Canvas(niveles, width=800, height=600)
	levelground.place(x=0, y=0)
	#Integrar fondo al canvas
	levelground.fondo = ImageTk.PhotoImage(fondo)
	levelground.create_image(0, 0, image=levelground.fondo, anchor="nw")
	#Integrar imagen de los niveles al canvas
	levelground.levels = ImageTk.PhotoImage(levels)
	lev = levelground.create_image(0, 0, image=levelground.levels, anchor="nw")
	#Integrar el seleccionador
	levelground.seleccionador = ImageTk.PhotoImage(seleccionador)
	selecter = levelground.create_image(198, 191, image=levelground.seleccionador, anchor="nw")
	#Aplicar movimiento al seleccionador
	levelground.bind_all("<KeyPress-Up>", move_up)
	levelground.bind_all("<KeyPress-Down>", move_down)
	#Entrar en el nivel seleccionado 
	levelground.bind_all("<KeyPress-Return>", enter_lvl)
	niveles.mainloop()

def level1_1p():
	def movimientoI_falc(event):
		level_one.move(falc, -5, 0)
		pass
	def movimientoD_falc(event):
		level_one.move(falc, 5, 0)
		pass


	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space.png")
	bandas = Image.open("bandas.png")
	falcon = Image.open("falcon.png")
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(234, -4400, image=espacio.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(399, 501, image=falcon.jugador, anchor="nw")
	#Movimiento del jugador
	distancia = 5
	movimientos = {
		"left" : (-distancia, 0),
		"right" : (distancia, 0)
		}
	def move_press(event):
		key = (event.keysym).lower()
		level_one.move(falc, *movimientos[key])

	level_one.bind_all("<KeyPress-Left>", move_press)
	level_one.bind_all("<KeyPress-Right>", move_press)
	#Contador para iniciar la partida
	init = 3
	while init >= 0:
		time.sleep(1)
		init -= 1
		if init == 0:
			start = True
			print("start")
	#Gasolina
	#if start == True:
	#Aplicar movimiento al fondo
	while start == True:
		level_one.move(space, 0, 5)
		level1.update()
		time.sleep(0.01)

	level1.mainloop()

level1_1p()
