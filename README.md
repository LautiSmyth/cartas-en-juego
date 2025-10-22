# Cartas en Juego

Juego educativo de cartas en Python + Pygame que ejercita memoria y lógica. Incluye música y efectos, cronómetro, puntuación y pantalla de créditos. Dos modos de juego y materias seleccionables.

## Modos de juego
- Parejas: encuentra las parejas pregunta–respuesta. Memoriza al inicio, gira cartas, suma puntos por aciertos.
- Intruso: identifica el elemento que no pertenece al conjunto. Avanza niveles con tiempo decreciente.

Materias: Matemáticas, Historia, Química y Geografía.

## Requisitos
- Python 3.10+
- `pygame`

## Instalación y ejecución
1. Descarga/clona el proyecto.
2. Instala dependencias: `pip install pygame`
3. Ejecuta: `python main.py`

Nota: ejecuta el juego desde la carpeta raíz para cargar `Sprite/` y `Sonidos/` correctamente.

## Controles
- Mouse: clic para seleccionar cartas y botones (JUGAR, CRÉDITOS, SALIR).

## Configuración
- Ajustes de ventana y juego en `lib/Var.py`.
- Puntos y tiempos en `lib/config.py`.
- Preguntas y contenidos en `lib/preguntas_parejas.py` y `lib/preguntas_intruso.py`.

## Estructura
- `main.py`: punto de entrada.
- `lib/game.py`: bucle del juego y estados.
- `lib/menu.py`, `lib/modo_parejas.py`, `lib/modo_intruso.py`: lógicas principales.
- `Sprite/` y `Sonidos/`: recursos gráficos y de audio.

## Créditos
Universidad Abierta Interamericana – Ingeniería en Sistemas Informáticos
Turno Noche · Sede Lomas · Comisión 3ºA
Estudiantes: San Martín Santiago, Sassaroli Agustín, Siffredi Agustín, Smyth Lautaro