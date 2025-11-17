items = []
n = 0
gaps = []
gap_index = 0
gap = 0
i = 0
j = 0
fase = "comparar"
temp = None  # Para guardar el valor que se desplaza

# ///////////////////// Inicialización /////////////////////
def init(vals):
    global items, n, gaps, gap_index, gap, i, j, fase, temp
    items = list(vals)
    n = len(items)
    # Secuencia de Knuth
    h = 1
    gaps = []
    while h < n:
        gaps.insert(0, h)  # de mayor a menor
        h = 3*h + 1
    gap_index = 0           # índice del gap actual
    gap = gaps[gap_index]   # valor del gap actual
    i = gap                 # puntero de inicio
    j = i                   # puntero de comparación/desplazamiento
    fase = "comparar"
    temp = None

# ///////////////////// Paso a paso /////////////////////
def step():
    global items, n, gaps, gap_index, gap, i, j, fase, temp
    
    # ///////////////////// Fin del algoritmo /////////////////////
    if gap_index >= len(gaps):
        return {"done": True}

    # ///////////////////// Inicializar temp /////////////////////
    if fase == "comparar" and temp is None:
        temp = items[j]

    # ///////////////////// Comparar para desplazar /////////////////////
    if fase == "comparar":
        if j >= gap and items[j - gap] > temp:
            # desplaza el elemento hacia la derecha
            items[j] = items[j - gap]
            a, b = j, j - gap
            j -= gap
            return {"a": a, "b": b, "swap": True}
        else:
            # colocar temp en su posición final
            items[j] = temp
            a, b = j, j
            fase = "avanzar"
            return {"a": a, "b": b, "swap": True}

    # ///////////////////// Avanzar al siguiente elemento /////////////////////
    if fase == "avanzar":
        i += 1
        if i < n:
            j = i
            temp = None
            fase = "comparar"
            a = j
            b = j - gap if j >= gap else j
            return {"a": a, "b": b, "swap": False}
        else:
            # ///////////////////// Cambio de gap /////////////////////
            gap_index += 1
            if gap_index >= len(gaps):
                return {"done": True}
            gap = gaps[gap_index]
            i = gap
            j = i
            temp = None
            fase = "comparar"
            a = j
            b = j - gap if j >= gap else j
            return {"a": a, "b": b, "swap": False}
