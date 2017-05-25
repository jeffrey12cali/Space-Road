from tkinter import*
from PIL import ImageTk, Image
import time
import random

fondo = Image.open("fondo.jpg")
#VARIABLES GLOBALES UTILIZADAS EN EL MODO 1 JUGADOR
#Utilizada en la función nombre para la aparición de una instrucción
contador = 1
#Utilizada en la función "nombre" para guardar el nombre que escribe el usuario
nombre_p1 = ""
#Utilizada en la función "level1" para controlar la velocidad con la que se mueve el mapa
velocidad = 0
#Utilizado en el menú de pausa
pausado = False #Indica si el juego se encuentra en pausa o no
p_selecter = 0  #Es la declaración global para el seleccionador del menú de pausa
#Energía de la nave
energy = 100
#Variables utilizadas para la declaración del enemigo "Wyvern" y su caja para las colisiones
wyvern = 0
wyvern_box = 0
#Variables utilizadas para la declaración del enemigo "Golden Fox" y su caja para las colisiones
goldenfox = 0
goldenfox_box = 0
cambio = False
#Variables utilizadas para la declaración del enemigo "Hyper Speeder" y su caja para las colisiones
hyper = 0
hyper_box = 0
cambio_hyper = False
#Variables utilizadas para la declaración de la energy ball y su caja para las colisiones
ball = 0
ball_box = 0
ball_in_movement = False
#Variables utilizadas para la declaración del agujero negro y su caja para las colisiones
hole = 0
hole_box = 0
#Utilizado para almacenar la puntiación del jugador en el modo 1p
puntos_1p = 0
#Utilizado para posteriormente guardar la partda
coordenadas_juego_l1 = [234, -18984]
coordenadas_juego_l1_x = coordenadas_juego_l1[0]
coordenadas_juego_l1_y = coordenadas_juego_l1[1]
#Indicador de si el juego ha sido cargado o no
cargado = False
##############################################################################################

#VARIABLES PARA EL MODO DOS JUGADORES
#Pantalla de nombres
nombre1 = ""
nombre2 = ""
contador2 = 1
#Vairables utilizadas para los niveles de 2 jugadores
#Variables para la energía 
energy1 = 100
energy2 = 100
#Variables para la velocidad
velocidad1 = 0
velocidad2 = 0
#Variables para los puntos
puntos1 = 0
puntos2 = 0
#Variable para el enemigo Wyvern
wyvern2 = 0
#Variables para el enemigo Golden Fox
cambio2 = False
goldenfox2 = 0
#Variables para el enemigo Hyper Speeder
hyper2 = 0
cambio_hyper = False
#Varialbes para la energy ball
ball2 = 0
ball2_box = 0
ball2_in_movement = False
#Variables para el agujero negro
hole2 = 0
hole2_box = 0





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
			principal.destroy()
			nombre_2p()
	#Evento para cargar la partida
	def load_game(event):
		global nombre_p1
		global energy
		global puntos_1p
		global coordenadas_juego_l1
		global cargado
		with open("save.txt", "r") as cargar:
			lista_cargar = cargar.readline()
			elementos = lista_cargar.split()
			nombre_p1 = StringVar()
			nombre_p1.set(elementos[0])
			energy = int(float(elementos[1]))
			puntos_1p = int(elementos[2])
			coordenadas_juego = list(elementos[3]+elementos[4])
			coordenadas_juego_l1_x = coordenadas_juego_l1[0]
			coordenadas_juego_l1_y = coordenadas_juego_l1[1]
			nivel = elementos[5]
			cargado = True
			if nivel == "lvl_1":
				principal.destroy()
				level1_1p()
			elif nivel == "lvl_2":
				principal.destroy()
				level2_1p()
			elif nivel == "lvl_3":
				principal.destroy()
				level3_1p()
			elif nivel == "lvl_4":
				principal.destroy()
				level4_1p()
			elif nivel == "lvl_5":
				principal.destroy()
				level5_1p()
	if cargado == False:
		energy = 100
		puntos_1p = 0
		coordenadas_juego_l1 = [234, -18984]
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
	principal.focus_force()
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
	#Instrucción para cargar partida
	loa = Image.open("load.png")
	lo = ImageTk.PhotoImage(loa)
	load = background.create_image(0, 0, image=lo, anchor="nw")
	#Movimiento al seleccionador
	background.bind_all("<KeyPress-Up>", select_move)
	background.bind_all("<KeyPress-Down>", select_move)
	background.bind_all("<KeyPress-Return>", enter)
	background.bind_all("<KeyPress-l>", load_game)
	principal.mainloop()

