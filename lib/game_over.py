import pygame
from .Color import *
from .sonidos import sistema_audio

class GameOver:
    def __init__(self, pantalla, ancho, alto, puntuacion_final, tiempo_total, victoria):
        self.__pantalla = pantalla 
        self.__ancho = ancho  
        self.__alto = alto  
        self.__puntuacion_final = puntuacion_final
        self.__tiempo_total = tiempo_total 
        self.__victoria = victoria
        
        if victoria:
            sistema_audio.reproducir_ganaste()  
        else:
            sistema_audio.reproducir_perdiste() 
        
        self.__fuente_titulo = pygame.font.Font(None, 72)  
        self.__fuente_subtitulo = pygame.font.Font(None, 48)  
        self.__fuente_estadistica = pygame.font.Font(None, 36) 
        self.__fuente_boton = pygame.font.Font(None, 32)
        
        self.crear_botones() 
        self.__tiempo_formateado = self.formatear_tiempo(tiempo_total) 
        self.__mouse_pos = (0, 0)
    
    def crear_botones(self):
        centro_x = self.__ancho // 2 
        centro_x = self.__ancho // 2
        self.__boton_reiniciar = pygame.Rect(centro_x - 120, 420, 240, 60) 
        self.__boton_menu = pygame.Rect(centro_x - 120, 500, 240, 60)
    
    def formatear_tiempo(self, tiempo_segundos):
        if tiempo_segundos < 0:
            tiempo_segundos = 0 
        minutos = int(tiempo_segundos // 60)  
        segundos = int(tiempo_segundos % 60)  
        return f"{minutos:02d}:{segundos:02d}"
    
    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEMOTION: 
            self.__mouse_pos = evento.pos  
            
        elif evento.type == pygame.MOUSEBUTTONDOWN: 
            if self.__boton_reiniciar.collidepoint(evento.pos):
                return {"accion": "reiniciar"}
            elif self.__boton_menu.collidepoint(evento.pos):
                return {"accion": "menu"}        
        return None
    
    def dibujar(self):
        panel_fondo = pygame.Surface((self.__ancho, self.__alto)) 
        panel_fondo.set_alpha(80) 
        panel_fondo.fill(CREMA) 
        self.__pantalla.blit(panel_fondo, (0, 0))
        
        titulo = "¡VICTORIA!" if self.__victoria else "GAME OVER"
        color_titulo = VERDE_EXITO if self.__victoria else ROJO_PRINCIPAL
        texto_titulo = self.__fuente_titulo.render(titulo, True, color_titulo)  
        titulo_rect = texto_titulo.get_rect(center=(self.__ancho // 2, 200))  
        self.__pantalla.blit(texto_titulo, titulo_rect) 
        
        subtitulo = "¡Completaste todos los niveles!" if self.__victoria else "¡Inténtalo de nuevo!"
        texto_subtitulo = self.__fuente_subtitulo.render(subtitulo, True, MARRON_OSCURO)  
        subtitulo_rect = texto_subtitulo.get_rect(center=(self.__ancho // 2, 260)) 
        self.__pantalla.blit(texto_subtitulo, subtitulo_rect)
        
        y_estadisticas = 320
        
        texto_puntuacion = f"Puntuación Final: {self.__puntuacion_final}"
        render_puntuacion = self.__fuente_estadistica.render(texto_puntuacion, True, MARRON_OSCURO)  
        puntuacion_rect = render_puntuacion.get_rect(center=(self.__ancho // 2, y_estadisticas))  
        self.__pantalla.blit(render_puntuacion, puntuacion_rect) 
        
        texto_tiempo = f"Tiempo Total: {self.__tiempo_formateado}"
        render_tiempo = self.__fuente_estadistica.render(texto_tiempo, True, MARRON_OSCURO)  
        tiempo_rect = render_tiempo.get_rect(center=(self.__ancho // 2, y_estadisticas + 50)) 
        self.__pantalla.blit(render_tiempo, tiempo_rect) 
        
        color_reiniciar = AZUL_INFO if self.__boton_reiniciar.collidepoint(self.__mouse_pos) else GRIS_OSCURO  
        pygame.draw.rect(self.__pantalla, color_reiniciar, self.__boton_reiniciar)  
        pygame.draw.rect(self.__pantalla, BLANCO, self.__boton_reiniciar, 3)  
        texto_reiniciar = self.__fuente_boton.render("Jugar de Nuevo", True, BLANCO)  
        reiniciar_rect = texto_reiniciar.get_rect(center=self.__boton_reiniciar.center)  
        self.__pantalla.blit(texto_reiniciar, reiniciar_rect) 
        
        color_menu = AZUL_INFO if self.__boton_menu.collidepoint(self.__mouse_pos) else GRIS_OSCURO 
        pygame.draw.rect(self.__pantalla, color_menu, self.__boton_menu)  
        pygame.draw.rect(self.__pantalla, BLANCO, self.__boton_menu, 3)
        texto_menu = self.__fuente_boton.render("Menú Principal", True, BLANCO)  
        menu_rect = texto_menu.get_rect(center=self.__boton_menu.center)  
        self.__pantalla.blit(texto_menu, menu_rect)
    