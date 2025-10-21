import pygame
import sys
from lib.game import Game
from lib.Var import ANCHO_VENTANA, ALTO_VENTANA, FPS, TITULO_JUEGO

def main():
    pygame.init()
    
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption(TITULO_JUEGO)
    
    reloj = pygame.time.Clock()
    
    juego = Game(pantalla, ANCHO_VENTANA, ALTO_VENTANA)
    
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            else:
                resultado = juego.manejar_evento(evento)
                if resultado and resultado.get("accion") == "salir":
                    ejecutando = False
        
        resultado = juego.actualizar()
        if resultado == "salir":
            ejecutando = False
        
        juego.dibujar()
        pygame.display.flip()
        reloj.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()