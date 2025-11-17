items = []
n = 0
gaps = []
gap_index = 0
gap = 0
i = 0
j = 0
fase = "comparar"

def init(vals):
    global items, n, gaps, gap_index, gap, i, j, fase
    items = list(vals)
    n = len(items)
    gaps = [2, 1] #gaps posibles
    gap_index = 0 #ind gap
    gap = gaps[gap_index] #valor del gap actual
    i = gap
    j = i
    fase = "comparar"

def step():
    global items, n, gaps, gap_index, gap, i, j, fase
    if gap_index >= len(gaps):
        return {"done": True}
# /////////////fin rapido///////////
    if gap >= n:
        gap_index += 1
        if gap_index >= len(gaps):
            return {"done": True} # termino si no hay mas gaps
# /////////defino///////////
        gap = gaps[gap_index] #q gap uso
        i = gap #equivalgo gap a i para pasar
        j = i #barredor
        fase = "comparar"
        if j >= gap:
            b = j - gap
        else:
            b = j
        return {"a": j, "b": b, "swap": False}
# ///////////////// comparar ///////////////////
    if fase == "comparar":
        if j >= gap and items[j] < items[j - gap]: #posicion en la sublista actual
            fase = "swap"
            if j >= gap:
                b = j - gap
            else:
                b = j
            return {"a": j, "b": b, "swap": False}
        else:
            fase = "avanzar"
            if j >= gap:
                b = j - gap
            else:
                b = j
            return {"a": j, "b": b, "swap": False}
# /////////////// swap ///////////////
    if fase == "swap":
        items[j], items[j - gap] = items[j - gap], items[j] #intercambio con en la sublista del swap
        a, b = j, j - gap
        j -= gap
        fase = "comparar"
        return {"a": a, "b": b, "swap": True}
# /////////////// avanzo ///////////////////
    if fase == "avanzar":
        i += 1
        if i < n:
            j = i
            fase = "comparar"
            if j >= gap:
                b = j - gap
            else:
                b = j
            return {"a": j, "b": b, "swap": False}
        else:
#/////////// cambio de gap /////////////////
            gap_index += 1
            if gap_index >= len(gaps):
                return {"done": True}
            gap = gaps[gap_index]
            i = gap
            j = i
            fase = "comparar"
            if j >= gap:
                b = j - gap
            else:
                b = j
            return {"a": j, "b": b, "swap": False}
# ///////////// terminatres ///////////////////////