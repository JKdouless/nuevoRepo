items = []
stack = []
n = 0
done = False

def init(vals):
    global items, stack, n, done
    items = list(vals)
    n = len(items)
    stack = []
    done = False
    
    if n > 1:
        stack.append([0, n-1, 0, 0, "partition"])

def step():
    global items, stack, done

    # Al finalizar

    if done:
        return {"done": True}

    if not stack:
        done = True
        return {"done": True}


    low, high, i, j, fase = stack[-1]

    # Al empezar seteamos el pivote 
    p = items[high]

    # Empezamos la primera fase
    if fase == "partition":
        if j < high:
            # Comparamos j con el pivote
            if items[j] <= p:
                items[i], items[j] = items[j], items[i]
                res = {"a": i, "b": j, "swap": True, "done": False}
                i += 1
            else:
                res = {"a": j, "b": high, "swap": False, "done": False}
            j += 1
            stack[-1] = [low, high, i, j, "partition"]
            return res
        else:
            # Al terminar de ordenar seteamos el pivote
            items[i], items[high] = items[high], items[i]
            mid = i
            stack.pop()

            # Agregamos las sublistas pendientes al stack
            if mid+1 < high:
                stack.append([mid+1, high, mid+1, mid+1, "partition"])
            if low < mid-1:
                stack.append([low, mid-1, low, low, "partition"])

            return {"a": i, "b": high, "swap": True, "done": False}
