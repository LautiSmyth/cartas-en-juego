import pygame
import os

class SistemaAudio:
    def __init__(self):
        pygame.mixer.init()
        self.sonidos = {}
        self.musica_activa = False
        self.volumen_efectos = 0.7
        self.volumen_musica = 0.5
        
        self.cargar_sonidos()
    
    def cargar_sonidos(self):
        ruta_sonidos = os.path.join("Sonidos")
        
        self.sonidos['correcto'] = pygame.mixer.Sound(os.path.join(ruta_sonidos, "Correcto.mp3"))
        self.sonidos['incorrecto'] = pygame.mixer.Sound(os.path.join(ruta_sonidos, "Incorrecto.mp3"))
        self.sonidos['ganaste'] = pygame.mixer.Sound(os.path.join(ruta_sonidos, "Ganaste.mp3"))
        self.sonidos['perdiste'] = pygame.mixer.Sound(os.path.join(ruta_sonidos, "Perdiste.mp3"))
        self.sonidos['iniciar'] = pygame.mixer.Sound(os.path.join(ruta_sonidos, "Iniciarminijuego.mp3"))
        
        for sonido in self.sonidos.values():
            sonido.set_volume(self.volumen_efectos)
            
        self.musica_menu = os.path.join(ruta_sonidos, "MusicaMenu.mp3")
    
    def reproducir_efecto(self, nombre_sonido):
        if nombre_sonido in self.sonidos and self.sonidos[nombre_sonido]:
            self.sonidos[nombre_sonido].play()
    
    def iniciar_musica_menu(self):
        pygame.mixer.music.load(self.musica_menu)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play(-1) 
        self.musica_activa = True

    def reproducir_correcto(self):
        self.reproducir_efecto('correcto')
    
    def reproducir_incorrecto(self):
        self.reproducir_efecto('incorrecto')
    
    def reproducir_ganaste(self):
        self.reproducir_efecto('ganaste')
    
    def reproducir_perdiste(self):
        self.reproducir_efecto('perdiste')
    
    def reproducir_iniciar_juego(self):
        self.reproducir_efecto('iniciar')

sistema_audio = SistemaAudio()