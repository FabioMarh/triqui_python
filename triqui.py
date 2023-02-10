#Juego de triqui hecho con la guia de tutorial de "Programando con Fadul" de U.Caldas

#Para este juego se utilizara un tablero de 3 X 3 . 
#Los jugadores seran "X" o "O" y marcaran en la tabla dichos caracteres.
#Tras cada jugada el tablero reaparecera mostrando el lugar seleccionado.
#Para salir se utilizara la tecla q, que indicara que el jugador se a rendido.

"""
Este es el modelo del tablero que se utilizara para el juego del triqui, la 
explicación es que la variable formato_fila me permite tener seleccion de linea entre
los corchetes.

La variable linea contiene los elementos que vamos a seleccionar para
en formato_fila, para este caso, los numero del uno al nueve.

bar es la linea de separación entre lineas. 

cuando se utiliza la funcion print(formato_fila.format(*linea[:3])) se debe de 
tener claro que .format es una función que permite adaptar el formato linea, En su 
interior se ingresa *linea para delimitar los datos que entraran el los corchetes{} de formato_fila y el rango de numeros esta entre los candados [] de .format(*linea[:3])

-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------

Código para imprimir el anterior cuadro:

formato_fila = "| {} | {} | {} |"
linea= "123456789"  
bar = "-------------"
print(bar)
print(formato_fila.format(*linea[:3]))
print(bar)
print(formato_fila.format(*linea[3:6]))
print(bar)
print(formato_fila.format(*linea[6:9]))
print(bar)

"""

def formatear_tablero(juego) -> str:
    formato_fila = "| {} | {} | {} |"   # El formato de cada fila dle tablero
    bar = "-------------"               # Lineas que separan las filas del tablero
    tablero = "\n"                      # Inicializa el tablero en fin de linea (return)
    tablero= tablero.join([bar, formato_fila.format(*juego[:3]), 
                         bar, formato_fila.format(*juego[3:6]),
                         bar, formato_fila.format(*juego[6:9]),bar ]) # .join hace que se puendan colocar cosas entre los objetos de esta lista, en este caso "/n" // El asterisco "*" en .format(*juego[]) lo que hace es desempaquetar el contenido de la variable juego [linea 82].
    
    return tablero

def actualizar_movimiento(juego, jugada, jugador) -> str:
    #Validacion del tipo y el rango de la jugada
    if not (jugada.isdigit() and int(jugada) in range(1,10)): #Condiciones que se deben de cumplir 
        print(f'jugada no valida "{jugada}", solo ingrese valores entre 1 y 9')
        return juego  #El juego no cambia 
    
    #Validacion de jugada permitida
    numero_jugada = int(jugada)
    if juego [numero_jugada - 1] in "XO": #Esta ocupada con otra jugada
        print (f'La casilla "{jugada}" ya esta ocupada')
        return juego #El juego no cambia 

    juego = juego[:numero_jugada - 1] + jugador + juego [numero_jugada:]
    return juego

def encontrar_ganador(juego) -> str:
    # Opciones disponibles para ganar, estan organizadas en tuplas. 
    ganadores = ((0,1,2) ,(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

    for jugador  in ('X' , 'O'):        #Verificar por cada jugador 
           for i, j , k in ganadores:   #buscar por cada opcion ganadora en la lista de ganadores 
               linea = (juego[i], juego[j], juego[k] ) #Obtiene una tupla de los simbolos en las posiciones de la tupla ganadores. 
               if linea == (jugador,jugador, jugador): #Compara si la tupla tiene el simbolo del jugador "X" o "O" para saber que si obtuvo la victoria
                  return jugador 
    return None #No hay ganador 


def jugar_triqui() -> None:
    juego = "123456789"  #Iniciar el tablero sin jugadas
    jugador = 'X'        #Inicia el jugador "X"
    while True:          #Ciclo infinito
        print(formatear_tablero(juego))         # Dibuja el tablero 
        jugada = input(f'Jugador {jugador},¿Cual es la jugada? [Oprima "q" para terminar]: ')

        if jugada == 'q':       #Retirarse del juego 
            print("Has abandonado la partida... Juego terminado.")
            break

        juego = actualizar_movimiento(juego, jugada, jugador) #Actualizar el tablero 
        ganador = encontrar_ganador(juego) #Busca al ganador 

        if ganador != None:      #Hay un ganador 
            print(f'{ganador} has ganado!')
            print(formatear_tablero(juego))
            break

        if jugador == 'X':     #Cambiar el simbolo del jugador para la proxima jugada 
            jugador = 'O'
        else:
            jugador = 'X'


#======================================================================
#       ALGORITMO PRINCIPAL. PUNTO DE ENTRADADA A LA APLICACIÓN      ||
#======================================================================

jugar_triqui()