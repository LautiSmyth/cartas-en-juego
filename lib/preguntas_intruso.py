PREGUNTAS_INTRUSO = {
    "Matemáticas": [
        # Números pares vs impar
        ([2, 4, 6, 8, 10], 7, "números pares"),  # 7 es impar entre pares
        ([1, 3, 5, 7, 9], 4, "números impares"),   # 4 es par entre impares
        ([12, 14, 16, 18, 20], 15, "números pares"),  # 15 es impar entre pares
        ([11, 13, 15, 17, 19], 16, "números impares"),   # 16 es par entre impares
        
        # Números primos vs compuesto
        ([2, 3, 5, 7, 11], 9, "números primos"),  # 9 no es primo
        ([4, 6, 8, 9, 10], 7, "números compuestos"),  # 7 es primo entre compuestos
        ([13, 17, 19, 23, 29], 21, "números primos"),  # 21 no es primo
        ([15, 18, 20, 21, 24], 23, "números compuestos"),  # 23 es primo entre compuestos
        
        # Múltiplos de un número
        ([5, 10, 15, 20, 25], 12, "múltiplos de 5"),  # 12 no es múltiplo de 5
        ([3, 6, 9, 12, 15], 8, "múltiplos de 3"),     # 8 no es múltiplo de 3
        ([7, 14, 21, 28, 35], 18, "múltiplos de 7"),  # 18 no es múltiplo de 7
        ([4, 8, 12, 16, 20], 15, "múltiplos de 4"),   # 15 no es múltiplo de 4
        
        # Números de una cifra vs dos cifras
        ([1, 2, 3, 4, 5], 12, "números de una cifra"),      # 12 tiene dos cifras
        ([10, 11, 12, 13, 14], 5, "números de dos cifras"), # 5 tiene una cifra
        ([6, 7, 8, 9, 3], 25, "números de una cifra"),         # 25 tiene dos cifras
        ([22, 23, 24, 25, 26], 8, "números de dos cifras"), # 8 tiene una cifra
        
        # Operaciones básicas
        (["+", "-", "×", "÷", "="], "√", "operaciones básicas"),  # √ no es operación básica
        (["2+3", "4-1", "5×2", "8÷2", "6+4"], "x²", "operaciones aritméticas"),  # x² es algebraica
        
        # Figuras geométricas vs no geométrica
        (["círculo", "cuadrado", "triángulo", "rectángulo", "rombo"], "número", "figuras geométricas"),
        (["esfera", "cubo", "pirámide", "cilindro", "cono"], "línea", "cuerpos geométricos"),
    ],
    
    "Historia": [
        # Fechas del siglo XX vs otra época
        (["1914", "1939", "1969", "1989", "1991"], "1492", "fechas del siglo XX"),  # 1492 es del siglo XV
        (["1901", "1945", "1975", "1985", "1999"], "1776", "fechas del siglo XX"),  # 1776 es del siglo XVIII
        
        # Personajes argentinos vs extranjero
        (["San Martín", "Belgrano", "Sarmiento", "Rivadavia", "Moreno"], "Napoleón", "personajes argentinos"),
        (["Rosas", "Mitre", "Perón", "Evita", "Yrigoyen"], "Churchill", "personajes argentinos"),
        
        # Guerras mundiales vs otro conflicto
        (["Primera Guerra", "Segunda Guerra", "Guerra Fría", "Guerra Vietnam", "Guerra Corea"], "Revolución Francesa", "conflictos del siglo XX"),
        (["Batalla Normandía", "Pearl Harbor", "Hiroshima", "Stalingrado", "D-Day"], "Batalla Waterloo", "eventos Segunda Guerra"),
        
        # Países americanos vs europeo
        (["Argentina", "Brasil", "Chile", "Perú", "Colombia"], "Francia", "países americanos"),
        (["México", "Venezuela", "Ecuador", "Uruguay", "Paraguay"], "Italia", "países americanos"),
        
        # Siglo XIX vs otra época
        (["1810", "1816", "1853", "1880", "1890"], "1969", "fechas del siglo XIX"),
        (["1820", "1845", "1860", "1870", "1895"], "2001", "fechas del siglo XIX"),
        
        # Presidentes argentinos vs extranjero
        (["Rivadavia", "Roca", "Yrigoyen", "Perón", "Alfonsín"], "Kennedy", "presidentes argentinos"),
        (["Menem", "De la Rúa", "Kirchner", "Macri", "Fernández"], "Obama", "presidentes argentinos"),
        
        # Revoluciones vs otro evento
        (["Revolución Francesa", "Revolución Rusa", "Revolución Cubana", "Revolución China", "Revolución Mexicana"], "Renacimiento", "revoluciones"),
        
        # Imperios antiguos vs moderno
        (["Romano", "Griego", "Egipcio", "Persa", "Azteca"], "Británico", "imperios antiguos"),
    ],
    
    "Química": [
        # Elementos vs compuesto
        (["H", "O", "C", "N", "Ca"], "H₂O", "elementos"),  # H₂O es compuesto
        (["Na", "Cl", "K", "Mg", "Al"], "CO₂", "elementos"),  # CO₂ es compuesto
        
        # Gases vs sólido
        (["O₂", "N₂", "CO₂", "CH₄", "NH₃"], "Fe", "gases"),  # Fe es sólido
        (["He", "Ne", "Ar", "Kr", "Xe"], "Cu", "gases nobles"),  # Cu es sólido
        
        # Metales vs no metal
        (["Fe", "Ca", "Na", "Mg", "Al"], "O", "metales"),  # O es no metal
        (["Cu", "Zn", "Pb", "Sn", "Ag"], "S", "metales"),  # S es no metal
        
        # Compuestos orgánicos vs inorgánico
        (["CH₄", "C₂H₆", "C₃H₈", "C₄H₁₀", "C₆H₆"], "NaCl", "compuestos orgánicos"),  # NaCl es inorgánico
        (["C₂H₄", "C₂H₂", "C₆H₁₂", "C₈H₁₈", "C₁₀H₂₂"], "H₂SO₄", "hidrocarburos"),  # H₂SO₄ es inorgánico
        
        # Elementos de una letra vs dos letras
        (["H", "O", "C", "N", "F"], "Ca", "elementos de una letra"),  # Ca tiene dos letras
        (["B", "P", "S", "I", "K"], "Br", "elementos de una letra"),  # Br tiene dos letras
        
        # Ácidos vs base
        (["HCl", "H₂SO₄", "HNO₃", "CH₃COOH", "H₃PO₄"], "NaOH", "ácidos"),  # NaOH es base
        (["NaOH", "KOH", "Ca(OH)₂", "Mg(OH)₂", "NH₄OH"], "HCl", "bases"),  # HCl es ácido
        
        # Estados de la materia
        (["sólido", "líquido", "gaseoso", "plasma", "condensado"], "energía", "estados de la materia"),
        
        # Grupos de la tabla periódica
        (["Li", "Na", "K", "Rb", "Cs"], "Cl", "metales alcalinos"),  
    ],
    
    "Geografía": [
        # Capitales sudamericanas vs europea
        (["Buenos Aires", "Brasilia", "Santiago", "Lima", "Bogotá"], "París", "capitales sudamericanas"),
        (["Caracas", "Quito", "La Paz", "Asunción", "Montevideo"], "Londres", "capitales sudamericanas"),
        
        # Países sudamericanos vs europeo
        (["Argentina", "Brasil", "Chile", "Perú", "Colombia"], "Francia", "países sudamericanos"),
        (["Venezuela", "Ecuador", "Bolivia", "Paraguay", "Uruguay"], "Alemania", "países sudamericanos"),
        
        # Ríos vs montaña
        (["Amazonas", "Nilo", "Misisipi", "Paraná", "Orinoco"], "Everest", "ríos"),
        (["Danubio", "Rin", "Támesis", "Sena", "Volga"], "Aconcagua", "ríos europeos"),
        
        # Continente americano vs otro continente
        (["Argentina", "Brasil", "Estados Unidos", "Canadá", "México"], "Francia", "países americanos"),
        (["Chile", "Colombia", "Venezuela", "Ecuador", "Perú"], "China", "países americanos"),
        
        # Océanos vs mar
        (["Atlántico", "Pacífico", "Índico", "Ártico", "Antártico"], "Mediterráneo", "océanos"),
        (["Atlántico", "Pacífico", "Índico", "Ártico", "Antártico"], "Caribe", "océanos"),
        
        # Montañas vs río
        (["Everest", "Aconcagua", "McKinley", "Kilimanjaro", "Mont Blanc"], "Amazonas", "montañas"),
        (["Andes", "Himalaya", "Alpes", "Rocosas", "Apalaches"], "Nilo", "cordilleras"),
        
        # Países europeos vs americano
        (["Francia", "Italia", "España", "Alemania", "Reino Unido"], "Brasil", "países europeos"),
        (["Suecia", "Noruega", "Dinamarca", "Finlandia", "Islandia"], "Argentina", "países nórdicos"),
        
        # Desiertos vs selva
        (["Sahara", "Gobi", "Atacama", "Kalahari", "Mojave"], "Amazonas", "desiertos"),
        
        # Islas vs continente
        (["Madagascar", "Groenlandia", "Nueva Guinea", "Borneo", "Sumatra"], "África", "islas"),
    ]
}