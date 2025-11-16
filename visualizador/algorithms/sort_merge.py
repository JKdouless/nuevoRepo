items = [] 
cantidad = 0

# Estados del merge sort "simulado".
ancho = 1
izq = 0
medio = 0
der = 0
pi = 0
pj = 0
pk = 0  # puntero para empujar valores
fase = "seleccionar"
valor_rotando = None


def init(vals):
    global items, cantidad, ancho, izq, medio, der, pi, pj, pk, fase, valor_rotando
    
    # Copiamos lo que llegó
    items = list(vals)
    cantidad = len(items)

    # Subbloques de tamaño 1
    ancho = 1
    
    # Reset total
    izq = 0
    medio = der = pi = pj = pk = 0
    valor_rotando = None
    
    # Si ya está ordenado, terminamos
    fase = "seleccionar" if cantidad > 1 else "done"


def step():
    global items, cantidad
    global ancho, izq, medio, der, pi, pj, pk, fase, valor_rotando

    if fase == "done":
        return {"done": True}

    # -------------------------------
    # Buscar qué dos pedazos mezclar
    # -------------------------------
    if fase == "seleccionar":

        # Si ya recorrimos todo este nivel, pasamos al siguiente tamaño
        if izq >= cantidad:
            ancho *= 2
            if ancho >= cantidad:
                fase = "done"
                return {"done": True}
            izq = 0
            return {"a": 0, "b": 0, "swap": False}

        # Límites del bloque izquierdo y derecho
        medio = min(izq + ancho, cantidad)
        der = min(izq + 2 * ancho, cantidad)

        # Si no existe el bloque derecho, saltar
        if medio >= der:
            izq += 2 * ancho
            return {"a": 0, "b": 0, "swap": False}

        # Preparar punteros internos
        pi = izq
        pj = medio
        fase = "comparar"
        return {"a": pi, "b": pj, "swap": False}

    # -------------------------------
    # Comparar elementos de cada bloque
    # -------------------------------
    if fase == "comparar":

        # Alguno se quedó sin elementos
        if pi >= medio or pj >= der:
            izq += 2 * ancho
            fase = "seleccionar"
            return {"a": 0, "b": 0, "swap": False}

        # Caso simple: izquierda va primero → avanzar
        if items[pi] <= items[pj]:
            viejo = pi
            pi += 1
            return {"a": viejo, "b": pj, "swap": False}

        # Caso donde hay que "meter" items[pj] en items[pi]
        valor_rotando = items[pj]
        pk = pj
        fase = "rotar"
        return {"a": pi, "b": pj, "swap": False}

    # -------------------------------
    # Rotación desplazando elementos 1 a 1
    # -------------------------------
    if fase == "rotar":

        # Llegamos a la posición donde debe caer el valor
        if pk <= pi:
            items[pi] = valor_rotando
            pi += 1
            medio += 1
            pj += 1
            fase = "comparar"

            return {"a": pi-1, "b": pi-1, "swap": True}

        # Desplazar un elemento hacia la derecha
        items[pk] = items[pk - 1]
        pk -= 1

        return {"a": pk, "b": pk+1, "swap": True}