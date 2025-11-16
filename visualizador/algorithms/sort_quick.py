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
    p = round(n/2) #pivote inicial
    m = 0
    i = 0 
    j = 0
    sublist = []


    
def step():
    global items, n, p ,m, i ,j, sublist
    
    j = i

    if items[j] < items[p]:
        i+=1
        return {"a": j, "b": p, "swap":  False, "done": False}
    else:
    
        
    if i > n:
        return {"done": True}
        