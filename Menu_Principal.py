# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:11:31 2021

@author: Anderson
"""
from Modulo import * #Importamos el Modulo

Opcion_Juego=1      #Itera las opciones antes de iniciar el juego
Nuevo_Jugador=1     #Si el usuario desea continuamos en el juego y se crea un nuevo jugador

while Opcion_Juego!=3:   
    Opcion_Juego=int(input("""Puedes elegir una de las siguientes opciones:
                       1 - Jugar.
                       2 - Ver el Historico del juego.
                       3 - Salir.\n""")) 
                       
    if Opcion_Juego==1:
        print("""Bienvenido al concurso de preguntas y respuestas:\n
        - Son 5 rondas con un plan de puntos acumulable por ronda:
        \t- Ronda 1: 100.\t
        \t- Ronda 2: 400.\t
        \t- Ronda 3: 900.\t
        \t- Ronda 4: 1600.\t
        \t- Ronda 5: 2500.
        - Para cada ronda tienes una pregunta con cuatro opciones y única respuesta.
        - A medida que aciertes aumenta la dificultad al igual que la recompensa.
        - Puedes retirarte con el acumulado antes de responder la pregunta.
        - Buena Suerte!\n""") 
        
        Jugador_Actual=Jugador() # Se crea el jugador con los atributos del objeto jugador
        
        Entrada_Nombre=input('Oprima 1 si desea Ingresar su nombre.\n')
        if Entrada_Nombre =='1':
            Nombre_Jugador=input('Ingrese su nombre: \n')
            
        else:
            Nombre_Jugador='Jugador ' + str(Nuevo_Jugador)
            Nuevo_Jugador+=1
            
        Jugador_Actual.Inicializar(Nombre_Jugador) #Se atribuyen los valores iniciales para el jugador
        Ronda=1 # Conteo de Rondas        
        
        while Ronda<=5:   
            print("\nEsta es la Ronda:",Ronda,"\nBuena suerte!")
            
            #Elegimos aleatoriamente una pregunta con su respuesta dependiendo de la Ronda actual
            Pregunta_Respuesta=Pregunta_Respuesta_Aleatoria(Ronda)

            Respuesta_Jugador=str(input(Pregunta_Respuesta[0])) #Recibimos la opcion del jugador
            
            if Respuesta_Jugador==Pregunta_Respuesta[1]: #Comparamos respuestas 
                Jugador_Actual.Aumento_Puntaje(Puntaje(Ronda)) #Aumento de puntaje
                print("\nFelicidades! Ha acertado!\n")
                if Ronda==5:
                    print('Usted ha ganado el juego!\n')
                
            else:
                print(Nombre_Jugador,"Lo sentimos! No es correcto!\n")
                Ronda=5
                
            print('Su Acumulado es: ', Jugador_Actual.Puntaje, 'Puntos.')
            
            if Ronda == 5: # Guardar el historico de jugadores
                Historico_Juego('a', Jugador_Actual.Nombre, Jugador_Actual.Puntaje)
            
            Ronda+=1

    elif Opcion_Juego==2: # Mostrar el historico de jugadores
        try:
            Historico_Juego('r', None, None)
        except:
            print('No hay Historico de Jugadores')
        
    elif Opcion_Juego==3:
        print('Hasta la proxima!\n')
    
    else:
        print('Opcion Incorrecta!\n')