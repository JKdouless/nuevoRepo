items = []
n = 0
i = 0
j = 0
min_idx = 0
fase = "buscar"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    if i >= n - 1:
        return {"done": True}
        

    if fase == "buscar":
        if j < n:
            if items[j] < items[min_idx]:
                min_idx = j
            j_actual = j
            j += 1
            return {"a": i, "b": j_actual, "swap": False}
        else:
            fase = "swap"
    if fase == "swap":
        items[i], items[min_idx] = items[min_idx], items[i]
        a, b = i, min_idx
        i += 1
        if i <= n - 1:
            j = i + 1
            min_idx = i
            fase = "buscar"
            return {"a": a, "b": b, "swap": True}
        else:
            return{"a": items[n-1],"b": items[n],"done": True}
        