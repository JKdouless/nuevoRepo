# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

#def step():
    # TODO:
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    # 3) Avanzar punteros (preparar el próximo paso).
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    #
    # Cuando no queden pasos, devolvé {"done": True}.
 #   return {"done": True}


def step():
    global items, n, i, j

    # Fin si termino la wea
    if n <= 1 or i >= n - 1:
        return {"done": True}

    a = j
    b = j + 1
    swap = False

    # Comaparcion y truque si pinta
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Muevo el variables de comparatione 
    j += 1
    if j >= n - 1 - i:
        i += 1
        j = 0

    return {"a": a, "b": b, "swap": swap, "done": False}
# Finiquitacion rapida