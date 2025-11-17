# ////////variables///////////////
items = []
cantidad = 0
ancho = 1
izq = 0
medio = 0
der = 0
pi = 0
pj = 0
pk = 0  # puntero para empujar valores
fase = "seleccionar"
valor_rotando = None
# ////////globales////////////////
def init(vals):
    global items, cantidad, ancho, izq, medio, der
    global pi, pj, pk, fase, valor_rotando
    items = list(vals)
    cantidad = len(items)
    ancho = 1
    izq = 0
    medio = der = pi = pj = pk = 0
    valor_rotando = None
    fase = "seleccionar" if cantidad > 1 else "done"
# ///////////step///////////////////////
def step():
    global items, cantidad
    global ancho, izq, medio, der, pi, pj, pk, fase, valor_rotando
    if fase == "done":
        return {"done": True}
# /////////selec sublistas///////////////////////
    if fase == "seleccionar":
        if izq >= cantidad:
            ancho *= 2
            if ancho >= cantidad:
                fase = "done"
                return {"done": True}
            izq = 0
            return {"a": 0, "b": 0, "swap": False}
        medio = min(izq + ancho, cantidad)
        der = min(izq + 2 * ancho, cantidad)
        pi = izq
        pj = medio
        fase = "comparar"
        return {"a": pi, "b": pj, "swap": False}
# /////////comparo sublistas/////////////
    if fase == "comparar":
        if pi >= medio or pj >= der:
            izq += 2 * ancho
            fase = "seleccionar"
            return {"a": -1, "b": -1, "swap": False}
        if items[pi] <= items[pj]:
            viejo = pi
            pi += 1
            return {"a": viejo, "b": pj, "swap": False}
        valor_rotando = items[pj]
        pk = pj
        fase = "rotar"
        return {"a": pi, "b": pj, "swap": False}
# //////// rotacion ////////////////
    if fase == "rotar":
        if pk <= pi:
            items[pi] = valor_rotando
            pi += 1
            medio += 1
            pj += 1
            fase = "comparar"
            return {"a": pi - 1, "b": pi - 1, "swap": True}
        items[pk] = items[pk - 1]
        pk -= 1
        return {"a": pk, "b": pk + 1, "swap": True}
#///////////////////fin////////////////