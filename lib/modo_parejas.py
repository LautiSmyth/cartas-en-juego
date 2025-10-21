import pygame
import random
import time
import os
from .Core import Carta, Cronometro, Puntuacion
from .config import DATOS_MATERIAS, CONFIG_PAREJAS
from .Color import *
from .Var import *
from .sonidos import sistema_audio

class ModoParejas:
    def __init__(self, pantalla, ancho, alto, materia_seleccionada="Matemáticas"):
        self.__pantalla = pantalla
        self.__ancho = ancho
        self.__alto = alto
        
        # Ahora solo manejamos una materia
        self.__materia_actual = materia_seleccionada

        self.__nivel_actual = 1
        self.__parejas_encontradas = 0
        self.__cartas_seleccionadas = []  
        
        self.__tiempo_mostrar_cartas = 0
        self.__mostrando_cartas_inicial = True  
        self.__esperando_volteo = False         
        self.__tiempo_espera_volteo = 0
        self.__esperando_siguiente_nivel = False 
        self.__tiempo_espera_nivel = 0
        
        self.__tiempo_total_acumulado = 0
        self.__tiempo_inicio_juego = time.time()
        
        self.__preguntas_utilizadas = set()
        

        self.__fondo_partida = pygame.image.load(os.path.join("Sprite", "Fondo", "fondominijuego.png")).convert_alpha()
        self.__fondo_partida = pygame.transform.smoothscale(self.__fondo_partida, (ancho, alto))
        
        self.__cronometro = Cronometro(814, 160, PAREJAS_TIEMPO_CRONOMETRO) 
        self.__puntuacion = Puntuacion(30, 160)  
        
        self.crear_tablero()
        self.iniciar_visualizacion_inicial()
    
    def crear_tablero(self):        
        datos_materia = DATOS_MATERIAS[self.__materia_actual]
        
        pares_disponibles = list(datos_materia.items())
        pares_no_utilizados = []
        
        for i, (pregunta, respuestas) in enumerate(pares_disponibles):
            if i not in self.__preguntas_utilizadas:
                pares_no_utilizados.append((i, pregunta, respuestas))
        
        if len(pares_no_utilizados) < 3:
            self.__preguntas_utilizadas.clear()
            pares_no_utilizados = [(i, pregunta, respuestas) 
                                 for i, (pregunta, respuestas) in enumerate(pares_disponibles)]
        
        pares_seleccionados_con_indice = random.sample(pares_no_utilizados, 3)
        
        # Marcar las preguntas como utilizadas
        for indice, _, _ in pares_seleccionados_con_indice:
            self.__preguntas_utilizadas.add(indice)
        
        # Extraer solo pregunta y respuestas
        pares_seleccionados = [(pregunta, respuestas) for _, pregunta, respuestas in pares_seleccionados_con_indice]
        
        # Crear lista de cartas
        cartas_datos = []
        for pregunta, respuestas in pares_seleccionados:
            # Si hay múltiples respuestas, elegir una aleatoria
            if isinstance(respuestas, list):
                respuesta_seleccionada = random.choice(respuestas)
            else:
                respuesta_seleccionada = respuestas
            
            cartas_datos.append(("pregunta", pregunta))
            cartas_datos.append(("respuesta", respuesta_seleccionada))
        
        random.shuffle(cartas_datos) 
        
        self.__tablero = []
        self.__cartas = []
        
        margen_x = (self.__ancho - (PAREJAS_COLUMNAS * CARTA_ANCHO + (PAREJAS_COLUMNAS - 1) * CARTA_ESPACIADO)) // 2
        margen_y = (self.__alto - (PAREJAS_FILAS * CARTA_ALTO + (PAREJAS_FILAS - 1) * CARTA_ESPACIADO)) // 2 + 50
        
        for fila in range(PAREJAS_FILAS):
            fila_cartas = []
            for col in range(PAREJAS_COLUMNAS):
                idx = fila * PAREJAS_COLUMNAS + col
                tipo, contenido = cartas_datos[idx]
                
                x = margen_x + col * (CARTA_ANCHO + CARTA_ESPACIADO)
                y = margen_y + fila * (CARTA_ALTO + CARTA_ESPACIADO)
                
                carta = Carta(x, y, CARTA_ANCHO, CARTA_ALTO, contenido, tipo)
                fila_cartas.append(carta)
                self.__cartas.append(carta)
            
            self.__tablero.append(fila_cartas)
    
    def iniciar_visualizacion_inicial(self):
        for carta in self.__cartas:
            carta.mostrar() 
        self.__tiempo_mostrar_cartas = pygame.time.get_ticks() 
        self.__mostrando_cartas_inicial = True
    
    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and not self.__mostrando_cartas_inicial and not self.__esperando_volteo and not self.__esperando_siguiente_nivel:
            pos = pygame.mouse.get_pos()
            for carta in self.__cartas:
                if carta.rect.collidepoint(pos) and not carta.volteada and not carta.encontrada:
                    self.seleccionar_carta(carta)
                    return None
        
        return None
    
    def seleccionar_carta(self, carta):
        carta.voltear()
        self.__cartas_seleccionadas.append(carta)
        
        if len(self.__cartas_seleccionadas) == 2:
            carta1, carta2 = self.__cartas_seleccionadas
            
            if self.es_pareja(carta1, carta2):
                carta1.encontrada = True
                carta2.encontrada = True
                self.__parejas_encontradas += 1
                self.__puntuacion.sumar_puntos(CONFIG_PAREJAS["puntos_acierto"])
                
                sistema_audio.reproducir_correcto()
                
                if self.__parejas_encontradas == 3:
                    if self.__nivel_actual < 3:
                        self.__esperando_siguiente_nivel = True
                        self.__tiempo_espera_nivel = pygame.time.get_ticks() 
                    else:
                        self.completar_nivel()
                
                self.__cartas_seleccionadas = []
            else:
                self.__puntuacion.restar_puntos(abs(CONFIG_PAREJAS["puntos_error"]))
                sistema_audio.reproducir_incorrecto()
                self.__esperando_volteo = True
                self.__tiempo_espera_volteo = pygame.time.get_ticks() 
    
    def es_pareja(self, carta1, carta2):
        if carta1.categoria == carta2.categoria:
            return False
        
        materia_datos = DATOS_MATERIAS[self.__materia_actual]
        for pregunta, respuestas in materia_datos.items():
            if isinstance(respuestas, list):
                for respuesta in respuestas:
                    if ((carta1.contenido == pregunta and carta2.contenido == respuesta) or
                        (carta1.contenido == respuesta and carta2.contenido == pregunta)):
                        return True
            else:
                if ((carta1.contenido == pregunta and carta2.contenido == respuestas) or
                    (carta1.contenido == respuestas and carta2.contenido == pregunta)):
                    return True
        return False
    
    def completar_nivel(self):
        tiempo_nivel = self.__cronometro.obtener_tiempo_transcurrido()
        self.__tiempo_total_acumulado += tiempo_nivel
        
        if self.__nivel_actual < PAREJAS_NIVELES_MAX:
            self.__nivel_actual += 1
            self.__parejas_encontradas = 0
            self.__cartas_seleccionadas = []
            self.__esperando_siguiente_nivel = False
            self.__cronometro.reiniciar(PAREJAS_TIEMPO_CRONOMETRO)
            self.crear_tablero()
            self.iniciar_visualizacion_inicial()
        else:
            puntos_finales = self.__puntuacion.puntos
            victoria = puntos_finales > 0 
            
            return {
                "estado": "game_over",
                "victoria": victoria,
                "puntuacion": puntos_finales,
                "tiempo": self.__tiempo_total_acumulado
            }
    
    def actualizar(self):
        self.__cronometro.actualizar()
        
        if self.__cronometro.tiempo_agotado():
            tiempo_nivel = self.__cronometro.obtener_tiempo_transcurrido()
            self.__tiempo_total_acumulado += tiempo_nivel
            
            return {
                "estado": "game_over",
                "victoria": False,  
                "puntuacion": self.__puntuacion.puntos,
                "tiempo": self.__tiempo_total_acumulado
            }
        
        resultado_nivel = None
        if self.__parejas_encontradas == 3 and self.__nivel_actual == PAREJAS_NIVELES_MAX:
            resultado_nivel = self.completar_nivel()
            if resultado_nivel:
                return resultado_nivel
        
        if self.__mostrando_cartas_inicial:
            if pygame.time.get_ticks() - self.__tiempo_mostrar_cartas > 3000:
                for carta in self.__cartas:
                    carta.ocultar()
                self.__mostrando_cartas_inicial = False
        
        if self.__esperando_volteo:
            if pygame.time.get_ticks() - self.__tiempo_espera_volteo > 1000:
                for carta in self.__cartas_seleccionadas:
                    if not carta.encontrada:
                        carta.voltear()
                self.__cartas_seleccionadas = []
                self.__esperando_volteo = False
        
        if self.__esperando_siguiente_nivel:
            if pygame.time.get_ticks() - self.__tiempo_espera_nivel > 3000:
                self.completar_nivel()
        
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
        
        for fila in self.__tablero:
            for carta in fila:
                carta.dibujar(self.__pantalla)
        
        if self.__mostrando_cartas_inicial:
            fuente_mensaje = pygame.font.Font(None, 48)  
            texto_mensaje = fuente_mensaje.render("¡Memoriza las cartas!", True, ROJO_PRINCIPAL)  
            texto_rect = texto_mensaje.get_rect(center=(self.__ancho // 2, self.__alto - 50))  
            self.__pantalla.blit(texto_mensaje, texto_rect)
        
        if self.__esperando_siguiente_nivel and self.__nivel_actual < PAREJAS_NIVELES_MAX:
            tiempo_transcurrido = pygame.time.get_ticks() - self.__tiempo_espera_nivel  
            segundos_restantes = max(0, 3 - (tiempo_transcurrido // 1000))  
            
            fuente_contador = pygame.font.Font(None, 36) 
            texto_contador = fuente_contador.render(f"Siguiente nivel en {segundos_restantes} segundos", True, VERDE_EXITO)
            contador_rect = texto_contador.get_rect(center=(self.__ancho // 2, self.__alto - 80))  
            self.__pantalla.blit(texto_contador, contador_rect)