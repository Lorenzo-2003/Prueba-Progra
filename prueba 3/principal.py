import funciones as fn
flag=False
while not flag:
    print("*"*20)
    print("eShirlitos")
    print("1.Registrar puntajes torneo")
    print("2.Lista de jugadores/puntajes")
    print("3.Imprimir por Tipo")
    print("4.Salir del programa")
    try:
        opc=int(input("-->"))
        if opc<1 or opc>4:
            print("valores fuera de rango")
            
    except:
        print("Solo numeros porfavor")
    if opc==1:
        fn.registroPuntaje()
    elif opc==2:
        fn.mostrarLista()
    elif opc==3:
        fn.Imprimit_por_tipo()
    elif opc==4:
        print("Salir del programa")
        flag=True



