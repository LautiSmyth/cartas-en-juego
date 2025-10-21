from .menu import Menu
from .modo_parejas import ModoParejas
from .modo_intruso import ModoIntruso
from .game_over import GameOver
from Creditos import Creditos
from .Color import *
from .Var import *

class Game:
    MENU = "menu"
    PAREJAS = "parejas"
    INTRUSO = "intruso"
    GAME_OVER = "game_over"
    CREDITOS = "creditos"
    
    def __init__(self, pantalla, ancho, alto):
        self.__pantalla = pantalla
        self.__ancho = ancho
        self.__alto = alto
        self.__estado_actual = self.MENU  
        
        self.__menu = Menu(pantalla, ancho, alto)
        self.__modo_parejas = None  
        self.__modo_intruso = None  
        self.__game_over = None     
        self.__creditos = None      
    
        self.__puntuacion_final = 0
        self.__tiempo_total = 0
        
        self.__materias_seleccionadas = []
    
    def manejar_evento(self, evento):
        if self.__estado_actual == self.MENU:
            resultado = self.__menu.manejar_evento(evento)
            if resultado:
                if resultado["accion"] == "parejas":
                    self.__materias_seleccionadas = resultado["materias"]
                    self.iniciar_modo_parejas()
                elif resultado["accion"] == "intruso":
                    self.__materias_seleccionadas = resultado["materias"]
                    self.iniciar_modo_intruso()
                elif resultado["accion"] == "creditos":
                    self.mostrar_creditos()
                elif resultado["accion"] == "salir":
                    return {"accion": "salir"}
        
        elif self.__estado_actual == self.PAREJAS:
            if self.__modo_parejas:
                resultado = self.__modo_parejas.manejar_evento(evento)
                if resultado:
                    if resultado["estado"] == "game_over":
                        self.__puntuacion_final = resultado["puntuacion"]
                        self.__tiempo_total = resultado["tiempo"]
                        self.iniciar_game_over(resultado["victoria"])
        
        elif self.__estado_actual == self.INTRUSO:
            if self.__modo_intruso:
                resultado = self.__modo_intruso.manejar_evento(evento)
                if resultado:
                    if resultado["estado"] == "game_over":
                        # Guardar datos y mostrar pantalla final
                        self.__puntuacion_final = resultado["puntuacion"]
                        self.__tiempo_total = resultado["tiempo"]
                        self.iniciar_game_over(resultado["victoria"])
        
        elif self.__estado_actual == self.GAME_OVER:
            if self.__game_over:
                resultado = self.__game_over.manejar_evento(evento)
                if resultado:
                    if resultado["accion"] == "reiniciar":
                        if self.__modo_parejas:
                            self.iniciar_modo_parejas()
                        elif self.__modo_intruso:
                            self.iniciar_modo_intruso()
                    elif resultado["accion"] == "menu":
                        self.volver_al_menu()
        
        elif self.__estado_actual == self.CREDITOS:
            if self.__creditos:
                resultado = self.__creditos.manejar_evento(evento)
                if resultado:
                    if resultado["accion"] == "menu":
                        self.volver_al_menu()
    
    def actualizar(self):
        if self.__estado_actual == self.PAREJAS and self.__modo_parejas:
            resultado = self.__modo_parejas.actualizar()
            if resultado and resultado["estado"] == "game_over":
                self.__puntuacion_final = resultado["puntuacion"]
                self.__tiempo_total = resultado["tiempo"]
                self.iniciar_game_over(resultado["victoria"])
                
        elif self.__estado_actual == self.INTRUSO and self.__modo_intruso:
            resultado = self.__modo_intruso.actualizar()
            if resultado and resultado["estado"] == "game_over":
                self.__puntuacion_final = resultado["puntuacion"]
                self.__tiempo_total = resultado["tiempo"]
                self.iniciar_game_over(resultado["victoria"])
    
    def dibujar(self):
        if self.__estado_actual == self.MENU:
            self.__menu.dibujar()
        elif self.__estado_actual == self.PAREJAS and self.__modo_parejas:
            self.__modo_parejas.dibujar()
        elif self.__estado_actual == self.INTRUSO and self.__modo_intruso:
            self.__modo_intruso.dibujar()
        elif self.__estado_actual == self.GAME_OVER and self.__game_over:
            self.__game_over.dibujar()
        elif self.__estado_actual == self.CREDITOS and self.__creditos:
            self.__creditos.dibujar()
    
    def iniciar_modo_parejas(self):
        self.__estado_actual = self.PAREJAS
        materia_seleccionada = self.__materias_seleccionadas[0] if self.__materias_seleccionadas else "Matemáticas"
        self.__modo_parejas = ModoParejas(self.__pantalla, self.__ancho, self.__alto, materia_seleccionada)
        self.__modo_intruso = None
        self.__game_over = None
    
    def iniciar_modo_intruso(self):
        self.__estado_actual = self.INTRUSO
        self.__modo_intruso = ModoIntruso(self.__pantalla, self.__ancho, self.__alto, self.__materias_seleccionadas)
        self.__modo_parejas = None
        self.__game_over = None
    
    def iniciar_game_over(self, victoria):
        self.__estado_actual = self.GAME_OVER
        self.__game_over = GameOver(
            self.__pantalla, 
            self.__ancho, 
            self.__alto, 
            self.__puntuacion_final, 
            self.__tiempo_total,
            victoria
        )
    
    def mostrar_creditos(self):
        self.__estado_actual = self.CREDITOS
        self.__creditos = Creditos(self.__pantalla, self.__ancho, self.__alto)
        
    def volver_al_menu(self):
        self.__estado_actual = self.MENU
        self.__modo_parejas = None
        self.__modo_intruso = None
        self.__game_over = None
        self.__creditos = None