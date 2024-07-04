import csv 

juegos=["valorant","fortnite","fifa"]
TipoJugador=["principiante","avanzado","experto"]
participante=[]
juegoParticipante=[]
#opcion1
def registroPuntaje():
    participante.append(input("Ingrese su ID: "))
    participante.append(input("Ingrese su Nombre Completo: "))
    ciclo=True
    while ciclo:
        while True:
            juego=str(input("Juego a elegir: ")).lower()
            if juego in juegoParticipante:
                print("El juego ya fue ingresado")
            else:
                break
        if juego in juegos:
            participante.append(juego)
            while True:
                try:
                    puntaje=int(input("Ingrese el puntaje obtenido: "))
                    if puntaje<1:
                        print("el puntaje debe ser mayor a 0")
                    else:
                        break
                except:
                    print("El puntaje debe ser solo numeros.")
            participante.append(puntaje)
            juegoParticipante.append(juego)


            elegirJuego=input("¿Desea volver a elegir un juego? (s/n): ").lower()
            if elegirJuego=="s":
                print("Vuelva a escoger el juego")
            elif elegirJuego=="n":
                break
            else:
                print("OPCION NO VALIDA")
        else:
            print("Juego no encontrado")
    while True:
        tipo=str(input("Ingrese el tipo de jugador: ")).lower()
        if tipo in TipoJugador:
            break
        else:
            print("tipo de jugador no encontrado")

    participante.append(tipo)
#opcion2
def mostrarLista():
    if len(participante)==0:
        print("no hay jugadores ingresados")
    else:    
        print(participante)
#opcion3
def Imprimit_por_tipo():
    bandera=True
    while bandera:
        opcion=str(input("Diga su tipo de jugador (Principiante - Avanzado - Experto): "))
        if opcion in TipoJugador:
            print("Funciono")
            bandera=False
        else: 
            print("Tipo de jugador no encontrado")        
    with open("Imprimir por Tipo","w",end=" ") as file:
        imprimir=csv.DictWriter(file)
        
        

            








        


