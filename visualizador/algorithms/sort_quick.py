# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
sublist = []
n = 0
i = 0
j = 0
p = 0
m = 0

def init(vals):
    global items, n, p, i, j
    items = list(vals) 
    n = len(items) 
    p = n-1 #pivote inicial
    m = #guardo la posicion de un numero especifico para swapear
    i = 0 
    j = i
    sublist = []


    
def step():
    global items, n, p , i ,j, sublist
    
    if i > n:
        return {"done": True}

    if items[j] > items[p]:
        if items [j] > items[j+1]:
            items[j], items[j+1] = items[j+1], items[j]
            

        



    return {"done": True}
