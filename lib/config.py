from .preguntas_parejas import DATOS_MATERIAS
from .Color import *

CONFIG_PAREJAS = {
    "puntos_acierto": 50,
    "puntos_error": -35,
    "tiempo_cronometro": 120,
    "cartas_por_nivel": 6
}

CONFIG_INTRUSO = {
    "cartas_por_nivel": 6,
    "tiempo_cronometro": {
        1: 30,  # Nivel 1: 30 segundos
        2: 25,  
        3: 20,  
        4: 15,  
        5: 10   
    },
    "tiempo_espera_nivel": 5,           
    "puntos_acierto": 50,              
    "puntos_error": -40,                
    "puntos_tiempo_bonus": 10,         
    "niveles_maximos": 5
}

CONFIG_VENTANA = {
    "ancho": 1024,
    "alto": 768,
    "fps": 60,
    "titulo": "Cartas en Juego"
}

COLORES = {
    "fondo": (50, 100, 150),
    "carta_frente": BLANCO,
    "carta_atras": (70, 130, 180),
    "texto": NEGRO,
    "texto_blanco": BLANCO,
    "boton": (70, 130, 180),
    "boton_hover": (100, 149, 237),
    "boton_seleccionado": (255, 215, 0),
    "cronometro_normal": BLANCO,
    "cronometro_alerta": (255, 0, 0)
}

DIMENSIONES = {
    "carta_ancho": 120,
    "carta_alto": 160,
    "margen_cartas": 20,
    "cronometro_ancho": 200,
    "cronometro_alto": 80,
    "puntuacion_ancho": 200,
    "puntuacion_alto": 80
}