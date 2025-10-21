import pygame
import os
from lib.Color import *
from lib.Var import *

class Creditos:    
    def __init__(self, pantalla, ancho, alto):
        self.__pantalla = pantalla
        self.__ancho = ancho
        self.__alto = alto
        
        self.__fondo = pygame.image.load(os.path.join("Sprite", "Fondo", "fondomenu.png")).convert_alpha()
        self.__fondo = pygame.transform.smoothscale(self.__fondo, (ancho, alto))
        
        self.__fuente_subtitulo = pygame.font.SysFont("Comic Sans MS", 36)
        self.__fuente_texto = pygame.font.SysFont("Comic Sans MS", 28)
        self.__fuente_boton = pygame.font.SysFont("Comic Sans MS", 32)
        
        self.__scroll_y = 0
        self.__contenido_altura = 0
        self.__max_scroll = 0
        self.__scroll_velocidad = 30
        
        self.__info_juego = {
            "descripcion": [
                "Un juego educativo de memoria y lógica que desafía tu mente",
                "a través de diferentes modalidades de juego con cartas."
            ],
            "como_jugar": [
                "• Selecciona un modo de juego desde el menú principal",
                "• Sigue las instrucciones específicas de cada modo",
                "• Completa todos los niveles manteniendo un puntaje positivo",
                "• ¡Gana solo si terminas con más de 0 puntos!"
            ],
            "modos": {
                "Modo Parejas": [
                    "Encuentra las parejas pregunta-respuesta correctas.",
                    "Memoriza las cartas al inicio de cada nivel.",
                    "Tienes tiempo limitado para completar cada nivel."
                ],
                "Modo Intruso": [
                    "Identifica el elemento que no pertenece al grupo.",
                    "Analiza cuidadosamente las opciones disponibles.",
                    "Cada nivel presenta categorías diferentes."
                ]
            },
            "proposito": [
                "Este juego está diseñado para:",
                "• Mejorar la memoria y concentración",
                "• Desarrollar habilidades de análisis y lógica",
                "• Reforzar conocimientos académicos",
                "  de forma divertida",
                "• Proporcionar entretenimiento educativo"
            ]
        }
        
        self.__autores = {
            "institucion": "Universidad Abierta Interamericana",
            "carrera": "Ingeniería en Sistemas Informáticos",
            "detalles": "Turno Noche - Sede Lomas - Comisión 3ºA",
            "estudiantes": [
                "San Martín Santiago",
                "Sassaroli Agustín",
                "Siffredi Agustín",
                "Smyth Lautaro"
            ]
        }
        
        self.__boton_volver = pygame.Rect(50, alto - 80, 150, 50)
        self.__hover_volver = False
        
        self.__calcular_altura_contenido()
    
    def __calcular_altura_contenido(self):
        """Calcula la altura total del contenido para el scroll"""
        altura = 150 
        
        altura += len(self.__info_juego["descripcion"]) * 30 + 40
        
        altura += 40 + len(self.__info_juego["como_jugar"]) * 25 + 40
        
        altura += 40
        for modo, descripcion in self.__info_juego["modos"].items():
            altura += 30 + len(descripcion) * 22 + 10
        altura += 20
        
        altura += 40 + len(self.__info_juego["proposito"]) * 30 + 80
        
        altura += 40 + 25 + 25 + 35 + 30 + len(self.__autores["estudiantes"]) * 25 + 100
        
        self.__contenido_altura = altura
        self.__max_scroll = max(0, self.__contenido_altura - self.__alto + 100)
    
    def manejar_evento(self, evento):       
        if evento.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            self.__hover_volver = self.__boton_volver.collidepoint(pos)
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.__boton_volver.collidepoint(pos):
                return {"accion": "menu"}
        
        elif evento.type == pygame.MOUSEWHEEL:
            self.__scroll_y -= evento.y * self.__scroll_velocidad
            self.__scroll_y = max(0, min(self.__scroll_y, self.__max_scroll))
        
        return None
    
    def dibujar(self):

        if self.__fondo:
            self.__pantalla.blit(self.__fondo, (0, 0))
        else:
            self.__pantalla.fill(CREMA)
        
        contenido_surface = pygame.Surface((self.__ancho, self.__contenido_altura), pygame.SRCALPHA)
        
        y_actual = 150 
        ancho_contenido = 600
        x_centro = self.__ancho // 2
        
        for linea in self.__info_juego["descripcion"]:
            texto = self.__fuente_texto.render(linea, True, GRIS_OSCURO)
            texto_rect = texto.get_rect(center=(x_centro, y_actual))
            contenido_surface.blit(texto, texto_rect)
            y_actual += 30
        
        y_actual += 20
        
        subtitulo = self.__fuente_subtitulo.render("CÓMO JUGAR", True, AZUL_INFO)
        subtitulo_rect = subtitulo.get_rect(center=(x_centro, y_actual))
        contenido_surface.blit(subtitulo, subtitulo_rect)
        y_actual += 40
        
        for linea in self.__info_juego["como_jugar"]:
            texto = self.__fuente_texto.render(linea, True, GRIS_OSCURO)
            texto_rect = texto.get_rect(center=(x_centro, y_actual))
            contenido_surface.blit(texto, texto_rect)
            y_actual += 25
        
        y_actual += 20
        
        subtitulo = self.__fuente_subtitulo.render("MODOS DE JUEGO", True, AZUL_INFO)
        subtitulo_rect = subtitulo.get_rect(center=(x_centro, y_actual))
        contenido_surface.blit(subtitulo, subtitulo_rect)
        y_actual += 40
        
        for modo, descripcion in self.__info_juego["modos"].items():
            modo_texto = self.__fuente_texto.render(f"• {modo}:", True, VERDE_EXITO)
            modo_rect = modo_texto.get_rect(center=(x_centro, y_actual))
            contenido_surface.blit(modo_texto, modo_rect)
            y_actual += 30
            
            for linea in descripcion:
                texto = self.__fuente_texto.render(linea, True, GRIS_OSCURO)
                texto_rect = texto.get_rect(center=(x_centro, y_actual))
                contenido_surface.blit(texto, texto_rect)
                y_actual += 22
            y_actual += 10
        
        y_actual += 20
        
        subtitulo = self.__fuente_subtitulo.render("PROPÓSITO", True, AZUL_INFO)
        subtitulo_rect = subtitulo.get_rect(center=(x_centro, y_actual))
        contenido_surface.blit(subtitulo, subtitulo_rect)
        y_actual += 40
        
        for linea in self.__info_juego["proposito"]:
            texto = self.__fuente_texto.render(linea, True, GRIS_OSCURO)
            texto_rect = texto.get_rect(center=(x_centro, y_actual))
            contenido_surface.blit(texto, texto_rect)
            y_actual += 25
        
        y_actual += 30
        
        subtitulo = self.__fuente_subtitulo.render("AUTORES", True, AZUL_INFO)
        subtitulo_rect = subtitulo.get_rect(center=(x_centro, y_actual))
        contenido_surface.blit(subtitulo, subtitulo_rect)
        y_actual += 40
        
        institucion = self.__fuente_texto.render(self.__autores["institucion"], True, GRIS_OSCURO)
        institucion_rect = institucion.get_rect(center=(x_centro, y_actual))
        contenido_surface.blit(institucion, institucion_rect)
        y_actual += 25
        
        carrera = self.__fuente_texto.render(self.__autores["carrera"], True, GRIS_OSCURO)
        carrera_rect = carrera.get_rect(center=(x_centro, y_actual))
        contenido_surface.blit(carrera, carrera_rect)
        y_actual += 25
        
        detalles = self.__fuente_texto.render(self.__autores["detalles"], True, GRIS_OSCURO)
        detalles_rect = detalles.get_rect(center=(x_centro, y_actual))
        contenido_surface.blit(detalles, detalles_rect)
        y_actual += 35
        
        estudiantes_titulo = self.__fuente_texto.render("Estudiantes:", True, VERDE_EXITO)
        estudiantes_rect = estudiantes_titulo.get_rect(center=(x_centro, y_actual))
        contenido_surface.blit(estudiantes_titulo, estudiantes_rect)
        y_actual += 30
        
        for estudiante in self.__autores["estudiantes"]:
            texto = self.__fuente_texto.render(f"• {estudiante}", True, GRIS_OSCURO)
            texto_rect = texto.get_rect(center=(x_centro, y_actual))
            contenido_surface.blit(texto, texto_rect)
            y_actual += 25
        
        area_visible = pygame.Rect(0, self.__scroll_y, self.__ancho, self.__alto - 100)
        contenido_recortado = contenido_surface.subsurface(area_visible)
        self.__pantalla.blit(contenido_recortado, (0, 0))
        
        if self.__max_scroll > 0:
            self.__dibujar_barra_scroll()
        
        color_boton = GRIS_CLARO if self.__hover_volver else VERDE_EXITO
        pygame.draw.rect(self.__pantalla, color_boton, self.__boton_volver)
        pygame.draw.rect(self.__pantalla, GRIS_OSCURO, self.__boton_volver, 2)
        
        texto_volver = self.__fuente_boton.render("VOLVER", True, BLANCO)
        texto_rect = texto_volver.get_rect(center=self.__boton_volver.center)
        self.__pantalla.blit(texto_volver, texto_rect)
    
    def __dibujar_barra_scroll(self):
        barra_ancho = 20
        barra_x = self.__ancho - barra_ancho - 10
        barra_y = 10
        barra_alto = self.__alto - 120
        
        pygame.draw.rect(self.__pantalla, GRIS_CLARO, (barra_x, barra_y, barra_ancho, barra_alto))
        
        if self.__max_scroll > 0:
            indicador_alto = max(20, int(barra_alto * (self.__alto - 100) / self.__contenido_altura))
            indicador_y = barra_y + int((barra_alto - indicador_alto) * (self.__scroll_y / self.__max_scroll))
            pygame.draw.rect(self.__pantalla, GRIS_OSCURO, (barra_x + 2, indicador_y, barra_ancho - 4, indicador_alto))