import random

tablero = [1,2,3,
           4,5,6,
           7,8,9]

def tablero():
    print(pos[1], pos[2], pos[3])
    print(pos[4], pos[5], pos[6])
    print(pos[7], pos[8], pos[9])

def ficha_del_jugador():
    caracter = ''
    while not (caracter =='X' or caracter == '0'):
        print('¿Con que ficha quieres jugar X o O?')
        caracter = input().upper()
    if caracter == 'X':
        return['X','O']
    else:
        return['O','X']
    
def turnos():
    if random.randint(0,1) == 0:
        return 'Jugador1'
    else:
        return 'Jugador2'
    
def movimiento(tablero, ficha, movimiento):
    tablero[movimiento] = ficha

def combo_ganador(ta,fi):
    return ((ta[7] == fi and ta[8] == fi and ta[9] == fi) or 
    (ta[4] == fi and ta[5] == fi and ta[6] == fi) or 
    (ta[1] == fi and ta[2] == fi and ta[3] == fi) or 
    (ta[7] == fi and ta[4] == fi and ta[1] == fi) or 
    (ta[8] == fi and ta[5] == fi and ta[2] == fi) or 
    (ta[9] == fi and ta[6] == fi and ta[3] == fi) or 
    (ta[7] == fi and ta[5] == fi and ta[3] == fi) or 
    (ta[9] == fi and ta[5] == fi and ta[1] == fi))

def espacio_libre(tablero,movimiento):
    return tablero[movimiento] == ' '

def movimientos(tablero):
    movimiento = ' '
    while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not espacio_libre(tablero, int(movimiento)):
        print('¿Cual va a ser su próximo movimiento? (1-9)')
        movimiento = input()
    return int(movimiento)