def nombre():
	global nombre_p1
	#Evento para la aparición de la insturcción
	def siguiente(event):
		global contador
		if contador == 1:
			press_enter = nameground.create_image(0, 0, image=p_enter, anchor="nw")
			contador = 2
	#Declaración de la variables que se utilizarán en el canvas
	question = Image.open("question2.png")
	press = Image.open("press enter.png")
	#Generar la ventana
	nombre = Tk()
	nombre.geometry("800x600")
	nombre.title("Space Road")
	nombre.resizable(0,0)
	nombre.focus_force()
	#Generar Canvas
	nameground = Canvas(nombre, width=800, height=600)
	nameground.place(x=0, y=0)
	#Integrar fondo al canvas
	nameground.fondo = ImageTk.PhotoImage(question)
	nameground.create_image(0, 0, image=nameground.fondo, anchor="nw")
	#Añadir caja de texto al canvas
	nombre_p1 = StringVar()
	name = Entry(nameground, textvariable=nombre_p1, bg="#3c115e", bd=0, fg="#94d0ff", font="System 42", width=13, justify=CENTER)
	name.place(x=180, y=302)
	#Pasar el nombre a la variable global
	#Añadir imagen de instrucción
	p_enter = ImageTk.PhotoImage(press)
	#Definición de la función para pasar a la ventana de niveles
	def pasar(event):
		nombre.destroy()
		nivel()
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
			niveles.destroy()
			level1_1p()
		elif levelground.coords(selecter) == [198, 262]:
			niveles.destroy()
			level2_1p()
		elif levelground.coords(selecter) == [198, 333]:
			niveles.destroy()
			level3_1p()
		elif levelground.coords(selecter) == [198, 404]:
			niveles.destroy()
			level4_1p()
		elif levelground.coords(selecter) == [198, 475]:
			niveles.destroy()
			level5_1p()
	#Declaración de las variables que se utilizarán en el canvas
	fondo = fondo.resize((800, 600))
	levels = Image.open("levels.png")
	seleccionador = Image.open("seleccionador.png")
	#Generar la ventana
	niveles = Tk()
	niveles.geometry("800x600")
	niveles.title("Space Road")
	niveles.resizable(0,0)
	niveles.focus_force()
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
	global energy
	global wyvern
	global wyvern_box
	global goldenfox
	global hyper
	global ball
	global hole
	global cargado

	#Función para guardar partida
	def save_game():
		global nombre_p1
		global energy
		global puntos_1p
		global coordenadas_juego
		guardado = open("save.txt", "w")
		lista_guardado = [str(nombre_p1), " ", str(energy), " ", str(puntos_1p), " ", str(coordenadas_juego_l1), " ", "lvl_1"]
		guardado.writelines(lista_guardado)
		guardado.close()

	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space.jpg")
	bandas = Image.open("bandas.png")
	falcon = Image.open("falcon.png")
	nombre_p1 = nombre_p1.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.title("Space Road")
	level1.resizable(0, 0)
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(234, -18984, image=espacio.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(428, 501, image=falcon.jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("youwin.png")
	win = ImageTk.PhotoImage(w)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(0, 602, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 8000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 10000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole = level_one.create_image(0, 600, image=ho, anchor="nw")

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
	def desacelerar():
		global velocidad
		velocidad = velocidad - 1
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	level_one.bind_all("<KeyPress-Up>", accelerate)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
			p_selecter = level_one.create_image(97, 158, image=pause_selecter, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
	#Imagen del seleccionador
	ps = Image.open("seleccionador.png")
	pause_selecter = ImageTk.PhotoImage(ps)
	#Función para el movimiento del seleccionador
	def move_down_pause(event):
		global p_selecter
		if level_one.coords(p_selecter) < [97, 418] and level_one.coords(p_selecter) >= [97, 158]:
			level_one.move(p_selecter, 0, 130)
		elif level_one.coords(p_selecter) == [97, 418]:
			level_one.coords(p_selecter, 97, 158)
	#Imagen para el guardado
	s = Image.open("saved.png")
	sv = ImageTk.PhotoImage(s)
	saved = level_one.create_image(0, 700, image=sv, anchor="nw")
	#Evento al presionar la tecla "enter"
	def eleccion_menu_pausa(event):
		global p_selecter
		global pausado
		if level_one.coords(p_selecter) == [97, 158]:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
			level_one.delete(saved)
			juego()
		elif level_one.coords(p_selecter) == [97, 288]:
			save_game()
			saved = level_one.create_image(0, 0, image=sv, anchor="nw")
		elif level_one.coords(p_selecter) == [97, 418]:
			level1.destroy()
			menu()
	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)
	level_one.bind_all("<KeyPress-Down>", move_down_pause)
	level_one.bind_all("<KeyPress-Return>", eleccion_menu_pausa)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=830, y=427)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=784, y=353)

	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=784, y=234)

	#Puntuación
	puntos = Label(level_one, text=puntos_1p, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=784, y=138)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy
		global wyvern
		global wyvern_box
		global puntos_1p
		global goldenfox
		global cambio
		global hyper
		global ball
		global hole
		global velocidad
		global coordenadas_juego

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 438, level_one.coords(falc)[1])
		#Se crea el enemigo wyvern
		while start == True and energy > 0 and pausado == False and level_one.coords(space)[1] < 1: 
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			level_one.after(5000, wyvern_spawn)
			level_one.move(space, 0, velocidad/70)
			level_one.move(wyvern, 0, 3)


			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern_coords = level_one.coords(wyvern)

			#Aparición del agujero negro
			hole_spawn()
			hole_box = level_one.bbox(hole)
			hole_coords = level_one.coords(hole)
			level_one.move(hole, 0, 3)


			#Colisión con el agujero negro
			if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 404:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 1
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 464:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 1
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_box = level_one.bbox(ball)
			level_one.move(ball, 0, 3)
			#Colisión con la energy ball
			if 3 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy = energy + 50
				eneg.config(text=int(energy))
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			level_one.move(hyper, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			#Movimiento de cambio de carril

			if level_one.coords(hyper) > [404, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 404 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 457:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [464, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 464 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 457:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [404, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 404 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [464, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 464 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy = energy - 0.01
			eneg.config(text=int(energy))
			speed.config(text=str(velocidad)+"Km/s")

			
			#Colisión con Wyvern
			if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy = energy - 2
				eneg.config(text=int(energy))
				if level_one.coords(goldenfox)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [392, 501] or level_one.coords(goldenfox) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox
			elif 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy = energy - 2
				eneg.config(text=int(energy))
				if level_one.coords(wyvern)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [392, 501] or level_one.coords(wyvern) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder
			elif 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy = energy - 2
				eneg.config(text=int(energy))
				if level_one.coords(hyper)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [392, 501] or level_one.coords(hyper) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Conteo de la puntuación
			elif falc_coords[1] == wyvern_coords[1]:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif hyper_coords[1] == 502:
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [392, 501] or level_one.coords(falc) >= [469, 501]:
				energy = energy - 10
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)

		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			level2_1p()
		elif energy == 0:
			loser = level_one.create_image(0, 0, image=los, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			menu()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 438, 501)
	level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

def level2_1p():
	global nombre_p1
	global init
	global energy
	global wyvern
	global wyvern_box
	global goldenfox
	global hyper
	global ball
	global hole
	global cargado

	#Función para guardar partida
	def save_game():
		global nombre_p1
		global energy
		global puntos_1p
		global coordenadas_juego
		guardado = open("save.txt", "w")
		lista_guardado = [str(nombre_p1), " ", str(energy), " ", str(puntos_1p), " ", str(coordenadas_juego_l1), " ", "lvl_2"]
		guardado.writelines(lista_guardado)
		guardado.close()

	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space2.jpg")
	bandas = Image.open("bandas.png")
	falcon = Image.open("falcon.png")
	nombre_p1 = nombre_p1.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(234, -18984, image=espacio.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(428, 501, image=falcon.jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("youwin.png")
	win = ImageTk.PhotoImage(w)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(0, 602, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 4000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 8000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 7000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole = level_one.create_image(0, 600, image=ho, anchor="nw")

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
	def desacelerar():
		global velocidad
		velocidad = velocidad - 1
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	level_one.bind_all("<KeyPress-Up>", accelerate)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
			p_selecter = level_one.create_image(97, 158, image=pause_selecter, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
	#Imagen del seleccionador
	ps = Image.open("seleccionador.png")
	pause_selecter = ImageTk.PhotoImage(ps)
	#Función para el movimiento del seleccionador
	def move_down_pause(event):
		global p_selecter
		if level_one.coords(p_selecter) < [97, 418] and level_one.coords(p_selecter) >= [97, 158]:
			level_one.move(p_selecter, 0, 130)
		elif level_one.coords(p_selecter) == [97, 418]:
			level_one.coords(p_selecter, 97, 158)
	#Imagen para el guardado
	s = Image.open("saved.png")
	sv = ImageTk.PhotoImage(s)
	saved = level_one.create_image(0, 700, image=sv, anchor="nw")
	#Evento al presionar la tecla "enter"
	def eleccion_menu_pausa(event):
		global p_selecter
		global pausado
		if level_one.coords(p_selecter) == [97, 158]:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
			level_one.delete(saved)
			juego()
		elif level_one.coords(p_selecter) == [97, 288]:
			save_game()
			saved = level_one.create_image(0, 0, image=sv, anchor="nw")
		elif level_one.coords(p_selecter) == [97, 418]:
			level1.destroy()
			menu()
	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)
	level_one.bind_all("<KeyPress-Down>", move_down_pause)
	level_one.bind_all("<KeyPress-Return>", eleccion_menu_pausa)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=830, y=427)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=784, y=353)

	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=784, y=234)

	#Puntuación
	puntos = Label(level_one, text=puntos_1p, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=784, y=138)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy
		global wyvern
		global wyvern_box
		global puntos_1p
		global goldenfox
		global cambio
		global hyper
		global ball
		global hole
		global velocidad
		global coordenadas_juego

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 438, level_one.coords(falc)[1])
		#Se crea el enemigo wyvern
		while start == True and energy > 0 and pausado == False and level_one.coords(space)[1] < 1: 
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			level_one.after(5000, wyvern_spawn)
			level_one.move(space, 0, velocidad/70)
			level_one.move(wyvern, 0, 3)


			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern_coords = level_one.coords(wyvern)

			#Aparición del agujero negro
			hole_spawn()
			hole_box = level_one.bbox(hole)
			hole_coords = level_one.coords(hole)
			level_one.move(hole, 0, 3)


			#Colisión con el agujero negro
			if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 404:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 2
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 464:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 2
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_box = level_one.bbox(ball)
			level_one.move(ball, 0, 3)
			#Colisión con la energy ball
			if 3 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy = energy + 20
				eneg.config(text=int(energy))
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			level_one.move(hyper, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			#Movimiento de cambio de carril

			if level_one.coords(hyper) > [404, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 404 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 457:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [464, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 464 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 457:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [404, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 404 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [464, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 464 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy = energy - 0.01
			eneg.config(text=int(energy))
			speed.config(text=str(velocidad)+"Km/s")

			
			#Colisión con Wyvern
			if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy = energy - 4
				eneg.config(text=int(energy))
				if level_one.coords(goldenfox)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [392, 501] or level_one.coords(goldenfox) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox
			elif 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy = energy - 4
				eneg.config(text=int(energy))
				if level_one.coords(wyvern)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [392, 501] or level_one.coords(wyvern) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder
			elif 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy = energy - 4
				eneg.config(text=int(energy))
				if level_one.coords(hyper)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [392, 501] or level_one.coords(hyper) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Conteo de la puntuación
			elif falc_coords[1] == wyvern_coords[1]:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif hyper_coords[1] == 502:
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [392, 501] or level_one.coords(falc) >= [469, 501]:
				energy = energy - 15
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)

		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			level3_1p()
		elif energy == 0:
			loser = level_one.create_image(0, 0, image=los, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			menu()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 438, 501)
	level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

def level3_1p():
	global nombre_p1
	global init
	global energy
	global wyvern
	global wyvern_box
	global goldenfox
	global hyper
	global ball
	global hole
	global cargado

	#Función para guardar partida
	def save_game():
		global nombre_p1
		global energy
		global puntos_1p
		global coordenadas_juego
		guardado = open("save.txt", "w")
		lista_guardado = [str(nombre_p1), " ", str(energy), " ", str(puntos_1p), " ", str(coordenadas_juego_l1), " ", "lvl_3"]
		guardado.writelines(lista_guardado)
		guardado.close()

	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space3.jpg")
	bandas = Image.open("bandas.png")
	falcon = Image.open("falcon.png")
	nombre_p1 = nombre_p1.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(234, -18984, image=espacio.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(428, 501, image=falcon.jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("youwin.png")
	win = ImageTk.PhotoImage(w)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(0, 602, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 600:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 7000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 6000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole = level_one.create_image(0, 600, image=ho, anchor="nw")

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
	def desacelerar():
		global velocidad
		velocidad = velocidad - 1
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	level_one.bind_all("<KeyPress-Up>", accelerate)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
			p_selecter = level_one.create_image(97, 158, image=pause_selecter, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
	#Imagen del seleccionador
	ps = Image.open("seleccionador.png")
	pause_selecter = ImageTk.PhotoImage(ps)
	#Función para el movimiento del seleccionador
	def move_down_pause(event):
		global p_selecter
		if level_one.coords(p_selecter) < [97, 418] and level_one.coords(p_selecter) >= [97, 158]:
			level_one.move(p_selecter, 0, 130)
		elif level_one.coords(p_selecter) == [97, 418]:
			level_one.coords(p_selecter, 97, 158)
	#Imagen para el guardado
	s = Image.open("saved.png")
	sv = ImageTk.PhotoImage(s)
	saved = level_one.create_image(0, 700, image=sv, anchor="nw")
	#Evento al presionar la tecla "enter"
	def eleccion_menu_pausa(event):
		global p_selecter
		global pausado
		if level_one.coords(p_selecter) == [97, 158]:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
			level_one.delete(saved)
			juego()
		elif level_one.coords(p_selecter) == [97, 288]:
			save_game()
			saved = level_one.create_image(0, 0, image=sv, anchor="nw")
		elif level_one.coords(p_selecter) == [97, 418]:
			level1.destroy()
			menu()
	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)
	level_one.bind_all("<KeyPress-Down>", move_down_pause)
	level_one.bind_all("<KeyPress-Return>", eleccion_menu_pausa)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=830, y=427)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=784, y=353)

	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=784, y=234)

	#Puntuación
	puntos = Label(level_one, text=puntos_1p, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=784, y=138)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy
		global wyvern
		global wyvern_box
		global puntos_1p
		global goldenfox
		global cambio
		global hyper
		global ball
		global hole
		global velocidad
		global coordenadas_juego

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 438, level_one.coords(falc)[1])
		#Se crea el enemigo wyvern
		while start == True and energy > 0 and pausado == False and level_one.coords(space)[1] < 1: 
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			level_one.after(5000, wyvern_spawn)
			level_one.move(space, 0, velocidad/70)
			level_one.move(wyvern, 0, 3)


			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern_coords = level_one.coords(wyvern)

			#Aparición del agujero negro
			hole_spawn()
			hole_box = level_one.bbox(hole)
			hole_coords = level_one.coords(hole)
			level_one.move(hole, 0, 3)


			#Colisión con el agujero negro
			if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 404:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 3
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 464:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 3
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_box = level_one.bbox(ball)
			level_one.move(ball, 0, 3)
			#Colisión con la energy ball
			if 3 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy = energy + 15
				eneg.config(text=int(energy))
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			level_one.move(hyper, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			#Movimiento de cambio de carril

			if level_one.coords(hyper) > [404, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 404 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 457:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [464, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 464 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 457:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [404, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 404 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [464, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 464 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy = energy - 0.01
			eneg.config(text=int(energy))
			speed.config(text=str(velocidad)+"Km/s")

			
			#Colisión con Wyvern
			if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy = energy - 5
				eneg.config(text=int(energy))
				if level_one.coords(goldenfox)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [392, 501] or level_one.coords(goldenfox) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox
			elif 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy = energy - 5
				eneg.config(text=int(energy))
				if level_one.coords(wyvern)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [392, 501] or level_one.coords(wyvern) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder
			elif 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy = energy - 5
				eneg.config(text=int(energy))
				if level_one.coords(hyper)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [392, 501] or level_one.coords(hyper) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Conteo de la puntuación
			elif falc_coords[1] == wyvern_coords[1]:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif hyper_coords[1] == 502:
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [392, 501] or level_one.coords(falc) >= [469, 501]:
				energy = energy - 20
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)

		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			level4_1p()
		elif energy == 0:
			loser = level_one.create_image(0, 0, image=los, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			menu()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 438, 501)
	level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

def level4_1p():
	global nombre_p1
	global init
	global energy
	global wyvern
	global wyvern_box
	global goldenfox
	global hyper
	global ball
	global hole
	global cargado

	#Función para guardar partida
	def save_game():
		global nombre_p1
		global energy
		global puntos_1p
		global coordenadas_juego
		guardado = open("save.txt", "w")
		lista_guardado = [str(nombre_p1), " ", str(energy), " ", str(puntos_1p), " ", str(coordenadas_juego_l1), " ", "lvl_4"]
		guardado.writelines(lista_guardado)
		guardado.close()
	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space4.jpg")
	bandas = Image.open("bandas.png")
	falcon = Image.open("falcon.png")
	nombre_p1 = nombre_p1.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(234, -18984, image=espacio.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(428, 501, image=falcon.jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("youwin.png")
	win = ImageTk.PhotoImage(w)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(0, 602, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 6000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole = level_one.create_image(0, 600, image=ho, anchor="nw")

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
	def desacelerar():
		global velocidad
		velocidad = velocidad - 1
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	level_one.bind_all("<KeyPress-Up>", accelerate)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
			p_selecter = level_one.create_image(97, 158, image=pause_selecter, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
	#Imagen del seleccionador
	ps = Image.open("seleccionador.png")
	pause_selecter = ImageTk.PhotoImage(ps)
	#Función para el movimiento del seleccionador
	def move_down_pause(event):
		global p_selecter
		if level_one.coords(p_selecter) < [97, 418] and level_one.coords(p_selecter) >= [97, 158]:
			level_one.move(p_selecter, 0, 130)
		elif level_one.coords(p_selecter) == [97, 418]:
			level_one.coords(p_selecter, 97, 158)
	#Imagen para el guardado
	s = Image.open("saved.png")
	sv = ImageTk.PhotoImage(s)
	saved = level_one.create_image(0, 700, image=sv, anchor="nw")
	#Evento al presionar la tecla "enter"
	def eleccion_menu_pausa(event):
		global p_selecter
		global pausado
		if level_one.coords(p_selecter) == [97, 158]:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
			level_one.delete(saved)
			juego()
		elif level_one.coords(p_selecter) == [97, 288]:
			save_game()
			saved = level_one.create_image(0, 0, image=sv, anchor="nw")
		elif level_one.coords(p_selecter) == [97, 418]:
			level1.destroy()
			menu()
	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)
	level_one.bind_all("<KeyPress-Down>", move_down_pause)
	level_one.bind_all("<KeyPress-Return>", eleccion_menu_pausa)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=830, y=427)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=784, y=353)

	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=784, y=234)

	#Puntuación
	puntos = Label(level_one, text=puntos_1p, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=784, y=138)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy
		global wyvern
		global wyvern_box
		global puntos_1p
		global goldenfox
		global cambio
		global hyper
		global ball
		global hole
		global velocidad
		global coordenadas_juego

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 438, level_one.coords(falc)[1])
		#Se crea el enemigo wyvern
		while start == True and energy > 0 and pausado == False and level_one.coords(space)[1] < 1: 
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			level_one.after(5000, wyvern_spawn)
			level_one.move(space, 0, velocidad/70)
			level_one.move(wyvern, 0, 3)


			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern_coords = level_one.coords(wyvern)

			#Aparición del agujero negro
			hole_spawn()
			hole_box = level_one.bbox(hole)
			hole_coords = level_one.coords(hole)
			level_one.move(hole, 0, 3)

			#Colisión con el agujero negro
			if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 404:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 4
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 464:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 4
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_box = level_one.bbox(ball)
			level_one.move(ball, 0, 3)
			#Colisión con la energy ball
			if 3 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy = energy + 10
				eneg.config(text=int(energy))
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			level_one.move(hyper, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			#Movimiento de cambio de carril

			if level_one.coords(hyper) > [404, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 404 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 457:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [464, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 464 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 457:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [404, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 404 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [464, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 464 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy = energy - 0.01
			eneg.config(text=int(energy))
			speed.config(text=str(velocidad)+"Km/s")

			
			#Colisión con Wyvern
			if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy = energy - 6
				eneg.config(text=int(energy))
				if level_one.coords(goldenfox)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [392, 501] or level_one.coords(goldenfox) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox
			elif 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy = energy - 6
				eneg.config(text=int(energy))
				if level_one.coords(wyvern)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [392, 501] or level_one.coords(wyvern) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder
			elif 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy = energy - 6
				eneg.config(text=int(energy))
				if level_one.coords(hyper)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [392, 501] or level_one.coords(hyper) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Conteo de la puntuación
			elif falc_coords[1] == wyvern_coords[1]:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif hyper_coords[1] == 502:
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [392, 501] or level_one.coords(falc) >= [469, 501]:
				energy = energy - 25
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)

		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			level5_1p()
		elif energy == 0:
			loser = level_one.create_image(0, 0, image=los, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			menu()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 438, 501)
	level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

def level5_1p():
	global nombre_p1
	global init
	global energy
	global wyvern
	global wyvern_box
	global goldenfox
	global hyper
	global ball
	global hole
	global cargado

	#Función para guardar partida
	def save_game():
		global nombre_p1
		global energy
		global puntos_1p
		global coordenadas_juego
		guardado = open("save.txt", "w")
		lista_guardado = [str(nombre_p1), " ", str(energy), " ", str(puntos_1p), " ", str(coordenadas_juego_l1), " ", "lvl_5"]
		guardado.writelines(lista_guardado)
		guardado.close()
	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space5.jpg")
	bandas = Image.open("bandas.png")
	falcon = Image.open("falcon.png")
	nombre_p1 = nombre_p1.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(234, -18984, image=espacio.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(428, 501, image=falcon.jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("youwin.png")
	win = ImageTk.PhotoImage(w)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[404, -90], [464, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(0, 602, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 2000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[404, -350], [464, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 2756:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[404, -128], [464, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[404, -128], [464, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 4000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[404, -128], [464, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole = level_one.create_image(0, 600, image=ho, anchor="nw")

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
	def desacelerar():
		global velocidad
		velocidad = velocidad - 1
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	level_one.bind_all("<KeyPress-Up>", accelerate)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
			p_selecter = level_one.create_image(97, 158, image=pause_selecter, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
	#Imagen del seleccionador
	ps = Image.open("seleccionador.png")
	pause_selecter = ImageTk.PhotoImage(ps)
	#Función para el movimiento del seleccionador
	def move_down_pause(event):
		global p_selecter
		if level_one.coords(p_selecter) < [97, 418] and level_one.coords(p_selecter) >= [97, 158]:
			level_one.move(p_selecter, 0, 130)
		elif level_one.coords(p_selecter) == [97, 418]:
			level_one.coords(p_selecter, 97, 158)
	#Imagen para el guardado
	s = Image.open("saved.png")
	sv = ImageTk.PhotoImage(s)
	saved = level_one.create_image(0, 700, image=sv, anchor="nw")
	#Evento al presionar la tecla "enter"
	def eleccion_menu_pausa(event):
		global p_selecter
		global pausado
		if level_one.coords(p_selecter) == [97, 158]:
			pausado = False
			level_one.delete(ventana_pausa)
			level_one.delete(p_selecter)
			level_one.delete(saved)
			juego()
		elif level_one.coords(p_selecter) == [97, 288]:
			save_game()
			saved = level_one.create_image(0, 0, image=sv, anchor="nw")
		elif level_one.coords(p_selecter) == [97, 418]:
			level1.destroy()
			menu()
	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)
	level_one.bind_all("<KeyPress-Down>", move_down_pause)
	level_one.bind_all("<KeyPress-Return>", eleccion_menu_pausa)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=830, y=427)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=784, y=353)

	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=784, y=234)

	#Puntuación
	puntos = Label(level_one, text=puntos_1p, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=784, y=138)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy
		global wyvern
		global wyvern_box
		global puntos_1p
		global goldenfox
		global cambio
		global hyper
		global ball
		global hole
		global velocidad
		global coordenadas_juego

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 438, level_one.coords(falc)[1])
		#Se crea el enemigo wyvern
		while start == True and energy > 0 and pausado == False and level_one.coords(space)[1] < 1: 
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			level_one.after(5000, wyvern_spawn)
			level_one.move(space, 0, velocidad/70)
			level_one.move(wyvern, 0, 3)


			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern_coords = level_one.coords(wyvern)

			#Aparición del agujero negro
			hole_spawn()
			hole_box = level_one.bbox(hole)
			hole_coords = level_one.coords(hole)
			level_one.move(hole, 0, 3)

			#Colisión con el agujero negro
			if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 404:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 5
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 464:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 5
						level_one.update()
						time.sleep(0.01)
						if 3 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_box = level_one.bbox(ball)
			level_one.move(ball, 0, 3)
			#Colisión con la energy ball
			if 3 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy = energy + 5
				eneg.config(text=int(energy))
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			level_one.move(hyper, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			#Movimiento de cambio de carril

			if level_one.coords(hyper) > [404, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 404 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 457:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [464, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 464 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 457:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [404, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 404 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [464, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 464 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy = energy - 0.01
			eneg.config(text=int(energy))
			speed.config(text=str(velocidad)+"Km/s")

			
			#Colisión con Wyvern
			if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy = energy - 10
				eneg.config(text=int(energy))
				if level_one.coords(goldenfox)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [392, 501] or level_one.coords(goldenfox) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox
			elif 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy = energy - 10
				eneg.config(text=int(energy))
				if level_one.coords(wyvern)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [392, 501] or level_one.coords(wyvern) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder
			elif 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy = energy - 10
				eneg.config(text=int(energy))
				if level_one.coords(hyper)[0] == 404:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 464:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [392, 501] or level_one.coords(hyper) >= [469, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 3 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Conteo de la puntuación
			elif falc_coords[1] == wyvern_coords[1]:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos_1p += 50
				puntos.config(text=str(puntos_1p)+"pts")

			elif hyper_coords[1] == 502:
				puntos_1p += 100
				puntos.config(text=str(puntos_1p)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [392, 501] or level_one.coords(falc) >= [469, 501]:
				energy = energy - 30
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)

		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			menu()
		elif energy == 0:
			loser = level_one.create_image(0, 0, image=los, anchor="nw")
			time.sleep(1)
			level_one.update()
			level1.destroy()
			menu()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 438, 501)
	level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

#CÓDIGO PARA EL MODO DOS JUGADORES

def nombre_2p():
	global nombre1
	global nombre2
	#Evento para la aparición de la insturcción
	def siguiente(event):
		global contador2
		if contador2 == 1:
			press_enter = nameground.create_image(0, 0, image=p_enter, anchor="nw")
			contador2 = 2
	#Declaración de la variables que se utilizarán en el canvas
	question = Image.open("question2p.png")
	press = Image.open("press enter.png")
	#Generar la ventana
	nombre2p = Tk()
	nombre2p.geometry("800x600")
	nombre2p.title("Space Road")
	nombre2p.resizable(0,0)
	nombre2p.focus_force()
	#Generar Canvas
	nameground = Canvas(nombre2p, width=800, height=600)
	nameground.place(x=0, y=0)
	#Integrar fondo al canvas
	nameground.fondo = ImageTk.PhotoImage(question)
	nameground.create_image(0, 0, image=nameground.fondo, anchor="nw")
	#Añadir caja de texto al canvas
	nombre1 = StringVar()
	name = Entry(nameground, textvariable=nombre1, bg="#3c115e", bd=0, fg="#94d0ff", font="System 42", width=13, justify=CENTER)
	name.place(x=180, y=196)
	#Añadir caja de texto al canvas
	nombre2 = StringVar()
	name = Entry(nameground, textvariable=nombre2, bg="#3c115e", bd=0, fg="#94d0ff", font="System 42", width=13, justify=CENTER)
	name.place(x=180, y=343)
	#Pasar el nombre a la variable global
	#Añadir imagen de instrucción
	p_enter = ImageTk.PhotoImage(press)
	#Definición de la función para pasar a la ventana de niveles
	def pasar(event):
		global contador2
		contador2 = 1
		nombre2p.destroy()
		nivel_2p()
	#Evento para continuar
	nameground.bind_all("<Key>", siguiente)
	nameground.bind_all("<KeyPress-Return>", pasar)
	nombre2p.mainloop()

def nivel_2p():
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
			niveles.destroy()
			level1_2p()
		elif levelground.coords(selecter) == [198, 262]:
			niveles.destroy()
			level2_2p()
		elif levelground.coords(selecter) == [198, 333]:
			niveles.destroy()
			level3_2p()
		elif levelground.coords(selecter) == [198, 404]:
			niveles.destroy()
			level4_2p()
		elif levelground.coords(selecter) == [198, 475]:
			niveles.destroy()
			level5_2p()
	#Declaración de las variables que se utilizarán en el canvas
	fondo = fondo.resize((800, 600))
	levels = Image.open("levels.png")
	seleccionador = Image.open("seleccionador.png")
	#Generar la ventana
	niveles = Tk()
	niveles.geometry("800x600")
	niveles.title("Space Road")
	niveles.resizable(0,0)
	niveles.focus_force()
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

def level1_2p():
	global nombre1
	global nombre2
	global init
	global energy1
	global energy2
	global wyvern
	global wyvern_box
	global wyvern2
	global goldenfox
	global goldenfox2
	global hyper
	global hyper2
	global ball
	global ball2
	global hole
	global hole2
	global cargado
	global velocidad2
	global puntos1
	global puntos2


	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space.jpg")
	espacio2 = Image.open("space1_2.jpg")
	bandas = Image.open("separador.png")
	falcon = Image.open("falcon.png")
	nombre1 = nombre1.get()
	nombre2 = nombre2.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(0, -18984, image=espacio.fondo, anchor="nw")
	#Integrar el fondo2
	espacio2.fondo = ImageTk.PhotoImage(espacio2)
	space2 = level_one.create_image(520, -18984, image=espacio2.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(199, 501, image=falcon.jugador, anchor="nw")
	#Integrar jugador2 al canvas
	f = Image.open("fire.png")
	fire_jugador = ImageTk.PhotoImage(f)
	fire = level_one.create_image(782, 501, image=fire_jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("win-lose.png")
	win_lose = ImageTk.PhotoImage(w)
	l = Image.open("lose-win.png")
	lose_win = ImageTk.PhotoImage(l)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(168, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar el enemigo con velocidad constante (Wyvern) 2
	def wyvern_spawn2():
		global wyvern2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)
		elif resultado == "si" and level_one.coords(wyvern2)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)

	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern2 = level_one.create_image(787, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern2)


	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemigo que cambia de carril aleatoriamente 2
	def goldenfox_spawn2():
		global goldenfox2
		global cambio2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False
		elif resultado_gf == "si" and level_one.coords(goldenfox2)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox2 = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar al enemgio que sigue al jugador

	def hyper_spawn2():
		global hyper2
		global cambio_hyper2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False
		elif resultado_hy == "si" and level_one.coords(hyper2)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper2 = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 8000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar la energy ball (carro gasolina)

	def ball_spawn2():
		global ball2
		global ball2_box
		global ball2_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball2)[1] > 8000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball2 = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 10000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		else:
			hole = level_one.create_image(0, 1000, image=ho, anchor="nw")

	def hole_spawn2():
		global hole2
		global hole2_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)
		elif aparecer_hole == 4 and level_one.coords(hole2)[1] > 10000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole2 = level_one.create_image(0, 600, image=ho, anchor="nw")

	#Intergrar el nombre del jugador a la pantalla
	name = Label(level_one, text=nombre1, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=340, y=88)
	#Intergrar el nombre del jugador2 a la pantalla
	name = Label(level_one, text=nombre2, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=539, y=88)
	#Movimiento del jugador
	distancia = 5
	movimientos = {
		"left" : (-distancia, 0),
		"right" : (distancia, 0),
		"a" : (-distancia, 0),
		"d" : (distancia, 0)
		}
	def move_press1(event):
		if level_one.coords(falc) >= [161, 501] and level_one.coords(falc) <= [235, 501]:
			key = (event.keysym).lower()
			level_one.move(falc, * movimientos[key])
	def move_press2(event):
		key = (event.keysym).lower()
		level_one.move(fire, * movimientos[key])
	level_one.bind_all("<KeyPress-Left>", move_press2)
	level_one.bind_all("<KeyPress-Right>", move_press2)
	level_one.bind_all("<KeyPress-a>", move_press1)
	level_one.bind_all("<KeyPress-d>", move_press1)
	#Movimiento de la carretera
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	#Movimiento de la carretera2
	def accelerate2(event):
		global velocidad2
		if velocidad2 < 300:
			velocidad2 = velocidad2 + 10
	def deaccelerate2(event): 
		global velocidad2
		while velocidad2 > 0 and velocidad2 <= 300:
			velocidad2 = velocidad2 - 1
	level_one.bind_all("<KeyPress-Up>", accelerate2)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate2)
	level_one.bind_all("<KeyPress-w>", accelerate)
	level_one.bind_all("<KeyRelease-w>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa2p.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			juego()

	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy1, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=340, y=482)

	#Declaración de la energía de la nave2
	eneg2 = Label(level_one, text=energy2, bg="black", fg="#4cffb5", font=("System", 30))
	eneg2.place(x=560, y=482)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=339, y=402)

	#Label para el título "Energy"
	energia_lab2 = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab2.place(x=544, y=402)


	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=335, y=197)

	#Mostrar la velocidad en pantalla 2
	speed2 = Label(level_one, text=velocidad2, bg="black", fg="#4cffb5", font=("System", 30))
	speed2.place(x=531, y=197)

	#Puntuación
	puntos = Label(level_one, text=puntos1, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=334, y=299)

	#Puntuación
	puntos_2p = Label(level_one, text=puntos2, bg="black", fg="#4cffb5", font=("System", 30))
	puntos_2p.place(x=529, y=299)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy1
		global energy2
		global wyvern
		global wyvern2
		global wyvern_box
		global wyvern2_box
		global puntos_1p
		global goldenfox
		global goldenfox2
		global cambio
		global cambio2
		global hyper
		global hyper2
		global ball
		global ball2
		global hole
		global hole2
		global velocidad
		global velocidad2
		global coordenadas_juego
		global puntos1
		global puntos2

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 198, level_one.coords(falc)[1])
		level_one.coords(fire, 817, level_one.coords(fire)[1])
		#Se crea el enemigo wyvern
		while start == True and energy1 > 0 and energy2 > 0 and pausado == False and level_one.coords(space)[1] < 1 and level_one.coords(space2)[1] < 1:
			fire_coords = level_one.coords(fire)
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			fire_box = level_one.bbox(fire)
			level_one.after(5000, wyvern_spawn)
			level_one.after(5000, wyvern_spawn2)
			level_one.move(space, 0, velocidad/70)
			level_one.move(space2, 0, velocidad2/70)
			level_one.move(wyvern, 0, 3)
			level_one.move(wyvern2, 0, 3)

			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern2_box = level_one.bbox(wyvern2)
			wyvern_coords = level_one.coords(wyvern)
			wyvern2_coords = level_one.coords(wyvern2)

			#Aparición del agujero negro
			hole_spawn()
			hole_spawn2()
			hole_box = level_one.bbox(hole)
			hole2_box = level_one.bbox(hole2)
			hole_coords = level_one.coords(hole)
			hole2_coords = level_one.coords(hole2)
			level_one.move(hole, 0, 3)
			level_one.move(hole2, 0, 3)

			#Colisión con el agujero negro
			if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 168:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 1
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 227:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 1
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)
			#Colisión con el agujero negro 2
			if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
				if hole2_coords[0] == 787:
					for x in range(10):
						level_one.move(fire, (velocidad+3)/100, 0)
						velocidad2 -= 1
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole2_coords[0] == 227:
					for x in range(10):
						level_one.move(fire, -(velocidad+3)/100, 0)
						velocidad2 -= 1
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_spawn2()
			ball_box = level_one.bbox(ball)
			ball2_box = level_one.bbox(ball2)
			level_one.move(ball, 0, 3)
			level_one.move(ball2, 0, 3)
			#Colisión con la energy ball
			if 4 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy1 = energy1 + 50
				eneg.config(text=int(energy1))
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")
			if 5 in level_one.find_overlapping(ball2_box[0], ball2_box[1], ball2_box[2], ball2_box[3]):
				level_one.coords(ball2, 0, 600)
				energy2 = energy2 + 50
				eneg2.config(text=int(energy2))
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			hyper_spawn2()
			level_one.move(hyper, 0, 3)
			level_one.move(hyper2, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			hyper2_coords = level_one.coords(hyper2)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			hyper2_box = level_one.bbox(hyper2)
			#Movimiento de cambio de carril
			if level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 168 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 197:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 227 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 197:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento de cambio de carril 2
			if level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 787 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] > 850:
					for x in range(12):
						level_one.move(hyper2, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 847 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] < 850:
					for x in range(12):
						level_one.move(hyper2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			level_one.after(5000, goldenfox_spawn2)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			goldenfox2_coords = level_one.coords(goldenfox2)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			fox2_box = level_one.bbox(goldenfox2)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 168 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 227 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento y cambio de carril de golden fox 2
			level_one.move(goldenfox2, 0, 3)
			if level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 787 and cambio2 == False:
				cambio2 = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox2, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 847 and cambio2 == False:
				cambio2 = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy1 = energy1 - 0.01
			energy2 = energy2 - 0.01
			eneg.config(text=int(energy1))
			eneg2.config(text=int(energy2))
			speed.config(text=str(velocidad)+"Km/s")
			speed2.config(text=str(velocidad2)+"Km/s")

			
			#Colisión con Golden Fox
			if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy1 = energy1 - 2
				eneg.config(text=int(energy1))
				if level_one.coords(goldenfox)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [161, 501] or level_one.coords(goldenfox) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)



			#Colisión con Hyper Speeder
			elif 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy1 = energy1 - 2
				eneg.config(text=int(energy1))
				if level_one.coords(hyper)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [161, 501] or level_one.coords(hyper) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Colisión con Wyvern
			elif 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy1 = energy1 - 2
				eneg.config(text=int(energy1))
				if level_one.coords(wyvern)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [161, 501] or level_one.coords(wyvern) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 1
			elif falc_coords[1] == wyvern_coords[1]:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif hyper_coords[1] == 502:
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")


			#Colisión con Wyvern 2
			if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
				energy2 = energy2 - 2
				eneg2.config(text=int(energy2))
				if level_one.coords(wyvern2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(wyvern2, -velocidad/10, 0)
				elif level_one.coords(wyvern2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(wyvern2, velocidad/10, 0)
				if level_one.coords(wyvern2) < [777, 501] or level_one.coords(wyvern2) > [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern2_coords[0], wyvern2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
					for x in range(10):
						level_one.move(wyvern2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox 2
			elif 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
				energy2 = energy2 - 2
				eneg2.config(text=int(energy2))
				if level_one.coords(goldenfox2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(goldenfox2, -velocidad/10, 0)
				elif level_one.coords(goldenfox2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(goldenfox2, velocidad/10, 0)
				if level_one.coords(goldenfox2) <= [777, 501] or level_one.coords(goldenfox2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox2_coords[0], goldenfox2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
					for x in range(10):
						level_one.move(goldenfox2, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder2
			elif 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
				energy2 = energy2 - 2
				eneg2.config(text=int(energy2))
				if level_one.coords(hyper2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(hyper2, -velocidad/10, 0)
				elif level_one.coords(hyper2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(hyper2, velocidad/10, 0)
				if level_one.coords(hyper2) <= [777, 501] or level_one.coords(hyper2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper2_coords[0], hyper2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
					for x in range(10):
						level_one.move(hyper2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 2
			elif fire_coords[1] == wyvern_coords[1]:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif goldenfox2_coords[1] == 502:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif hyper2_coords[1] == 502:
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [161, 501] or level_one.coords(falc) >= [235, 501]:
				energy1 = energy1 - 10
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


			#Colisión con los límites de la carretera fire
			if level_one.coords(fire) <= [777, 501] or level_one.coords(fire) >= [852, 501]:
				energy2 = energy2 - 10
				for x in range(len(list_explos)):
					explos = level_one.create_image(fire_coords[0], fire_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif level_one.coords(space2)[1] >= 1:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy1 <= 0:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy2 <= 0:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 168, 501)
	#level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

def level2_2p():
	global nombre1
	global nombre2
	global init
	global energy1
	global energy2
	global wyvern
	global wyvern_box
	global wyvern2
	global goldenfox
	global goldenfox2
	global hyper
	global hyper2
	global ball
	global ball2
	global hole
	global hole2
	global cargado
	global velocidad2
	global puntos1
	global puntos2


	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space2.jpg")
	espacio2 = Image.open("space2_2.jpg")
	bandas = Image.open("separador.png")
	falcon = Image.open("falcon.png")
	nombre1 = nombre1.get()
	nombre2 = nombre2.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(0, -18984, image=espacio.fondo, anchor="nw")
	#Integrar el fondo2
	espacio2.fondo = ImageTk.PhotoImage(espacio2)
	space2 = level_one.create_image(520, -18984, image=espacio2.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(199, 501, image=falcon.jugador, anchor="nw")
	#Integrar jugador2 al canvas
	f = Image.open("fire.png")
	fire_jugador = ImageTk.PhotoImage(f)
	fire = level_one.create_image(782, 501, image=fire_jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("win-lose.png")
	win_lose = ImageTk.PhotoImage(w)
	l = Image.open("lose-win.png")
	lose_win = ImageTk.PhotoImage(l)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(168, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar el enemigo con velocidad constante (Wyvern) 2
	def wyvern_spawn2():
		global wyvern2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)
		elif resultado == "si" and level_one.coords(wyvern2)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)

	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern2 = level_one.create_image(787, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern2)


	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemigo que cambia de carril aleatoriamente 2
	def goldenfox_spawn2():
		global goldenfox2
		global cambio2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False
		elif resultado_gf == "si" and level_one.coords(goldenfox2)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox2 = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 4000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar al enemgio que sigue al jugador

	def hyper_spawn2():
		global hyper2
		global cambio_hyper2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False
		elif resultado_hy == "si" and level_one.coords(hyper2)[1] > 4000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper2 = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar la energy ball (carro gasolina)

	def ball_spawn2():
		global ball2
		global ball2_box
		global ball2_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball2)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball2 = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 8000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		else:
			hole = level_one.create_image(0, 1000, image=ho, anchor="nw")

	def hole_spawn2():
		global hole2
		global hole2_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)
		elif aparecer_hole == 4 and level_one.coords(hole2)[1] > 8000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole2 = level_one.create_image(0, 600, image=ho, anchor="nw")

	#Intergrar el nombre del jugador a la pantalla
	name = Label(level_one, text=nombre1, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=340, y=88)
	#Intergrar el nombre del jugador2 a la pantalla
	name = Label(level_one, text=nombre2, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=539, y=88)
	#Movimiento del jugador
	distancia = 5
	movimientos = {
		"left" : (-distancia, 0),
		"right" : (distancia, 0),
		"a" : (-distancia, 0),
		"d" : (distancia, 0)
		}
	def move_press1(event):
		if level_one.coords(falc) >= [161, 501] and level_one.coords(falc) <= [235, 501]:
			key = (event.keysym).lower()
			level_one.move(falc, * movimientos[key])
	def move_press2(event):
		key = (event.keysym).lower()
		level_one.move(fire, * movimientos[key])
	level_one.bind_all("<KeyPress-Left>", move_press2)
	level_one.bind_all("<KeyPress-Right>", move_press2)
	level_one.bind_all("<KeyPress-a>", move_press1)
	level_one.bind_all("<KeyPress-d>", move_press1)
	#Movimiento de la carretera
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	#Movimiento de la carretera2
	def accelerate2(event):
		global velocidad2
		if velocidad2 < 300:
			velocidad2 = velocidad2 + 10
	def deaccelerate2(event): 
		global velocidad2
		while velocidad2 > 0 and velocidad2 <= 300:
			velocidad2 = velocidad2 - 1
	level_one.bind_all("<KeyPress-Up>", accelerate2)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate2)
	level_one.bind_all("<KeyPress-w>", accelerate)
	level_one.bind_all("<KeyRelease-w>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa2p.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			juego()

	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy1, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=340, y=482)

	#Declaración de la energía de la nave2
	eneg2 = Label(level_one, text=energy2, bg="black", fg="#4cffb5", font=("System", 30))
	eneg2.place(x=560, y=482)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=339, y=402)

	#Label para el título "Energy"
	energia_lab2 = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab2.place(x=544, y=402)


	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=335, y=197)

	#Mostrar la velocidad en pantalla 2
	speed2 = Label(level_one, text=velocidad2, bg="black", fg="#4cffb5", font=("System", 30))
	speed2.place(x=531, y=197)

	#Puntuación
	puntos = Label(level_one, text=puntos1, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=334, y=299)

	#Puntuación
	puntos_2p = Label(level_one, text=puntos2, bg="black", fg="#4cffb5", font=("System", 30))
	puntos_2p.place(x=529, y=299)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy1
		global energy2
		global wyvern
		global wyvern2
		global wyvern_box
		global wyvern2_box
		global puntos_1p
		global goldenfox
		global goldenfox2
		global cambio
		global cambio2
		global hyper
		global hyper2
		global ball
		global ball2
		global hole
		global hole2
		global velocidad
		global velocidad2
		global coordenadas_juego
		global puntos1
		global puntos2

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 198, level_one.coords(falc)[1])
		level_one.coords(fire, 817, level_one.coords(fire)[1])
		#Se crea el enemigo wyvern
		while start == True and energy1 > 0 and energy2 > 0 and pausado == False and level_one.coords(space)[1] < 1 and level_one.coords(space2)[1] < 1:
			fire_coords = level_one.coords(fire)
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			fire_box = level_one.bbox(fire)
			level_one.after(5000, wyvern_spawn)
			level_one.after(5000, wyvern_spawn2)
			level_one.move(space, 0, velocidad/70)
			level_one.move(space2, 0, velocidad2/70)
			level_one.move(wyvern, 0, 3)
			level_one.move(wyvern2, 0, 3)

			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern2_box = level_one.bbox(wyvern2)
			wyvern_coords = level_one.coords(wyvern)
			wyvern2_coords = level_one.coords(wyvern2)

			#Aparición del agujero negro
			hole_spawn()
			hole_spawn2()
			hole_box = level_one.bbox(hole)
			hole2_box = level_one.bbox(hole2)
			hole_coords = level_one.coords(hole)
			hole2_coords = level_one.coords(hole2)
			level_one.move(hole, 0, 3)
			level_one.move(hole2, 0, 3)

			#Colisión con el agujero negro
			if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 168:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 2
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 227:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 2
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)
			#Colisión con el agujero negro 2
			if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
				if hole2_coords[0] == 787:
					for x in range(10):
						level_one.move(fire, (velocidad+3)/100, 0)
						velocidad2 -= 2
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole2_coords[0] == 227:
					for x in range(10):
						level_one.move(fire, -(velocidad+3)/100, 0)
						velocidad2 -= 2
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_spawn2()
			ball_box = level_one.bbox(ball)
			ball2_box = level_one.bbox(ball2)
			level_one.move(ball, 0, 3)
			level_one.move(ball2, 0, 3)
			#Colisión con la energy ball
			if 4 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy1 = energy1 + 40
				eneg.config(text=int(energy1))
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")
			if 5 in level_one.find_overlapping(ball2_box[0], ball2_box[1], ball2_box[2], ball2_box[3]):
				level_one.coords(ball2, 0, 600)
				energy2 = energy2 + 40
				eneg2.config(text=int(energy2))
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			hyper_spawn2()
			level_one.move(hyper, 0, 3)
			level_one.move(hyper2, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			hyper2_coords = level_one.coords(hyper2)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			hyper2_box = level_one.bbox(hyper2)
			#Movimiento de cambio de carril
			if level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 168 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 197:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 227 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 197:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento de cambio de carril 2
			if level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 787 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] > 850:
					for x in range(12):
						level_one.move(hyper2, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 847 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] < 850:
					for x in range(12):
						level_one.move(hyper2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			level_one.after(5000, goldenfox_spawn2)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			goldenfox2_coords = level_one.coords(goldenfox2)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			fox2_box = level_one.bbox(goldenfox2)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 168 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 227 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento y cambio de carril de golden fox 2
			level_one.move(goldenfox2, 0, 3)
			if level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 787 and cambio2 == False:
				cambio2 = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox2, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 847 and cambio2 == False:
				cambio2 = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy1 = energy1 - 0.01
			energy2 = energy2 - 0.01
			eneg.config(text=int(energy1))
			eneg2.config(text=int(energy2))
			speed.config(text=str(velocidad)+"Km/s")
			speed2.config(text=str(velocidad2)+"Km/s")

			
			#Colisión con Golden Fox
			if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy1 = energy1 - 4
				eneg.config(text=int(energy1))
				if level_one.coords(goldenfox)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [161, 501] or level_one.coords(goldenfox) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)



			#Colisión con Hyper Speeder
			elif 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy1 = energy1 - 4
				eneg.config(text=int(energy1))
				if level_one.coords(hyper)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [161, 501] or level_one.coords(hyper) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Colisión con Wyvern
			elif 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy1 = energy1 - 4
				eneg.config(text=int(energy1))
				if level_one.coords(wyvern)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [161, 501] or level_one.coords(wyvern) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 1
			elif falc_coords[1] == wyvern_coords[1]:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif hyper_coords[1] == 502:
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")


			#Colisión con Wyvern 2
			if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
				energy2 = energy2 - 4
				eneg2.config(text=int(energy2))
				if level_one.coords(wyvern2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(wyvern2, -velocidad/10, 0)
				elif level_one.coords(wyvern2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(wyvern2, velocidad/10, 0)
				if level_one.coords(wyvern2) < [777, 501] or level_one.coords(wyvern2) > [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern2_coords[0], wyvern2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
					for x in range(10):
						level_one.move(wyvern2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox 2
			elif 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
				energy2 = energy2 - 4
				eneg2.config(text=int(energy2))
				if level_one.coords(goldenfox2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(goldenfox2, -velocidad/10, 0)
				elif level_one.coords(goldenfox2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(goldenfox2, velocidad/10, 0)
				if level_one.coords(goldenfox2) <= [777, 501] or level_one.coords(goldenfox2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox2_coords[0], goldenfox2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
					for x in range(10):
						level_one.move(goldenfox2, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder2
			elif 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
				energy2 = energy2 - 4
				eneg2.config(text=int(energy2))
				if level_one.coords(hyper2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(hyper2, -velocidad/10, 0)
				elif level_one.coords(hyper2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(hyper2, velocidad/10, 0)
				if level_one.coords(hyper2) <= [777, 501] or level_one.coords(hyper2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper2_coords[0], hyper2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
					for x in range(10):
						level_one.move(hyper2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 2
			elif fire_coords[1] == wyvern_coords[1]:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif goldenfox2_coords[1] == 502:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif hyper2_coords[1] == 502:
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [161, 501] or level_one.coords(falc) >= [235, 501]:
				energy1 = energy1 - 15
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


			#Colisión con los límites de la carretera fire
			if level_one.coords(fire) <= [777, 501] or level_one.coords(fire) >= [852, 501]:
				energy2 = energy2 - 15
				for x in range(len(list_explos)):
					explos = level_one.create_image(fire_coords[0], fire_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif level_one.coords(space2)[1] >= 1:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy1 <= 0:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy2 <= 0:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 168, 501)
	#level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

def level3_2p():
	global nombre1
	global nombre2
	global init
	global energy1
	global energy2
	global wyvern
	global wyvern_box
	global wyvern2
	global goldenfox
	global goldenfox2
	global hyper
	global hyper2
	global ball
	global ball2
	global hole
	global hole2
	global cargado
	global velocidad2
	global puntos1
	global puntos2


	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space3.jpg")
	espacio2 = Image.open("space3_2.jpg")
	bandas = Image.open("separador.png")
	falcon = Image.open("falcon.png")
	nombre1 = nombre1.get()
	nombre2 = nombre2.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(0, -18984, image=espacio.fondo, anchor="nw")
	#Integrar el fondo2
	espacio2.fondo = ImageTk.PhotoImage(espacio2)
	space2 = level_one.create_image(520, -18984, image=espacio2.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(199, 501, image=falcon.jugador, anchor="nw")
	#Integrar jugador2 al canvas
	f = Image.open("fire.png")
	fire_jugador = ImageTk.PhotoImage(f)
	fire = level_one.create_image(782, 501, image=fire_jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("win-lose.png")
	win_lose = ImageTk.PhotoImage(w)
	l = Image.open("lose-win.png")
	lose_win = ImageTk.PhotoImage(l)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(168, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar el enemigo con velocidad constante (Wyvern) 2
	def wyvern_spawn2():
		global wyvern2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)
		elif resultado == "si" and level_one.coords(wyvern2)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)

	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern2 = level_one.create_image(787, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern2)


	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 2000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemigo que cambia de carril aleatoriamente 2
	def goldenfox_spawn2():
		global goldenfox2
		global cambio2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False
		elif resultado_gf == "si" and level_one.coords(goldenfox2)[1] > 2000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox2 = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar al enemgio que sigue al jugador

	def hyper_spawn2():
		global hyper2
		global cambio_hyper2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False
		elif resultado_hy == "si" and level_one.coords(hyper2)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper2 = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 4000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar la energy ball (carro gasolina)

	def ball_spawn2():
		global ball2
		global ball2_box
		global ball2_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball2)[1] > 4000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball2 = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		else:
			hole = level_one.create_image(0, 1000, image=ho, anchor="nw")

	def hole_spawn2():
		global hole2
		global hole2_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)
		elif aparecer_hole == 4 and level_one.coords(hole2)[1] > 5000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole2 = level_one.create_image(0, 600, image=ho, anchor="nw")

	#Intergrar el nombre del jugador a la pantalla
	name = Label(level_one, text=nombre1, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=340, y=88)
	#Intergrar el nombre del jugador2 a la pantalla
	name = Label(level_one, text=nombre2, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=539, y=88)
	#Movimiento del jugador
	distancia = 5
	movimientos = {
		"left" : (-distancia, 0),
		"right" : (distancia, 0),
		"a" : (-distancia, 0),
		"d" : (distancia, 0)
		}
	def move_press1(event):
		if level_one.coords(falc) >= [161, 501] and level_one.coords(falc) <= [235, 501]:
			key = (event.keysym).lower()
			level_one.move(falc, * movimientos[key])
	def move_press2(event):
		key = (event.keysym).lower()
		level_one.move(fire, * movimientos[key])
	level_one.bind_all("<KeyPress-Left>", move_press2)
	level_one.bind_all("<KeyPress-Right>", move_press2)
	level_one.bind_all("<KeyPress-a>", move_press1)
	level_one.bind_all("<KeyPress-d>", move_press1)
	#Movimiento de la carretera
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	#Movimiento de la carretera2
	def accelerate2(event):
		global velocidad2
		if velocidad2 < 300:
			velocidad2 = velocidad2 + 10
	def deaccelerate2(event): 
		global velocidad2
		while velocidad2 > 0 and velocidad2 <= 300:
			velocidad2 = velocidad2 - 1
	level_one.bind_all("<KeyPress-Up>", accelerate2)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate2)
	level_one.bind_all("<KeyPress-w>", accelerate)
	level_one.bind_all("<KeyRelease-w>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa2p.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			juego()

	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy1, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=340, y=482)

	#Declaración de la energía de la nave2
	eneg2 = Label(level_one, text=energy2, bg="black", fg="#4cffb5", font=("System", 30))
	eneg2.place(x=560, y=482)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=339, y=402)

	#Label para el título "Energy"
	energia_lab2 = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab2.place(x=544, y=402)


	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=335, y=197)

	#Mostrar la velocidad en pantalla 2
	speed2 = Label(level_one, text=velocidad2, bg="black", fg="#4cffb5", font=("System", 30))
	speed2.place(x=531, y=197)

	#Puntuación
	puntos = Label(level_one, text=puntos1, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=334, y=299)

	#Puntuación
	puntos_2p = Label(level_one, text=puntos2, bg="black", fg="#4cffb5", font=("System", 30))
	puntos_2p.place(x=529, y=299)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy1
		global energy2
		global wyvern
		global wyvern2
		global wyvern_box
		global wyvern2_box
		global puntos_1p
		global goldenfox
		global goldenfox2
		global cambio
		global cambio2
		global hyper
		global hyper2
		global ball
		global ball2
		global hole
		global hole2
		global velocidad
		global velocidad2
		global coordenadas_juego
		global puntos1
		global puntos2

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 198, level_one.coords(falc)[1])
		level_one.coords(fire, 817, level_one.coords(fire)[1])
		#Se crea el enemigo wyvern
		while start == True and energy1 > 0 and energy2 > 0 and pausado == False and level_one.coords(space)[1] < 1 and level_one.coords(space2)[1] < 1:
			fire_coords = level_one.coords(fire)
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			fire_box = level_one.bbox(fire)
			level_one.after(5000, wyvern_spawn)
			level_one.after(5000, wyvern_spawn2)
			level_one.move(space, 0, velocidad/70)
			level_one.move(space2, 0, velocidad2/70)
			level_one.move(wyvern, 0, 3)
			level_one.move(wyvern2, 0, 3)

			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern2_box = level_one.bbox(wyvern2)
			wyvern_coords = level_one.coords(wyvern)
			wyvern2_coords = level_one.coords(wyvern2)

			#Aparición del agujero negro
			hole_spawn()
			hole_spawn2()
			hole_box = level_one.bbox(hole)
			hole2_box = level_one.bbox(hole2)
			hole_coords = level_one.coords(hole)
			hole2_coords = level_one.coords(hole2)
			level_one.move(hole, 0, 3)
			level_one.move(hole2, 0, 3)

			#Colisión con el agujero negro
			if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 168:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 2
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 227:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 2
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)
			#Colisión con el agujero negro 2
			if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
				if hole2_coords[0] == 787:
					for x in range(10):
						level_one.move(fire, (velocidad+3)/100, 0)
						velocidad2 -= 2
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole2_coords[0] == 227:
					for x in range(10):
						level_one.move(fire, -(velocidad+3)/100, 0)
						velocidad2 -= 2
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_spawn2()
			ball_box = level_one.bbox(ball)
			ball2_box = level_one.bbox(ball2)
			level_one.move(ball, 0, 3)
			level_one.move(ball2, 0, 3)
			#Colisión con la energy ball
			if 4 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy1 = energy1 + 20
				eneg.config(text=int(energy1))
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")
			if 5 in level_one.find_overlapping(ball2_box[0], ball2_box[1], ball2_box[2], ball2_box[3]):
				level_one.coords(ball2, 0, 600)
				energy2 = energy2 + 20
				eneg2.config(text=int(energy2))
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			hyper_spawn2()
			level_one.move(hyper, 0, 3)
			level_one.move(hyper2, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			hyper2_coords = level_one.coords(hyper2)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			hyper2_box = level_one.bbox(hyper2)
			#Movimiento de cambio de carril
			if level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 168 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 197:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 227 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 197:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento de cambio de carril 2
			if level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 787 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] > 850:
					for x in range(12):
						level_one.move(hyper2, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 847 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] < 850:
					for x in range(12):
						level_one.move(hyper2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			level_one.after(5000, goldenfox_spawn2)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			goldenfox2_coords = level_one.coords(goldenfox2)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			fox2_box = level_one.bbox(goldenfox2)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 168 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 227 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento y cambio de carril de golden fox 2
			level_one.move(goldenfox2, 0, 3)
			if level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 787 and cambio2 == False:
				cambio2 = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox2, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 847 and cambio2 == False:
				cambio2 = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy1 = energy1 - 0.01
			energy2 = energy2 - 0.01
			eneg.config(text=int(energy1))
			eneg2.config(text=int(energy2))
			speed.config(text=str(velocidad)+"Km/s")
			speed2.config(text=str(velocidad2)+"Km/s")

			
			#Colisión con Golden Fox
			if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy1 = energy1 - 5
				eneg.config(text=int(energy1))
				if level_one.coords(goldenfox)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [161, 501] or level_one.coords(goldenfox) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)



			#Colisión con Hyper Speeder
			elif 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy1 = energy1 - 5
				eneg.config(text=int(energy1))
				if level_one.coords(hyper)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [161, 501] or level_one.coords(hyper) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Colisión con Wyvern
			elif 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy1 = energy1 - 5
				eneg.config(text=int(energy1))
				if level_one.coords(wyvern)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [161, 501] or level_one.coords(wyvern) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 1
			elif falc_coords[1] == wyvern_coords[1]:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif hyper_coords[1] == 502:
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")


			#Colisión con Wyvern 2
			if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
				energy2 = energy2 - 5
				eneg2.config(text=int(energy2))
				if level_one.coords(wyvern2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(wyvern2, -velocidad/10, 0)
				elif level_one.coords(wyvern2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(wyvern2, velocidad/10, 0)
				if level_one.coords(wyvern2) < [777, 501] or level_one.coords(wyvern2) > [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern2_coords[0], wyvern2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
					for x in range(10):
						level_one.move(wyvern2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox 2
			elif 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
				energy2 = energy2 - 5
				eneg2.config(text=int(energy2))
				if level_one.coords(goldenfox2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(goldenfox2, -velocidad/10, 0)
				elif level_one.coords(goldenfox2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(goldenfox2, velocidad/10, 0)
				if level_one.coords(goldenfox2) <= [777, 501] or level_one.coords(goldenfox2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox2_coords[0], goldenfox2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
					for x in range(10):
						level_one.move(goldenfox2, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder2
			elif 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
				energy2 = energy2 - 5
				eneg2.config(text=int(energy2))
				if level_one.coords(hyper2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(hyper2, -velocidad/10, 0)
				elif level_one.coords(hyper2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(hyper2, velocidad/10, 0)
				if level_one.coords(hyper2) <= [777, 501] or level_one.coords(hyper2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper2_coords[0], hyper2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
					for x in range(10):
						level_one.move(hyper2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 2
			elif fire_coords[1] == wyvern_coords[1]:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif goldenfox2_coords[1] == 502:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif hyper2_coords[1] == 502:
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [161, 501] or level_one.coords(falc) >= [235, 501]:
				energy1 = energy1 - 17
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


			#Colisión con los límites de la carretera fire
			if level_one.coords(fire) <= [777, 501] or level_one.coords(fire) >= [852, 501]:
				energy2 = energy2 - 17
				for x in range(len(list_explos)):
					explos = level_one.create_image(fire_coords[0], fire_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif level_one.coords(space2)[1] >= 1:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy1 <= 0:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy2 <= 0:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 168, 501)
	#level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

def level4_2p():
	global nombre1
	global nombre2
	global init
	global energy1
	global energy2
	global wyvern
	global wyvern_box
	global wyvern2
	global goldenfox
	global goldenfox2
	global hyper
	global hyper2
	global ball
	global ball2
	global hole
	global hole2
	global cargado
	global velocidad2
	global puntos1
	global puntos2


	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space4.jpg")
	espacio2 = Image.open("space4_2.jpg")
	bandas = Image.open("separador.png")
	falcon = Image.open("falcon.png")
	nombre1 = nombre1.get()
	nombre2 = nombre2.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(0, -18984, image=espacio.fondo, anchor="nw")
	#Integrar el fondo2
	espacio2.fondo = ImageTk.PhotoImage(espacio2)
	space2 = level_one.create_image(520, -18984, image=espacio2.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(199, 501, image=falcon.jugador, anchor="nw")
	#Integrar jugador2 al canvas
	f = Image.open("fire.png")
	fire_jugador = ImageTk.PhotoImage(f)
	fire = level_one.create_image(782, 501, image=fire_jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("win-lose.png")
	win_lose = ImageTk.PhotoImage(w)
	l = Image.open("lose-win.png")
	lose_win = ImageTk.PhotoImage(l)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(168, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar el enemigo con velocidad constante (Wyvern) 2
	def wyvern_spawn2():
		global wyvern2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)
		elif resultado == "si" and level_one.coords(wyvern2)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)

	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern2 = level_one.create_image(787, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern2)


	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 1986:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemigo que cambia de carril aleatoriamente 2
	def goldenfox_spawn2():
		global goldenfox2
		global cambio2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False
		elif resultado_gf == "si" and level_one.coords(goldenfox2)[1] > 1986:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox2 = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar al enemgio que sigue al jugador

	def hyper_spawn2():
		global hyper2
		global cambio_hyper2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False
		elif resultado_hy == "si" and level_one.coords(hyper2)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper2 = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar la energy ball (carro gasolina)

	def ball_spawn2():
		global ball2
		global ball2_box
		global ball2_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball2)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball2 = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 4000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		else:
			hole = level_one.create_image(0, 1000, image=ho, anchor="nw")

	def hole_spawn2():
		global hole2
		global hole2_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)
		elif aparecer_hole == 4 and level_one.coords(hole2)[1] > 4000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole2 = level_one.create_image(0, 600, image=ho, anchor="nw")

	#Intergrar el nombre del jugador a la pantalla
	name = Label(level_one, text=nombre1, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=340, y=88)
	#Intergrar el nombre del jugador2 a la pantalla
	name = Label(level_one, text=nombre2, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=539, y=88)
	#Movimiento del jugador
	distancia = 5
	movimientos = {
		"left" : (-distancia, 0),
		"right" : (distancia, 0),
		"a" : (-distancia, 0),
		"d" : (distancia, 0)
		}
	def move_press1(event):
		if level_one.coords(falc) >= [161, 501] and level_one.coords(falc) <= [235, 501]:
			key = (event.keysym).lower()
			level_one.move(falc, * movimientos[key])
	def move_press2(event):
		key = (event.keysym).lower()
		level_one.move(fire, * movimientos[key])
	level_one.bind_all("<KeyPress-Left>", move_press2)
	level_one.bind_all("<KeyPress-Right>", move_press2)
	level_one.bind_all("<KeyPress-a>", move_press1)
	level_one.bind_all("<KeyPress-d>", move_press1)
	#Movimiento de la carretera
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	#Movimiento de la carretera2
	def accelerate2(event):
		global velocidad2
		if velocidad2 < 300:
			velocidad2 = velocidad2 + 10
	def deaccelerate2(event): 
		global velocidad2
		while velocidad2 > 0 and velocidad2 <= 300:
			velocidad2 = velocidad2 - 1
	level_one.bind_all("<KeyPress-Up>", accelerate2)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate2)
	level_one.bind_all("<KeyPress-w>", accelerate)
	level_one.bind_all("<KeyRelease-w>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa2p.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			juego()

	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy1, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=340, y=482)

	#Declaración de la energía de la nave2
	eneg2 = Label(level_one, text=energy2, bg="black", fg="#4cffb5", font=("System", 30))
	eneg2.place(x=560, y=482)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=339, y=402)

	#Label para el título "Energy"
	energia_lab2 = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab2.place(x=544, y=402)


	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=335, y=197)

	#Mostrar la velocidad en pantalla 2
	speed2 = Label(level_one, text=velocidad2, bg="black", fg="#4cffb5", font=("System", 30))
	speed2.place(x=531, y=197)

	#Puntuación
	puntos = Label(level_one, text=puntos1, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=334, y=299)

	#Puntuación
	puntos_2p = Label(level_one, text=puntos2, bg="black", fg="#4cffb5", font=("System", 30))
	puntos_2p.place(x=529, y=299)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy1
		global energy2
		global wyvern
		global wyvern2
		global wyvern_box
		global wyvern2_box
		global puntos_1p
		global goldenfox
		global goldenfox2
		global cambio
		global cambio2
		global hyper
		global hyper2
		global ball
		global ball2
		global hole
		global hole2
		global velocidad
		global velocidad2
		global coordenadas_juego
		global puntos1
		global puntos2

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 198, level_one.coords(falc)[1])
		level_one.coords(fire, 817, level_one.coords(fire)[1])
		#Se crea el enemigo wyvern
		while start == True and energy1 > 0 and energy2 > 0 and pausado == False and level_one.coords(space)[1] < 1 and level_one.coords(space2)[1] < 1:
			fire_coords = level_one.coords(fire)
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			fire_box = level_one.bbox(fire)
			level_one.after(5000, wyvern_spawn)
			level_one.after(5000, wyvern_spawn2)
			level_one.move(space, 0, velocidad/70)
			level_one.move(space2, 0, velocidad2/70)
			level_one.move(wyvern, 0, 3)
			level_one.move(wyvern2, 0, 3)

			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern2_box = level_one.bbox(wyvern2)
			wyvern_coords = level_one.coords(wyvern)
			wyvern2_coords = level_one.coords(wyvern2)

			#Aparición del agujero negro
			hole_spawn()
			hole_spawn2()
			hole_box = level_one.bbox(hole)
			hole2_box = level_one.bbox(hole2)
			hole_coords = level_one.coords(hole)
			hole2_coords = level_one.coords(hole2)
			level_one.move(hole, 0, 3)
			level_one.move(hole2, 0, 3)

			#Colisión con el agujero negro
			if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 168:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 5
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 227:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 5
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)
			#Colisión con el agujero negro 2
			if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
				if hole2_coords[0] == 787:
					for x in range(10):
						level_one.move(fire, (velocidad+3)/100, 0)
						velocidad2 -= 5
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole2_coords[0] == 227:
					for x in range(10):
						level_one.move(fire, -(velocidad+3)/100, 0)
						velocidad2 -= 5
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_spawn2()
			ball_box = level_one.bbox(ball)
			ball2_box = level_one.bbox(ball2)
			level_one.move(ball, 0, 3)
			level_one.move(ball2, 0, 3)
			#Colisión con la energy ball
			if 4 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy1 = energy1 + 10
				eneg.config(text=int(energy1))
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")
			if 5 in level_one.find_overlapping(ball2_box[0], ball2_box[1], ball2_box[2], ball2_box[3]):
				level_one.coords(ball2, 0, 600)
				energy2 = energy2 + 10
				eneg2.config(text=int(energy2))
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			hyper_spawn2()
			level_one.move(hyper, 0, 3)
			level_one.move(hyper2, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			hyper2_coords = level_one.coords(hyper2)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			hyper2_box = level_one.bbox(hyper2)
			#Movimiento de cambio de carril
			if level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 168 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 197:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 227 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 197:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento de cambio de carril 2
			if level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 787 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] > 850:
					for x in range(12):
						level_one.move(hyper2, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 847 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] < 850:
					for x in range(12):
						level_one.move(hyper2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			level_one.after(5000, goldenfox_spawn2)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			goldenfox2_coords = level_one.coords(goldenfox2)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			fox2_box = level_one.bbox(goldenfox2)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 168 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 227 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento y cambio de carril de golden fox 2
			level_one.move(goldenfox2, 0, 3)
			if level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 787 and cambio2 == False:
				cambio2 = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox2, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 847 and cambio2 == False:
				cambio2 = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy1 = energy1 - 0.01
			energy2 = energy2 - 0.01
			eneg.config(text=int(energy1))
			eneg2.config(text=int(energy2))
			speed.config(text=str(velocidad)+"Km/s")
			speed2.config(text=str(velocidad2)+"Km/s")

			
			#Colisión con Golden Fox
			if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy1 = energy1 - 10
				eneg.config(text=int(energy1))
				if level_one.coords(goldenfox)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [161, 501] or level_one.coords(goldenfox) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)



			#Colisión con Hyper Speeder
			elif 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy1 = energy1 - 10
				eneg.config(text=int(energy1))
				if level_one.coords(hyper)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [161, 501] or level_one.coords(hyper) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Colisión con Wyvern
			elif 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy1 = energy1 - 10
				eneg.config(text=int(energy1))
				if level_one.coords(wyvern)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [161, 501] or level_one.coords(wyvern) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 1
			elif falc_coords[1] == wyvern_coords[1]:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif hyper_coords[1] == 502:
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")


			#Colisión con Wyvern 2
			if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
				energy2 = energy2 - 10
				eneg2.config(text=int(energy2))
				if level_one.coords(wyvern2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(wyvern2, -velocidad/10, 0)
				elif level_one.coords(wyvern2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(wyvern2, velocidad/10, 0)
				if level_one.coords(wyvern2) < [777, 501] or level_one.coords(wyvern2) > [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern2_coords[0], wyvern2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
					for x in range(10):
						level_one.move(wyvern2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox 2
			elif 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
				energy2 = energy2 - 10
				eneg2.config(text=int(energy2))
				if level_one.coords(goldenfox2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(goldenfox2, -velocidad/10, 0)
				elif level_one.coords(goldenfox2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(goldenfox2, velocidad/10, 0)
				if level_one.coords(goldenfox2) <= [777, 501] or level_one.coords(goldenfox2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox2_coords[0], goldenfox2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
					for x in range(10):
						level_one.move(goldenfox2, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder2
			elif 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
				energy2 = energy2 - 10
				eneg2.config(text=int(energy2))
				if level_one.coords(hyper2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(hyper2, -velocidad/10, 0)
				elif level_one.coords(hyper2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(hyper2, velocidad/10, 0)
				if level_one.coords(hyper2) <= [777, 501] or level_one.coords(hyper2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper2_coords[0], hyper2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
					for x in range(10):
						level_one.move(hyper2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 2
			elif fire_coords[1] == wyvern_coords[1]:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif goldenfox2_coords[1] == 502:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif hyper2_coords[1] == 502:
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [161, 501] or level_one.coords(falc) >= [235, 501]:
				energy1 = energy1 - 20
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


			#Colisión con los límites de la carretera fire
			if level_one.coords(fire) <= [777, 501] or level_one.coords(fire) >= [852, 501]:
				energy2 = energy2 - 20
				for x in range(len(list_explos)):
					explos = level_one.create_image(fire_coords[0], fire_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif level_one.coords(space2)[1] >= 1:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy1 <= 0:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy2 <= 0:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 168, 501)
	#level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()

def level5_2p():
	global nombre1
	global nombre2
	global init
	global energy1
	global energy2
	global wyvern
	global wyvern_box
	global wyvern2
	global goldenfox
	global goldenfox2
	global hyper
	global hyper2
	global ball
	global ball2
	global hole
	global hole2
	global cargado
	global velocidad2
	global puntos1
	global puntos2


	#Declarar las variables que se utilizarán
	start = False
	espacio = Image.open("space5.jpg")
	espacio2 = Image.open("space5_2.jpg")
	bandas = Image.open("separador.png")
	falcon = Image.open("falcon.png")
	nombre1 = nombre1.get()
	nombre2 = nombre2.get()
	#Generar la ventana
	level1 = Tk()
	level1.geometry("1000x600")
	level1.resizable(0, 0)
	level1.title("Space Road")
	level1.focus_force()
	#Generar el canvas
	level_one = Canvas(level1, width=1000, height=600)
	level_one.place(x=0, y=0)
	#Integrar el fondo
	espacio.fondo = ImageTk.PhotoImage(espacio)
	space = level_one.create_image(0, -18984, image=espacio.fondo, anchor="nw")
	#Integrar el fondo2
	espacio2.fondo = ImageTk.PhotoImage(espacio2)
	space2 = level_one.create_image(520, -18984, image=espacio2.fondo, anchor="nw")
	#Integrar las bandas negras
	bandas.fondo = ImageTk.PhotoImage(bandas)
	band = level_one.create_image(0, 0, image=bandas.fondo, anchor="nw")
	#Integrar jugador al canvas
	falcon.jugador = ImageTk.PhotoImage(falcon)
	falc = level_one.create_image(199, 501, image=falcon.jugador, anchor="nw")
	#Integrar jugador2 al canvas
	f = Image.open("fire.png")
	fire_jugador = ImageTk.PhotoImage(f)
	fire = level_one.create_image(782, 501, image=fire_jugador, anchor="nw")
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

	#Se crea una lista para la animación de la explosión
	list_explos = [explo1, explo2, explo3, explo4, explo5, explo6]

	#Imagen al completar el nivel
	w = Image.open("win-lose.png")
	win_lose = ImageTk.PhotoImage(w)
	l = Image.open("lose-win.png")
	lose_win = ImageTk.PhotoImage(l)
	#Integrar el enemigo con velocidad constante (Wyvern)
	def wyvern_spawn():
		global wyvern
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
		elif resultado == "si" and level_one.coords(wyvern)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[168, -90], [227, -90]]
			resultado2 = random.choice(spawns)
			wyvern = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern_box = level_one.bbox(wyvern)
	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern = level_one.create_image(168, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern)

	#Integrar el enemigo con velocidad constante (Wyvern) 2
	def wyvern_spawn2():
		global wyvern2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer = ["si", "no"]
		resultado = random.choice(aparecer)
		if resultado == "si" and wyvern2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)
		elif resultado == "si" and level_one.coords(wyvern2)[1] > 1000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns = [[787, -90], [847, -90]]
			resultado2 = random.choice(spawns)
			wyvern2 = level_one.create_image(resultado2[0], resultado2[1], image=wyv, anchor="nw")
			wyvern2_box = level_one.bbox(wyvern2)

	wy = Image.open("wyvern.png")
	wyv = ImageTk.PhotoImage(wy)
	wyvern2 = level_one.create_image(787, -90, image=wyv, anchor="nw")
	wyvern_box = level_one.bbox(wyvern2)


	#Integrar al enemigo que cambia de carril aleatoriamente 
	def goldenfox_spawn():
		global goldenfox
		global cambio
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False
		elif resultado_gf == "si" and level_one.coords(goldenfox)[1] > 1500:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[168, -350], [227, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox_box = level_one.bbox(goldenfox)
			cambio = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemigo que cambia de carril aleatoriamente 2
	def goldenfox_spawn2():
		global goldenfox2
		global cambio2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_gf = ["si", "no"]
		resultado_gf = random.choice(aparecer_gf)
		if resultado_gf == "si" and goldenfox2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False
		elif resultado_gf == "si" and level_one.coords(goldenfox2)[1] > 1500:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_gf = [[787, -350], [847, -350]]
			resultado2_gf = random.choice(spawns_gf)
			goldenfox2 = level_one.create_image(resultado2_gf[0], resultado2_gf[1], image=gold, anchor="nw")
			goldenfox2_box = level_one.bbox(goldenfox2)
			cambio2 = False

	gf = Image.open("goldenfox.png")
	gold = ImageTk.PhotoImage(gf)
	goldenfox2 = level_one.create_image(0, 600, image=gold, anchor="nw")

	#Integrar al enemgio que sigue al jugador

	def hyper_spawn():
		global hyper
		global cambio_hyper
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False
		elif resultado_hy == "si" and level_one.coords(hyper)[1] > 2000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[168, -128], [227, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper_box = level_one.bbox(hyper)
			cambio_hyper = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar al enemgio que sigue al jugador

	def hyper_spawn2():
		global hyper2
		global cambio_hyper2
		#Se hace una elección para que aparezca el enemigo o no
		aparecer_hy = ["si", "no"]
		resultado_hy = random.choice(aparecer_hy)
		if resultado_hy == "si" and hyper2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado_hy[0], resultado_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False
		elif resultado_hy == "si" and level_one.coords(hyper2)[1] > 2000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hy = [[787, -128], [847, -128]]
			resultado2_hy = random.choice(spawns_hy)
			hyper2 = level_one.create_image(resultado2_hy[0], resultado2_hy[1], image=hy, anchor="nw")
			hyper2_box = level_one.bbox(hyper2)
			cambio_hyper2 = False

	hs = Image.open("hyper.png")
	hy = ImageTk.PhotoImage(hs)
	hyper2 = level_one.create_image(0, 600, image=hy, anchor="nw")


	#Integrar la energy ball (carro gasolina)

	def ball_spawn():
		global ball
		global ball_box
		global ball_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball)[1] > 2000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[168, -128], [227, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball_box = level_one.bbox(ball)
			ball_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar la energy ball (carro gasolina)

	def ball_spawn2():
		global ball2
		global ball2_box
		global ball2_in_movement
		aparecer_ball = random.randrange(10)
		if aparecer_ball == 4 and ball2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado_ball[0], resultado_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True
		elif aparecer_ball == 4 and level_one.coords(ball2)[1] > 2000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_ball = [[787, -128], [847, -128]]
			resultado2_ball = random.choice(spawns_ball)
			ball2 = level_one.create_image(resultado2_ball[0], resultado2_ball[1], image=en, anchor="nw")
			ball2_box = level_one.bbox(ball2)
			ball2_in_movement = True


	e = Image.open("energy ball.png")
	en = ImageTk.PhotoImage(e)
	ball2 = level_one.create_image(0, 600, image=en, anchor="nw")

	#Integrar el agujero negro (mancha de aceite)

	def hole_spawn():
		global hole
		global hole_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		elif aparecer_hole == 4 and level_one.coords(hole)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[168, -128], [227, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole_box = level_one.bbox(hole)
		else:
			hole = level_one.create_image(0, 1000, image=ho, anchor="nw")

	def hole_spawn2():
		global hole2
		global hole2_box
		aparecer_hole = random.randrange(10)
		if aparecer_hole == 4 and hole2 == 0:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado_hole[0], resultado_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)
		elif aparecer_hole == 4 and level_one.coords(hole2)[1] > 3000:
			#Se hace otra elección aleatoria para que posicione al enemigo en uno de los dos carriles diponibles
			spawns_hole = [[787, -128], [847, -128]]
			resultado2_hole = random.choice(spawns_hole)
			hole2 = level_one.create_image(resultado2_hole[0], resultado2_hole[1], image=ho, anchor="nw")
			hole2_box = level_one.bbox(hole2)

	h = Image.open("hole.png")
	ho = ImageTk.PhotoImage(h)
	hole2 = level_one.create_image(0, 600, image=ho, anchor="nw")

	#Intergrar el nombre del jugador a la pantalla
	name = Label(level_one, text=nombre1, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=340, y=88)
	#Intergrar el nombre del jugador2 a la pantalla
	name = Label(level_one, text=nombre2, bg="black", fg="#4cffb5", font=("System", 30))
	name.place(x=539, y=88)
	#Movimiento del jugador
	distancia = 5
	movimientos = {
		"left" : (-distancia, 0),
		"right" : (distancia, 0),
		"a" : (-distancia, 0),
		"d" : (distancia, 0)
		}
	def move_press1(event):
		if level_one.coords(falc) >= [161, 501] and level_one.coords(falc) <= [235, 501]:
			key = (event.keysym).lower()
			level_one.move(falc, * movimientos[key])
	def move_press2(event):
		key = (event.keysym).lower()
		level_one.move(fire, * movimientos[key])
	level_one.bind_all("<KeyPress-Left>", move_press2)
	level_one.bind_all("<KeyPress-Right>", move_press2)
	level_one.bind_all("<KeyPress-a>", move_press1)
	level_one.bind_all("<KeyPress-d>", move_press1)
	#Movimiento de la carretera
	def accelerate(event):
		global velocidad
		if velocidad < 300:
			velocidad = velocidad + 10
	def deaccelerate(event): 
		global velocidad
		while velocidad > 0 and velocidad <= 300:
			velocidad = velocidad - 1
	#Movimiento de la carretera2
	def accelerate2(event):
		global velocidad2
		if velocidad2 < 300:
			velocidad2 = velocidad2 + 10
	def deaccelerate2(event): 
		global velocidad2
		while velocidad2 > 0 and velocidad2 <= 300:
			velocidad2 = velocidad2 - 1
	level_one.bind_all("<KeyPress-Up>", accelerate2)
	level_one.bind_all("<KeyRelease-Up>", deaccelerate2)
	level_one.bind_all("<KeyPress-w>", accelerate)
	level_one.bind_all("<KeyRelease-w>", deaccelerate)
	#Imagen del menú de pausa
	pausa = Image.open("pausa2p.png")
	pause = ImageTk.PhotoImage(pausa)
	#Definición para el evento para pausar
	def pause_menu(event):
		global p_selecter
		global pausado
		global ventana_pausa
		if pausado == False:
			pausado = True
			ventana_pausa = level_one.create_image(0, 0, image=pause, anchor="nw")
		elif pausado == True:
			pausado = False
			level_one.delete(ventana_pausa)
			juego()

	#Key bind para entrar al menú de pausa
	level_one.bind_all("<Key-p>", pause_menu)

	#Declaración de la energía de la nave
	eneg = Label(level_one, text=energy1, bg="black", fg="#4cffb5", font=("System", 30))
	eneg.place(x=340, y=482)

	#Declaración de la energía de la nave2
	eneg2 = Label(level_one, text=energy2, bg="black", fg="#4cffb5", font=("System", 30))
	eneg2.place(x=560, y=482)

	#Label para el título "Energy"
	energia_lab = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab.place(x=339, y=402)

	#Label para el título "Energy"
	energia_lab2 = Label(level_one, text= "Energy", bg="black", fg="#4cffb5", font=("System", 30))
	energia_lab2.place(x=544, y=402)


	#Mostrar la velocidad en pantalla
	speed = Label(level_one, text=velocidad, bg="black", fg="#4cffb5", font=("System", 30))
	speed.place(x=335, y=197)

	#Mostrar la velocidad en pantalla 2
	speed2 = Label(level_one, text=velocidad2, bg="black", fg="#4cffb5", font=("System", 30))
	speed2.place(x=531, y=197)

	#Puntuación
	puntos = Label(level_one, text=puntos1, bg="black", fg="#4cffb5", font=("System", 30))
	puntos.place(x=334, y=299)

	#Puntuación
	puntos_2p = Label(level_one, text=puntos2, bg="black", fg="#4cffb5", font=("System", 30))
	puntos_2p.place(x=529, y=299)

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

	#Primera imagen de goldenfox
	goldenfox = level_one.create_image(0, 3001, image=gold, anchor="nw")

	#Integrar la imagen de perder la partida
	perd = Image.open("lose.png")
	los = ImageTk.PhotoImage(perd)

	#Aplicar movimiento al fondo
	def juego():
		global energy1
		global energy2
		global wyvern
		global wyvern2
		global wyvern_box
		global wyvern2_box
		global puntos_1p
		global goldenfox
		global goldenfox2
		global cambio
		global cambio2
		global hyper
		global hyper2
		global ball
		global ball2
		global hole
		global hole2
		global velocidad
		global velocidad2
		global coordenadas_juego
		global puntos1
		global puntos2

		#Se posiciona al jugador en el eje x de inicio
		level_one.coords(falc, 198, level_one.coords(falc)[1])
		level_one.coords(fire, 817, level_one.coords(fire)[1])
		#Se crea el enemigo wyvern
		while start == True and energy1 > 0 and energy2 > 0 and pausado == False and level_one.coords(space)[1] < 1 and level_one.coords(space2)[1] < 1:
			fire_coords = level_one.coords(fire)
			falc_coords = level_one.coords(falc)
			#Declaración de la caja para las colisiones
			falc_box = level_one.bbox(falc)
			fire_box = level_one.bbox(fire)
			level_one.after(5000, wyvern_spawn)
			level_one.after(5000, wyvern_spawn2)
			level_one.move(space, 0, velocidad/70)
			level_one.move(space2, 0, velocidad2/70)
			level_one.move(wyvern, 0, 3)
			level_one.move(wyvern2, 0, 3)

			#Declaración de la caja para las colisiones
			wyvern_box = level_one.bbox(wyvern)
			wyvern2_box = level_one.bbox(wyvern2)
			wyvern_coords = level_one.coords(wyvern)
			wyvern2_coords = level_one.coords(wyvern2)

			#Aparición del agujero negro
			hole_spawn()
			hole_spawn2()
			hole_box = level_one.bbox(hole)
			hole2_box = level_one.bbox(hole2)
			hole_coords = level_one.coords(hole)
			hole2_coords = level_one.coords(hole2)
			level_one.move(hole, 0, 3)
			level_one.move(hole2, 0, 3)

			#Colisión con el agujero negro
			if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
				if hole_coords[0] == 168:
					for x in range(10):
						level_one.move(falc, (velocidad+3)/100, 0)
						velocidad -= 5
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole_coords[0] == 227:
					for x in range(10):
						level_one.move(falc, -(velocidad+3)/100, 0)
						velocidad -= 5
						level_one.update()
						time.sleep(0.01)
						if 4 in level_one.find_overlapping(hole_box[0], hole_box[1], hole_box[2], hole_box[3]):
							for x in range(10):
								level_one.move(hole, 0, 3)
								level_one.update()
								time.sleep(0.01)
			#Colisión con el agujero negro 2
			if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
				if hole2_coords[0] == 787:
					for x in range(10):
						level_one.move(fire, (velocidad+3)/100, 0)
						velocidad2 -= 5
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)

				if hole2_coords[0] == 227:
					for x in range(10):
						level_one.move(fire, -(velocidad+3)/100, 0)
						velocidad2 -= 5
						level_one.update()
						time.sleep(0.01)
						if 5 in level_one.find_overlapping(hole2_box[0], hole2_box[1], hole2_box[2], hole2_box[3]):
							for x in range(10):
								level_one.move(hole2, 0, 3)
								level_one.update()
								time.sleep(0.01)


			#Aparación de la Energy ball
			ball_spawn()
			ball_spawn2()
			ball_box = level_one.bbox(ball)
			ball2_box = level_one.bbox(ball2)
			level_one.move(ball, 0, 3)
			level_one.move(ball2, 0, 3)
			#Colisión con la energy ball
			if 4 in level_one.find_overlapping(ball_box[0], ball_box[1], ball_box[2], ball_box[3]):
				level_one.coords(ball, 0, 600)
				energy1 = energy1 + 5
				eneg.config(text=int(energy1))
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")
			if 5 in level_one.find_overlapping(ball2_box[0], ball2_box[1], ball2_box[2], ball2_box[3]):
				level_one.coords(ball2, 0, 600)
				energy2 = energy2 + 5
				eneg2.config(text=int(energy2))
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Aparición de Hyper Speeder
			hyper_spawn()
			hyper_spawn2()
			level_one.move(hyper, 0, 3)
			level_one.move(hyper2, 0, 3)
			#coordenadas de Hyper Speeder
			hyper_coords = level_one.coords(hyper)
			hyper2_coords = level_one.coords(hyper2)
			#Caja de Hyper Speeder
			hyper_box = level_one.bbox(hyper)
			hyper2_box = level_one.bbox(hyper2)
			#Movimiento de cambio de carril
			if level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 168 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] > 197:
					for x in range(12):
						level_one.move(hyper, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper) > [168, random.randrange(10, 300)] and level_one.coords(hyper)[0] == 227 and cambio == False:
				cambio_hyper = True
				if falc_coords[0] < 197:
					for x in range(12):
						level_one.move(hyper, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento de cambio de carril 2
			if level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 787 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] > 850:
					for x in range(12):
						level_one.move(hyper2, 5, 1) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(hyper2) > [787, random.randrange(10, 300)] and level_one.coords(hyper2)[0] == 847 and cambio2 == False:
				cambio_hyper2 = True
				if fire_coords[0] < 850:
					for x in range(12):
						level_one.move(hyper2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			#Aparición de Golden Fox
			level_one.after(5000, goldenfox_spawn)
			level_one.after(5000, goldenfox_spawn2)
			#Coordenadas de Golden Fox
			goldenfox_coords = level_one.coords(goldenfox)
			goldenfox2_coords = level_one.coords(goldenfox2)
			#Caja para las colisiones de golden fox
			fox_box = level_one.bbox(goldenfox)
			fox2_box = level_one.bbox(goldenfox2)
			#Movimiento y cambio de carril de golden fox
			level_one.move(goldenfox, 0, 3)
			if level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 168 and cambio == False:
				cambio = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox) > [168, random.randrange(10, 300)] and level_one.coords(goldenfox)[0] == 227 and cambio == False:
				cambio = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox, -5, 1) 
						level_one.update()
						time.sleep(0.01)
			#Movimiento y cambio de carril de golden fox 2
			level_one.move(goldenfox2, 0, 3)
			if level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 787 and cambio2 == False:
				cambio2 = True
				comprobar1 = ["si", "no"]
				cambiar_carril1 = random.choice(comprobar1)
				if cambiar_carril1 == "si":
					for x in range(12):
						level_one.move(goldenfox2, 5, 3) 
						level_one.update()
						time.sleep(0.01)
			elif level_one.coords(goldenfox2) > [787, random.randrange(10, 300)] and level_one.coords(goldenfox2)[0] == 847 and cambio2 == False:
				cambio2 = True
				comprobar2 = ["si", "no"]
				cambiar_carril2 = random.choice(comprobar2)
				if cambiar_carril2 == "si":
					for x in range(12):
						level_one.move(goldenfox2, -5, 1) 
						level_one.update()
						time.sleep(0.01)

			energy1 = energy1 - 0.01
			energy2 = energy2 - 0.01
			eneg.config(text=int(energy1))
			eneg2.config(text=int(energy2))
			speed.config(text=str(velocidad)+"Km/s")
			speed2.config(text=str(velocidad2)+"Km/s")

			
			#Colisión con Golden Fox
			if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
				energy1 = energy1 - 15
				eneg.config(text=int(energy1))
				if level_one.coords(goldenfox)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(goldenfox, -velocidad/10, 0)
				elif level_one.coords(goldenfox)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(goldenfox, velocidad/10, 0)
				if level_one.coords(goldenfox) <= [161, 501] or level_one.coords(goldenfox) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox_coords[0], goldenfox_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(fox_box[0], fox_box[1], fox_box[2], fox_box[3]):
					for x in range(10):
						level_one.move(goldenfox, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)



			#Colisión con Hyper Speeder
			elif 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
				energy1 = energy1 - 15
				eneg.config(text=int(energy1))
				if level_one.coords(hyper)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(hyper, -velocidad/10, 0)
				elif level_one.coords(hyper)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(hyper, velocidad/10, 0)
				if level_one.coords(hyper) <= [161, 501] or level_one.coords(hyper) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper_coords[0], hyper_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(hyper_box[0], hyper_box[1], hyper_box[2], hyper_box[3]):
					for x in range(10):
						level_one.move(hyper, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Colisión con Wyvern
			elif 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
				energy1 = energy1 - 15
				eneg.config(text=int(energy1))
				if level_one.coords(wyvern)[0] == 168:
					level_one.move(falc, velocidad/8, 0)
					level_one.move(wyvern, -velocidad/10, 0)
				elif level_one.coords(wyvern)[0] == 227:
					level_one.move(falc, -velocidad/8, 0)
					level_one.move(wyvern, velocidad/10, 0)
				if level_one.coords(wyvern) <= [161, 501] or level_one.coords(wyvern) >= [235, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern_coords[0], wyvern_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 4 in level_one.find_overlapping(wyvern_box[0], wyvern_box[1], wyvern_box[2], wyvern_box[3]):
					for x in range(10):
						level_one.move(wyvern, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 1
			elif falc_coords[1] == wyvern_coords[1]:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif goldenfox_coords[1] == 502:
				puntos1 += 50
				puntos.config(text=str(puntos1)+"pts")

			elif hyper_coords[1] == 502:
				puntos1 += 100
				puntos.config(text=str(puntos1)+"pts")


			#Colisión con Wyvern 2
			if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
				energy2 = energy2 - 15
				eneg2.config(text=int(energy2))
				if level_one.coords(wyvern2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(wyvern2, -velocidad/10, 0)
				elif level_one.coords(wyvern2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(wyvern2, velocidad/10, 0)
				if level_one.coords(wyvern2) < [777, 501] or level_one.coords(wyvern2) > [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(wyvern2_coords[0], wyvern2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(wyvern2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(wyvern2_box[0], wyvern2_box[1], wyvern2_box[2], wyvern2_box[3]):
					for x in range(10):
						level_one.move(wyvern2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)

			#Colisión con Golden Fox 2
			elif 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
				energy2 = energy2 - 15
				eneg2.config(text=int(energy2))
				if level_one.coords(goldenfox2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(goldenfox2, -velocidad/10, 0)
				elif level_one.coords(goldenfox2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(goldenfox2, velocidad/10, 0)
				if level_one.coords(goldenfox2) <= [777, 501] or level_one.coords(goldenfox2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(goldenfox2_coords[0], goldenfox2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(goldenfox2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(fox2_box[0], fox2_box[1], fox2_box[2], fox2_box[3]):
					for x in range(10):
						level_one.move(goldenfox2, 0, 3)
						level_one.update()
						time.sleep(0.01)

				level_one.update()
				time.sleep(0.1)

			#Colisión con Hyper Speeder2
			elif 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
				energy2 = energy2 - 15
				eneg2.config(text=int(energy2))
				if level_one.coords(hyper2)[0] == 787:
					level_one.move(fire, velocidad/8, 0)
					level_one.move(hyper2, -velocidad/10, 0)
				elif level_one.coords(hyper2)[0] == 847:
					level_one.move(fire, -velocidad/8, 0)
					level_one.move(hyper2, velocidad/10, 0)
				if level_one.coords(hyper2) <= [777, 501] or level_one.coords(hyper2) >= [852, 501]:
					for x in range(len(list_explos)):
						explos = level_one.create_image(hyper2_coords[0], hyper2_coords[1], image=list_explos[x], anchor="nw")
						level_one.coords(hyper2, 0, 600)
						if x == 5:
							level_one.delete(explos)
						level_one.update()
						time.sleep(0.1)
						level_one.delete(explos)
				if 5 in level_one.find_overlapping(hyper2_box[0], hyper2_box[1], hyper2_box[2], hyper2_box[3]):
					for x in range(10):
						level_one.move(hyper2, 0, 3)
						level_one.update()
						time.sleep(0.01)
				level_one.update()
				time.sleep(0.1)


			#Conteo de la puntuación jugador 2
			elif fire_coords[1] == wyvern_coords[1]:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif goldenfox2_coords[1] == 502:
				puntos2 += 50
				puntos_2p.config(text=str(puntos2)+"pts")

			elif hyper2_coords[1] == 502:
				puntos2 += 100
				puntos_2p.config(text=str(puntos2)+"pts")


			#Colisión con los límites de la carretera
			if level_one.coords(falc) <= [161, 501] or level_one.coords(falc) >= [235, 501]:
				energy1 = energy1 - 20
				for x in range(len(list_explos)):
					explos = level_one.create_image(falc_coords[0], falc_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


			#Colisión con los límites de la carretera fire
			if level_one.coords(fire) <= [777, 501] or level_one.coords(fire) >= [852, 501]:
				energy2 = energy2 - 20
				for x in range(len(list_explos)):
					explos = level_one.create_image(fire_coords[0], fire_coords[1], image=list_explos[x], anchor="nw")
					if x == 5:
						level_one.delete(explos)
						level_one.after(5000, juego())
					level_one.update()
					time.sleep(0.1)
					level_one.delete(explos)
			level_one.update()
			time.sleep(0.01)


		#Mensaje de que ganó la partida
		if level_one.coords(space)[1] >= 1:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif level_one.coords(space2)[1] >= 1:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy1 <= 0:
			winner = level_one.create_image(0, 0, image=lose_win, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
		elif energy2 <= 0:
			winner = level_one.create_image(0, 0, image=win_lose, anchor="nw")
			level_one.update()
			time.sleep(5)
			level1.destroy()
			level2_2p()
	#La nave del jugador vuelve al lugar de origen
	level_one.coords(falc, 168, 501)
	#level_one.coords(space, coordenadas_juego_l1_x, coordenadas_juego_l1_y)
	juego()
	cargado = False
	level1.mainloop()
menu()