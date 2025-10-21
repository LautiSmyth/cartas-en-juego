import pygame
import os
import time
from .Color import *
from .Var import *

class Carta:
    def __init__(self, x, y, ancho, alto, contenido, categoria):
        self.__rect = pygame.Rect(x, y, ancho, alto)
        self.__contenido = contenido
        self.__categoria = categoria
        self.__mostrar_frente = False
        self.__eliminada = False
        self.__volteada = False
        self.__encontrada = False
        
        self.__sprite_frente = pygame.image.load(os.path.join("Sprite", "Carta", "CartaFrente.png"))
        self.__sprite_frente = pygame.transform.scale(self.__sprite_frente, (ancho, alto))
        
        self.__sprite_detras = pygame.image.load(os.path.join("Sprite", "Carta", "CartaDetras.png"))
        self.__sprite_detras = pygame.transform.scale(self.__sprite_detras, (ancho, alto))

        self.__fuente = pygame.font.Font(None, 28)
    
    def get_rect(self):
        return self.__rect    
    def set_rect(self, value):
        self.__rect = value    
    rect = property(get_rect, set_rect)
    
    def get_volteada(self):
        return self.__volteada    
    def set_volteada(self, value):
        self.__volteada = value    
    volteada = property(get_volteada, set_volteada)
    
    def get_encontrada(self):
        return self.__encontrada    
    def set_encontrada(self, value):
        self.__encontrada = value    
    encontrada = property(get_encontrada, set_encontrada)
    
    def get_eliminada(self):
        return self.__eliminada    
    def set_eliminada(self, value):
        self.__eliminada = value    
    eliminada = property(get_eliminada, set_eliminada)
    
    def get_contenido(self):
        return self.__contenido    
    contenido = property(get_contenido)
    
    def get_categoria(self):
        return self.__categoria    
    categoria = property(get_categoria)
    
    def voltear(self):
        self.__mostrar_frente = not self.__mostrar_frente
        self.__volteada = self.__mostrar_frente
    
    def mostrar(self):
        self.__mostrar_frente = True
        self.__volteada = True
    
    def ocultar(self):
        self.__mostrar_frente = False
        self.__volteada = False

    def dibujar(self, pantalla):
        if self.__eliminada:
            return
        
        #Dibujar colision
        if self.__mostrar_frente:
            pantalla.blit(self.__sprite_frente, self.__rect)
            
            contenido_texto = str(self.__contenido)
            
            # Limpiar caracteres especiales
            contenido_texto = contenido_texto.replace("[", "").replace("]", "").replace("'", "").replace('"', '')
            
            # Separar textos largos en varias líneas
            if len(contenido_texto) > 10:
                palabras = contenido_texto.split()
                lineas = []
                linea_actual = ""
                
                # Crear líneas que no excedan caracteres
                for palabra in palabras:
                    if len(linea_actual + " " + palabra) <= 10:
                        linea_actual += " " + palabra if linea_actual else palabra
                    else:
                        if linea_actual:
                            lineas.append(linea_actual)
                        linea_actual = palabra
                if linea_actual:
                    lineas.append(linea_actual)
                
                y_offset = self.__rect.centery - (len(lineas) * 14) // 2
                
                for i, linea in enumerate(lineas):
                    texto = self.__fuente.render(linea, True, NEGRO) 
                    texto_rect = texto.get_rect(center=(self.__rect.centerx, y_offset + i * 28))  
                    pantalla.blit(texto, texto_rect)
            else:
                texto = self.__fuente.render(contenido_texto, True, NEGRO) 
                texto_rect = texto.get_rect(center=self.__rect.center) 
                pantalla.blit(texto, texto_rect)
                
        else:
            pantalla.blit(self.__sprite_detras, self.__rect)
    
    def contiene_punto(self, punto):
        return self.__rect.collidepoint(punto)

class Cronometro:
    def __init__(self, x, y, tiempo_inicial):
        self.__rect = pygame.Rect(x, y, CRONOMETRO_ANCHO, CRONOMETRO_ALTO)
        self.__tiempo_inicial = tiempo_inicial
        self.__tiempo_restante = tiempo_inicial
        self.__pausado = False
        self.__ultimo_tiempo = time.time()
        
        self.__fuente = pygame.font.Font(None, 45)
    
    def get_rect(self):
        return self.__rect    
    def set_rect(self, value):
        self.__rect = value    
    rect = property(get_rect, set_rect)
    
    def actualizar(self):
        if not self.__pausado:
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - self.__ultimo_tiempo
            self.__tiempo_restante -= tiempo_transcurrido
            self.__ultimo_tiempo = tiempo_actual
            
            if self.__tiempo_restante < 0:
                self.__tiempo_restante = 0

    def reiniciar(self, nuevo_tiempo):
        self.__tiempo_inicial = nuevo_tiempo
        self.__tiempo_restante = nuevo_tiempo
        self.__pausado = False
        self.__ultimo_tiempo = time.time()

    def tiempo_agotado(self):
        return self.__tiempo_restante <= 0
    
    def obtener_tiempo_transcurrido(self):
        return self.__tiempo_inicial - self.__tiempo_restante
    
    def dibujar(self, pantalla):
        minutos = int(self.__tiempo_restante // 60)
        segundos = int(self.__tiempo_restante % 60)
        tiempo_texto = f"{minutos:02d}:{segundos:02d}"
        
        color = ROJO_PRINCIPAL if self.__tiempo_restante <= 10 else NEGRO
        texto = self.__fuente.render(tiempo_texto, True, color)
        texto_rect = texto.get_rect(center=(self.__rect.x + 115, self.__rect.y + 30))  
        pantalla.blit(texto, texto_rect)

class Puntuacion:
    def __init__(self, x, y):
        self.__rect = pygame.Rect(x, y, PUNTUACION_ANCHO, PUNTUACION_ALTO)
        self.__puntos = 0
        
        self.__fuente = pygame.font.Font(None, 45)
    
    def get_rect(self):
        return self.__rect    
    def set_rect(self, value):
        self.__rect = value    
    rect = property(get_rect, set_rect)
    
    def get_puntos(self):
        return self.__puntos    
    def set_puntos(self, value):
        self.__puntos = value    
    puntos = property(get_puntos, set_puntos)
    
    def sumar_puntos(self, cantidad):
        self.__puntos += cantidad
    
    def restar_puntos(self, cantidad):
        self.__puntos -= cantidad
    
    def reiniciar(self):
        self.__puntos = 0
    
    def obtener_puntos(self):
        return self.__puntos
    
    def dibujar(self, pantalla):
        texto = self.__fuente.render(str(self.__puntos), True, NEGRO) 
        texto_rect = texto.get_rect(center=(self.__rect.x + 132, self.__rect.y + 30))
        pantalla.blit(texto, texto_rect)