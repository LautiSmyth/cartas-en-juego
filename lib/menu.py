import pygame
import os
from .Color import *
from .Var import *
from .sonidos import sistema_audio

class Menu:
    def __init__(self, pantalla, ancho, alto):
        self.pantalla = pantalla  
        self.ancho = ancho  
        self.alto = alto  
        
        sistema_audio.iniciar_musica_menu()
        

        self.fondo_menu = pygame.image.load(os.path.join("Sprite", "Fondo", "fondomenu.png")).convert_alpha() 
        self.fondo_menu = pygame.transform.smoothscale(self.fondo_menu, (ancho, alto)) 
        
        self.fuente_titulo = pygame.font.SysFont("Comic Sans MS", 70)
        self.fuente_subtitulo = pygame.font.SysFont("Comic Sans MS", 38)
        self.fuente_boton = pygame.font.SysFont("Comic Sans MS", 28)
        self.fuente_texto = pygame.font.SysFont("Comic Sans MS", 28)
        
        self.modos = ["Parejas", "Intruso"] 
        self.materias = ["Matemáticas", "Historia", "Química", "Geografía"] 
        
        self.modo_seleccionado = 0  
        self.materia_seleccionada = 0 

        self.crear_botones()
    
    def crear_botones(self):
        self.botones_modo = []
        for i, modo in enumerate(self.modos):
            x = self.ancho // 2 - 190 + i * 200 
            y = 220 
            rect = pygame.Rect(x, y, 180, 50)
            self.botones_modo.append(rect)
        
        self.botones_materia = []
        for i, materia in enumerate(self.materias):
            x = self.ancho // 2 - 390 + i * 200  
            y = 370 
            rect = pygame.Rect(x, y, 180, 50)  
            self.botones_materia.append(rect)

        self.boton_jugar = pygame.Rect(self.ancho // 2 - 100, 480, 200, 60) 
        self.boton_creditos = pygame.Rect(self.ancho // 2 - 100, 550, 200, 60)  
        self.boton_salir = pygame.Rect(self.ancho // 2 - 100, 620, 200, 60) 
    
    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos() 
            
            for i, boton in enumerate(self.botones_modo):
                if boton.collidepoint(pos): 
                    self.modo_seleccionado = i
            
            for i, boton in enumerate(self.botones_materia):
                if boton.collidepoint(pos):  
                    self.materia_seleccionada = i 
            
            if self.boton_jugar.collidepoint(pos):  
                sistema_audio.reproducir_iniciar_juego()
                materia_activa = [self.materias[self.materia_seleccionada]]
                modo = self.modos[self.modo_seleccionado].lower()
                return {
                    "accion": modo,
                    "materias": materia_activa
                }
            
            if self.boton_creditos.collidepoint(pos):  
                return {"accion": "creditos"} 
            
            if self.boton_salir.collidepoint(pos): 
                return {"accion": "salir"}  
        
        return None 
    
    def dibujar(self):
        self.pantalla.blit(self.fondo_menu, (0, 0))  

        subtitulo_modo = self.fuente_subtitulo.render("Selecciona Modo:", True, MARRON_OSCURO)  
        subtitulo_modo_rect = subtitulo_modo.get_rect(center=(self.ancho // 2, 180))  
        self.pantalla.blit(subtitulo_modo, subtitulo_modo_rect) 
        
        for i, (boton, modo) in enumerate(zip(self.botones_modo, self.modos)):
            color = AMARILLO_DORADO if i == self.modo_seleccionado else CORAL
            pygame.draw.rect(self.pantalla, color, boton) 
            pygame.draw.rect(self.pantalla, NEGRO, boton, 2)  
            
            texto = self.fuente_boton.render(modo, True, NEGRO)  
            texto_rect = texto.get_rect(center=boton.center)  
            self.pantalla.blit(texto, texto_rect)  
        
        subtitulo_materia = self.fuente_subtitulo.render("Selecciona Materia:", True, MARRON_OSCURO)  
        subtitulo_materia_rect = subtitulo_materia.get_rect(center=(self.ancho // 2, 330))  
        self.pantalla.blit(subtitulo_materia, subtitulo_materia_rect) 
        
        for i, (boton, materia) in enumerate(zip(self.botones_materia, self.materias)):
            color = AMARILLO_DORADO if i == self.materia_seleccionada else CORAL
            pygame.draw.rect(self.pantalla, color, boton)  
            pygame.draw.rect(self.pantalla, NEGRO, boton, 2)  
            
            texto = self.fuente_texto.render(materia, True, NEGRO)  
            texto_rect = texto.get_rect(center=boton.center)  
            self.pantalla.blit(texto, texto_rect) 
        
        pygame.draw.rect(self.pantalla, ROJO_PRINCIPAL, self.boton_jugar) 
        pygame.draw.rect(self.pantalla, NEGRO, self.boton_jugar, 3) 
        texto_jugar = self.fuente_boton.render("JUGAR", True, BLANCO)  
        texto_jugar_rect = texto_jugar.get_rect(center=self.boton_jugar.center)  
        self.pantalla.blit(texto_jugar, texto_jugar_rect)  
        
        pygame.draw.rect(self.pantalla, AZUL_INFO, self.boton_creditos)  
        pygame.draw.rect(self.pantalla, NEGRO, self.boton_creditos, 3) 
        texto_creditos = self.fuente_boton.render("CRÉDITOS", True, BLANCO)  
        texto_creditos_rect = texto_creditos.get_rect(center=self.boton_creditos.center)  
        self.pantalla.blit(texto_creditos, texto_creditos_rect)  
        
        pygame.draw.rect(self.pantalla, GRIS_OSCURO, self.boton_salir)  
        pygame.draw.rect(self.pantalla, NEGRO, self.boton_salir, 3)  
        texto_salir = self.fuente_boton.render("SALIR", True, BLANCO)  
        texto_salir_rect = texto_salir.get_rect(center=self.boton_salir.center) 
        self.pantalla.blit(texto_salir, texto_salir_rect)