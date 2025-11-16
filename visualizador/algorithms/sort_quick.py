# QuickSort incremental compatible con el visualizador
# Contrato: init(vals), step() -> {a:int, b:int, swap:bool, done:bool}

items = []
n = 0

# Estado
stack = []   # pila de (low, high)
i = None
j = None
pivot = None
phase = None   # "partition", "push_left", "push_right"
done = False

def init(vals):
    global items, n, stack, i, j, pivot, phase, done
    items = list(vals)
    n = len(items)

    stack = [(0, n-1)]  # simulamos recursión
    i = j = None
    pivot = None
    phase = None
    done = False


def step():
    global items, stack, i, j, pivot, phase, done

    if done:
        return {"done": True}

    # Si no hay más segmentos → terminado
    if not stack:
        done = True
        return {"done": True}

    low, high = stack[-1]

    # Segments of length 0 or 1 are already sorted
    if low >= high:
        stack.pop()
        return {"a": 0, "b": 0, "swap": False, "done": False}

    # Si arrancamos un nuevo partition
    if phase is None:
        pivot = pivot_val = items[high]
        i = low - 1
        j = low
        phase = "partition"
        return {"a": high, "b": high, "swap": False, "done": False}  # highlight pivot

    # Fase: recorrer j y comparar
    if phase == "partition":
        if j < high:
            # comparar items[j] con pivot
            if items[j] <= pivot:
                i += 1
                if i != j:
                    # swap durante partition
                    items[i], items[j] = items[j], items[i]
                    res = {"a": i, "b": j, "swap": True, "done": False}
                else:
                    res = {"a": j, "b": j, "swap": False, "done": False}
                j += 1
                return res
            else:
                res = {"a": j, "b": high, "swap": False, "done": False}
                j += 1
                return res

        # terminamos loop → mover pivot
        i += 1
        if i != high:
            items[i], items[high] = items[high], items[i]
            phase = "push_left"
            return {"a": i, "b": high, "swap": True, "done": False}
        else:
            phase = "push_left"
            return {"a": i, "b": high, "swap": False, "done": False}

    # Agregar intervalos a la pila
    if phase == "push_left":
        stack.pop()
        stack.append((low, i-1))
        phase = "push_right"
        return {"a": low, "b": i-1, "swap": False, "done": False}

    if phase == "push_right":
        stack.append((i+1, high))
        phase = None
        return {"a": i+1, "b": high, "swap": False, "done": False}

    return {"done": True}