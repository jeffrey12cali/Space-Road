from tkinter import*
from PIL import ImageTk, Image
import time

fondo = Image.open("fondo.jpg")
contador = 1
nombre_p1 = "Jeffrey"
velocidad = 0



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
	global nombre_p1
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
	#Pasar el nombre a la variable global
	nombre_p1 = name.get()


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
	global nombre_p1
	global init
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
	falc = level_one.create_image(428, 501, image=falcon.jugador, anchor="nw")
	#Movimiento de falcon
	#Integrar imagenes para la explosion
	expl1 = Image.open("explosion1.png")
	expl2 = Image.open("explosion2.png")
	expl3 = Image.open("explosion3.png")
	expl4 = Image.open("explosion4.png")
	expl5 = Image.open("explosion5.png")
	expl6 = Image.open("explosion6.png")

	explo1 = ImageTk.PhotoImage(expl1)
	explo2 = ImageTk.PhotoImage(expl2)
	explo3 = ImageTk.PhotoImage(expl3)
	explo4 = ImageTk.PhotoImage(expl4)
	explo5 = ImageTk.PhotoImage(expl5)
	explo6 = ImageTk.PhotoImage(expl6)

	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Integrar el enemigo con velocidad constante
	#Intergrar el nombre del jugador a la pantalla
	name = Label(level_one, text=nombre_p1, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=784, y=36)
	#Movimiento del jugador
	distancia = 5
	movimientos = {
		"left" : (-distancia, 0),
		"right" : (distancia, 0)
		}
	def move_press(event):
		if level_one.coords(falc) >= [392, 501] and level_one.coords(falc) <= [469, 501]:
			key = (event.keysym).lower()
			level_one.move(falc, * movimientos[key])
	level_one.bind_all("<KeyPress-Left>", move_press)
	level_one.bind_all("<KeyPress-Right>", move_press)
	#Movimiento de la carretera
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
		print(velocidad)
	def deaccelerate(event): #No sirve todavía
		global velocidad
		while velocidad >= -1 and velocidad <= 309:
			velocidad = velocidad - 1
		print(velocidad)
	level_one.bind_all("<KeyPress-Up>", accelerate)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate)
	#Entrar al menú de pausa
	
	#Contador para iniciar la partida
	init = 4
	cont_partida = Label(level_one, text=init, bg="black", fg="#4cffb5", font=("System", 70))
	cont_partida.place(x=431, y=249)

	for i in range(4):
		time.sleep(1)
		init = init - 1		
		cont_partida.config(text=init)
		cont_partida.update()
		if init == 0:
			start = True
			cont_partida.destroy()

	#Declaración de la energía de la nave
	energy = 100
	eneg = Label(level_one, text=energy, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=830, y=427)
		#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=784, y=353)
	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=784, y=234)
	#Aplicar movimiento al fondo
	def juego(energy):
		#La nave del jugador vuelve al lugar de origen
		level_one.coords(falc, 428, 501)
		while start == True and energy > 0:
			falc_coords = level_one.coords(falc)
			level_one.move(space, 0, velocidad/50)
			energy = energy - 0.01
			eneg.config(text=int(energy))
			speed.config(text=str(velocidad)+"Km/s")
			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [392, 501] or level_one.coords(falc) >= [469, 501]:
				energy = energy - 10
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego(energy))
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)
	juego(energy)



	level1.mainloop()

level1_1p()
