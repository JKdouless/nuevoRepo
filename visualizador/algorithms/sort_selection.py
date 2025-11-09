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

def step():
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    return {"done": True}
d
ef step():
    i=0
    aux=0
    for i in range(0,n-1):
        if fase=="buscar":
            if items[i] < items[j]:
                min_idx=i
                i+=1
                aux=lista[i]
                items[i]=items[j]
                items[j]=aux
            return{"a":min_idx,"b":j_actual,"swap":False,"done":False}

    if lista[i] == n-1:
        lista[]=lista[min_idx]
        paso=1
   
if i==n-1:
    return{"done":True}


for i in range(0,n-1):
    paso=0