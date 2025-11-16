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

def step():
    global items, n, i, j

    # Al terminar de ordenar devolvemos "done":True
    if i >= n - 1:
        return {"done": True}

    # Marcamos 2 indices en base a j
    a = j
    b = j + 1

    # Creamos una variable para señalar cuando swapear y cuando no
    swap = False
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzamos
    j += 1

    # Al finalizar una pasada reseteamos j y avanzamos i
    if j >= (n - 1 - i):
        j = 0
        i += 1

     # Hacemos el intercambio correspondiente
    return {"a": a, "b": b, "swap": swap, "done": False}

    