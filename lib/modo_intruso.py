import pygame
import random
import time
import os
from .Core import Carta, Cronometro, Puntuacion
from .config import DATOS_MATERIAS, CONFIG_INTRUSO
from .preguntas_intruso import PREGUNTAS_INTRUSO
from .Color import *
from .Var import *
from .sonidos import sistema_audio

class ModoIntruso:
    def __init__(self, pantalla, ancho, alto, materias_seleccionadas=None):
        self.__pantalla = pantalla
        self.__ancho = ancho
        self.__alto = alto
        
        if materias_seleccionadas is None:
            self.__materias_seleccionadas = ["Matemáticas"] 
        else:
            self.__materias_seleccionadas = materias_seleccionadas
        
        self.__nivel_actual = 1
        self.__intruso_encontrado = False
        self.__esperando_siguiente_nivel = False
        self.__tiempo_espera_nivel = 0

        self.__preguntas_utilizadas = {
            "Matemáticas": set(),
            "Historia": set(),
            "Química": set(),
            "Geografía": set()
        }
        
        self.__fondo_partida = pygame.image.load(os.path.join("Sprite", "Fondo", "fondominijuego.png")).convert_alpha()  
        self.__fondo_partida = pygame.transform.smoothscale(self.__fondo_partida, (ancho, alto)) 
        
        self.__cronometro = Cronometro(814, 160, INTRUSO_TIEMPO_CRONOMETRO[1]) 
        self.__puntuacion = Puntuacion(30, 160) 

        self.crear_nivel()
    
    def crear_nivel(self):
        materia_principal = self.__materias_seleccionadas[0]
        
        if materia_principal == "Matemáticas":
            contenidos, indice_intruso, categoria_mayoria = self.generar_matematicas_intruso()
        elif materia_principal == "Historia":
            contenidos, indice_intruso, categoria_mayoria = self.generar_historia_intruso()
        elif materia_principal == "Química":
            contenidos, indice_intruso, categoria_mayoria = self.generar_quimica_intruso()            
        else:
            contenidos, indice_intruso, categoria_mayoria = self.generar_geografia_intruso()
        
        self.__indice_intruso = indice_intruso
        self.__categoria_mayoria = categoria_mayoria
        
        self.__cartas = []
        
        # Posiciones de cartas
        margen_x = (self.__ancho - (3 * CARTA_ANCHO + 2 * CARTA_ESPACIADO)) // 2
        margen_y = (self.__alto - (2 * CARTA_ALTO + CARTA_ESPACIADO)) // 2 + 50
        
        for i, contenido in enumerate(contenidos):
            fila = i // 3  
            col = i % 3   
            
            x = margen_x + col * (CARTA_ANCHO + CARTA_ESPACIADO)
            y = margen_y + fila * (CARTA_ALTO + CARTA_ESPACIADO)

            tipo = "intruso" if i == self.__indice_intruso else "normal"
            carta = Carta(x, y, CARTA_ANCHO, CARTA_ALTO, contenido, tipo)
            carta.mostrar()
            self.__cartas.append(carta)
    
    def generar_matematicas_intruso(self):
        opciones = PREGUNTAS_INTRUSO["Matemáticas"]
        
        opciones_disponibles = []
        for i, (normales, intruso, categoria) in enumerate(opciones):
            if i not in self.__preguntas_utilizadas["Matemáticas"]:
                opciones_disponibles.append((i, normales, intruso, categoria))
        
        if not opciones_disponibles:
            self.__preguntas_utilizadas["Matemáticas"].clear()
            opciones_disponibles = [(i, normales, intruso, categoria) 
                                  for i, (normales, intruso, categoria) in enumerate(opciones)]
        
        indice_opcion, normales, intruso, categoria = random.choice(opciones_disponibles)
        
        self.__preguntas_utilizadas["Matemáticas"].add(indice_opcion)
        
        contenidos = normales + [intruso]
        random.shuffle(contenidos)
        
        indice_intruso = contenidos.index(intruso)
                
        return contenidos, indice_intruso, categoria
    
    def generar_historia_intruso(self):
        opciones = PREGUNTAS_INTRUSO["Historia"]
        
        opciones_disponibles = []
        for i, (normales, intruso, categoria) in enumerate(opciones):
            if i not in self.__preguntas_utilizadas["Historia"]:
                opciones_disponibles.append((i, normales, intruso, categoria))
        
        if not opciones_disponibles:
            self.__preguntas_utilizadas["Historia"].clear()
            opciones_disponibles = [(i, normales, intruso, categoria) 
                                  for i, (normales, intruso, categoria) in enumerate(opciones)]
        
        indice_opcion, normales, intruso, categoria = random.choice(opciones_disponibles)
        
        self.__preguntas_utilizadas["Historia"].add(indice_opcion)
        
        contenidos = normales + [intruso]
        random.shuffle(contenidos)  
        indice_intruso = contenidos.index(intruso)
        
        return contenidos, indice_intruso, categoria
    
    def generar_quimica_intruso(self):
        opciones = PREGUNTAS_INTRUSO["Química"]
        
        opciones_disponibles = []
        for i, (normales, intruso, categoria) in enumerate(opciones):
            if i not in self.__preguntas_utilizadas["Química"]:
                opciones_disponibles.append((i, normales, intruso, categoria))
        
        if not opciones_disponibles:
            self.__preguntas_utilizadas["Química"].clear()
            opciones_disponibles = [(i, normales, intruso, categoria) 
                                  for i, (normales, intruso, categoria) in enumerate(opciones)]
        
        indice_opcion, normales, intruso, categoria = random.choice(opciones_disponibles)  
        
        self.__preguntas_utilizadas["Química"].add(indice_opcion)
        
        contenidos = normales + [intruso]
        random.shuffle(contenidos)
        indice_intruso = contenidos.index(intruso) 
        
        return contenidos, indice_intruso, categoria
    
    def generar_geografia_intruso(self):
        opciones = PREGUNTAS_INTRUSO["Geografía"]
        
        opciones_disponibles = []
        for i, (normales, intruso, categoria) in enumerate(opciones):
            if i not in self.__preguntas_utilizadas["Geografía"]:
                opciones_disponibles.append((i, normales, intruso, categoria))
        
        if not opciones_disponibles:
            self.__preguntas_utilizadas["Geografía"].clear()
            opciones_disponibles = [(i, normales, intruso, categoria) 
                                  for i, (normales, intruso, categoria) in enumerate(opciones)]
        
        indice_opcion, normales, intruso, categoria = random.choice(opciones_disponibles)
        
        self.__preguntas_utilizadas["Geografía"].add(indice_opcion)
        
        contenidos = normales + [intruso]
        random.shuffle(contenidos) 
        indice_intruso = contenidos.index(intruso)
        
        return contenidos, indice_intruso, categoria
    
    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and not self.__esperando_siguiente_nivel:
            pos = pygame.mouse.get_pos() 
            
            for i, carta in enumerate(self.__cartas):
                if carta.rect.collidepoint(pos):  
                    return self.seleccionar_carta(i, carta)
        
        return None
    
    def seleccionar_carta(self, indice, carta):
        if indice == self.__indice_intruso:
            self.__intruso_encontrado = True
            self.__puntuacion.sumar_puntos(CONFIG_INTRUSO["puntos_acierto"])
            carta.encontrada = True 
            
            sistema_audio.reproducir_correcto()
            
            if self.__nivel_actual < INTRUSO_NIVELES_MAX:
                self.__esperando_siguiente_nivel = True
                self.__tiempo_espera_nivel = pygame.time.get_ticks()
            else:
                puntos_finales = self.__puntuacion.puntos
                victoria = puntos_finales > 0
                
                return {
                    "estado": "game_over",
                    "victoria": victoria,
                    "puntuacion": puntos_finales,
                    "tiempo": self.__cronometro.obtener_tiempo_transcurrido()
                }
        else:
            self.__puntuacion.restar_puntos(abs(CONFIG_INTRUSO["puntos_error"]))
            
            sistema_audio.reproducir_incorrecto()
        
        return None
    
    def avanzar_nivel(self):
        self.__nivel_actual += 1
        self.__intruso_encontrado = False
        self.__esperando_siguiente_nivel = False
        
        tiempo_nivel = INTRUSO_TIEMPO_CRONOMETRO.get(self.__nivel_actual, 10) 
        self.__cronometro.reiniciar(tiempo_nivel)
        
        self.crear_nivel()
    
    def actualizar(self):
        self.__cronometro.actualizar()
        
        if self.__cronometro.tiempo_agotado():
            return {
                "estado": "game_over",
                "victoria": False,
                "puntuacion": self.__puntuacion.puntos,
                "tiempo": self.__cronometro.obtener_tiempo_transcurrido()
            }
        
        if self.__esperando_siguiente_nivel:
            if pygame.time.get_ticks() - self.__tiempo_espera_nivel > 2000:
                self.avanzar_nivel()
        
        return None
    
    def dibujar(self):
        if self.__fondo_partida:
            self.__pantalla.blit(self.__fondo_partida, (0, 0)) 
        else:
            self.__pantalla.fill(CREMA) 
        
        self.__cronometro.dibujar(self.__pantalla)
        self.__puntuacion.dibujar(self.__pantalla)
        
        fuente = pygame.font.Font(None, 36)  
        texto_nivel = fuente.render(f"Nivel: {self.__nivel_actual}", True, GRIS_CLARO)  
        self.__pantalla.blit(texto_nivel, (self.__ancho // 2 - 50, 20))
        
        for carta in self.__cartas:
            carta.dibujar(self.__pantalla)
        
        if self.__esperando_siguiente_nivel:
            fuente_mensaje = pygame.font.Font(None, 48)  
            texto_mensaje = fuente_mensaje.render("¡Correcto! Siguiente nivel...", True, VERDE_EXITO) 
            mensaje_rect = texto_mensaje.get_rect(center=(self.__ancho // 2, self.__alto - 50))  
            self.__pantalla.blit(texto_mensaje, mensaje_rect)  