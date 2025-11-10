# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
I = 0
J = 0
P = 0

def init(vals):
    global items, n
    items = list(vals)
    n = len(items)
    P = n-1 #pivote inicial
    i = 0
    
    

def step():
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    return {"done": True}
