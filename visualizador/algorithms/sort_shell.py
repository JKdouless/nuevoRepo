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

    gaps = [2, 1]           # ← lo que pediste
    gap_index = 0
    gap = gaps[gap_index]

    i = gap
    j = i

    fase = "comparar"


def step():
    global items, n, gaps, gap_index, gap, i, j, fase

    # Si ya pasamos todos los gaps → terminado
    if gap_index >= len(gaps):
        return {"done": True}

    # Si el gap es mayor que n, saltamos al siguiente
    if gap >= n:
        gap_index += 1
        if gap_index >= len(gaps):
            return {"done": True}
        gap = gaps[gap_index]
        i = gap
        j = i
        fase = "comparar"
        return {"a": j, "b": j-gap if j >= gap else j, "swap": False}

    # --------------- FASE COMPARAR ----------------
    if fase == "comparar":

        if j >= gap and items[j] < items[j - gap]:
            fase = "swap"
            return {"a": j, "b": j - gap, "swap": False}

        else:
            fase = "avanzar"
            return {"a": j, "b": j - gap if j >= gap else j, "swap": False}

    # --------------- FASE SWAP --------------------
    if fase == "swap":
        items[j], items[j - gap] = items[j - gap], items[j]
        a, b = j, j - gap
        j -= gap
        fase = "comparar"
        return {"a": a, "b": b, "swap": True}

    # --------------- FASE AVANZAR -----------------
    if fase == "avanzar":
        i += 1
        if i < n:
            j = i
            fase = "comparar"
            return {"a": j, "b": j - gap if j >= gap else j, "swap": False}

        else:
            # Terminado este gap → pasar al siguiente
            gap_index += 1

            if gap_index >= len(gaps):
                return {"done": True}

            gap = gaps[gap_index]
            i = gap
            j = i
            fase = "comparar"

            return {"a": j, "b": j - gap if j >= gap else j, "swap": False}