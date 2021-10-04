# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:00:05 2021

@author: Anderson

Creamos un modulo
"""
import random
import os

# Definicion de preguntas
Preguntas=[{'Pregunta 1a: Elija respuesta':'a','Pregunta 1b: Elija respuesta':'b',
            'Pregunta 1c: Elija respuesta':'c','Pregunta 1d: Elija respuesta':'d',
            'Pregunta 1e: Elija respuesta':'a'},
           {'Pregunta 2a: Elija respuesta':'a','Pregunta 2b: Elija respuesta':'b',
            'Pregunta 2c: Elija respuesta':'c','Pregunta 2d: Elija respuesta':'d',
            'Pregunta 2e: Elija respuesta':'a'},
           {'Pregunta 3a: Elija respuesta':'a','Pregunta 3b: Elija respuesta':'b',
            'Pregunta 3c: Elija respuesta':'c','Pregunta 3d: Elija respuesta':'d',
            'Pregunta 3e: Elija respuesta':'a'},
           {'Pregunta 4a: Elija respuesta':'a','Pregunta 4b: Elija respuesta':'b',
            'Pregunta 4c: Elija respuesta':'c','Pregunta 4d: Elija respuesta':'d',
            'Pregunta 4e: Elija respuesta':'a'},
           {'Pregunta 5a: Elija respuesta':'a','Pregunta 5b: Elija respuesta':'b',
            'Pregunta 5c: Elija respuesta':'c','Pregunta 5d: Elija respuesta':'d',
            'Pregunta 5e: Elija respuesta':'a'}] 

class Jugador:    
    def Inicializar(self, Nombre): #Inicializa los datos del objeto jugador
        self.Nombre=Nombre
        self.Puntaje=0

    def Aumento_Puntaje(self, Puntaje):
        self.Puntaje+=Puntaje

def Pregunta_Respuesta_Aleatoria(Ronda): #Elegimos aleatoriamente una pregunta y su respuesta dependiendo de la Ronda
    return list(random.choice(list(Preguntas[Ronda-1].items())))

def Puntaje(Ronda): #El puntaje aumenta exponencialmente respecto a la Ronda
    return pow(10*Ronda, 2) 
        
def Historico_Juego(Opcion, Nombre, Puntaje): #Creamos, escribimos o leemos el archivo Historico_Juego.txt 
    
    #Comprueba la existencia del Historico_Juego.txt y de ser el caso lo crea por primera vez
    if Opcion=='a' and os.path.isfile(str(os.path.abspath(os.getcwd()))+"\\Historico_Juego.txt")==False:
        Historico_Juego = open(str(os.path.abspath(os.getcwd()))+"\\Historico_Juego.txt", 'w')
        Historico_Juego.write('Nombre'+'\t'+'Puntaje' + os.linesep)
        Historico_Juego.close()
        
    Historico_Juego = open(str(os.path.abspath(os.getcwd()))+"\\Historico_Juego.txt", str(Opcion))
    
    if Opcion=='a': #Sobreescribir el archivo Historico_Juego.txt
        Historico_Juego.write(str(Nombre)+'\t'+str(Puntaje) + os.linesep)
    elif Opcion=='r': # Lectura del archivo
        print('\nEste es el Historico del Juego:\n\n',Historico_Juego.read())
        
    Historico_Juego.close()
