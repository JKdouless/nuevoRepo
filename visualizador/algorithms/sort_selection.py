# ...existing code...
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

def step():
    """
    Devuelve:
      - {"a": int, "b": int, "swap": bool, "done": False} para comparaciones o swaps parciales
      - {"done": True} cuando el algoritmo terminó
    Comportamiento por llamada:
      - Fase "buscar": compara items[j] con items[min_idx], actualiza min_idx, avanza j
        y devuelve {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
        Si j alcanza n, cambia a fase "swap" (el swap se hará en la siguiente llamada).
      - Fase "swap": realiza (si corresponde) el único swap entre i y min_idx y lo devuelve
        con "swap": True. Luego avanza i, reinicia j y min_idx, y vuelve a "buscar".
    """
    global items, n, i, j, min_idx, fase

    # Fin rápido si no hay nada que ordenar
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
            # terminamos el barrido de la pasada; preparar swap en la próxima llamada
            fase = "swap"

    if fase == "swap":
        # realizar (o no) el swap entre i y min_idx y devolverlo como acción
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            result = {"a": i, "b": min_idx, "swap": True, "done": False}
        else:
            result = {"a": i, "b": min_idx, "swap": False, "done": False}

        # avanzar a la siguiente cabeza de la parte no ordenada
        i += 1
        if i >= n - 1:
            # próxima llamada retornará done
            j = i + 1
            min_idx = i
            fase = "buscar"
        else:
            j = i + 1
            min_idx = i
            fase = "buscar"

        return result
# ...existing code...