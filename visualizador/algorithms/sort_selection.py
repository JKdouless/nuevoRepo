# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

#def step():
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    #return {"done": True}

# Finiquitacion rapida
    if n <= 1 or i >= n - 1:
        return {"done": True}

    if fase == "buscar":
        if j < n:
            j_actual = j
            if items[j] < items[min_idx]:
                min_idx = j
            j += 1
            return {"a": min_idx, "b": j_actual, "swap": False, "done": False}
        else:
            # buscqueda o swap
            fase = "swap"

    if fase == "swap":
        # swap o no swap
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            result = {"a": i, "b": min_idx, "swap": True, "done": False}
        else:
            result = {"a": i, "b": min_idx, "swap": False, "done": False}

        # mover cabeza
        i += 1
        if i >= n - 1:
            # proximo punto de inicio
            j = i + 1
            min_idx = i
            fase = "buscar"
        else:
            j = i + 1
            min_idx = i
            fase = "buscar"

        return result
    #terminado