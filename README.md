# TP — Visualización de algoritmos de ordenamiento

## 👥 Integrantes

Grupo 13 — Comisión 11, 2do Cuatrimestre 2025

**Thomas Arias 46534733	@ThomasArias55**

**Laureano Fernández Safuri	47121801	@JKdouless**

---

## Objetivos
- Implementar **Bubble**, **Selection** e **Insertion** cumpliendo el **contrato** `init(vals)` + `step()` que usa la UI.
- Ver el algoritmo **animado** y **paso a paso** (una operación por llamada a `step`).
- Agregar los algoritmos extra **Merge**, **Quick** y **Shell**.

---

## ¿Qué es un algoritmo de ordenamiento?
Un algoritmo de ordenamiento es un procedimiento que re-acomoda una colección según un criterio (números, palabras, objetos por propiedad, etc.).  
Existen múltiples estrategias (Bubble, Selection, Insertion, Quick, Merge, Shell, Heap…), cada una con una idea distinta para comparar e intercambiar elementos.

---

## 📦 Estructura del repositorio
```
/visualizador/               
  /algorithms/
    sort_bubble.py
    sort_selection.py
    sort_merge.py
    sort_quick.py
    sort_insertion.py
    sort_shell.py
    index.html   
  .gitignore
  README.md
    
```
---

## Notas de implementacion

- **Bubble**: Se implemento el algoritmo bubble de tal manera que cada llamada a `step` realiza una única comparación (y posible swap) entre dos elementos consecutivos:
  
1. Compara `items[j]` y ``items[j+1]``

2. Si están desordenados, los intercambia (``swap = True``)

3. Avanza ``j``

4. Si ``j`` llegó al límite de la pasada, se reinicia ``j = 0`` y se incrementa ``i``

5. Cuando ``i >= n - 1``, se retorna ``done = True``

#
- **Insertion**: Se implemento el algoritmo insertion de modo que:

1. Cuando ``j is None``, se inicializa ``j = i`` y se muestra el estado sin swap.

2. Mientras ``items[j-1]`` > ``items[j]``, se hace un swap adyacente y se decrementa ``j``.

3. Cuando ya no hay que mover más el elemento se incrementa ``i`` y se resetea ``j = None``

4. Cuando ``i >= n``, se retorna ``{"done": True}``

#
- **Selection**: se implemento el algoritmo selection de modo que:

1. se inicializa ``min_idx = i`` y ``j = i + 1``

2. ``Fase "buscar"``: Se recorre la zona no ordenada y retorna cada comparación ``(swap=False)``, con cada elemento menor se actualiza ``min_idx``

3. ``Fase "swap"``: Se hace un  swap entre ``i`` y ``min_idx``, Se retorna ``swap=True``

4. Setea ``i`` para la próxima pasada, ``(i += 1)``

5. Cuando ``i >= n - 1``, retorna ``{"done": True}``
  
#
- **Merge**: Se implemento el algoritmo merge usando fases:

1. ``fase == "seleccionar"``: Si ya hemos recorrido toda la lista para ese ancho ``izq >= cantidad`` dobla el ancho, si no reinicia ``izq = 0``
   
2. Establece los límites (``izq``, ``medio``, ``der``) y punteros (``pi``, ``pj``) de la lista y cambia a ``fase = "comparar"``

    se retorna: ``"swap": False`` y señalamos los dos punteros para visualización

3. ``fase == "comparar"``: Si una de las sublistas se terminó ``pi >= medio or pj >= der`` duplica el ancho: ``izq += 2*ancho``, y vuelve a seleccionar ``fase = "seleccionar"``

    retorna ``"swap": False``

4. Si ``items[pj] < items[pi]``: se prepara para rotar: ``valor_rotando = items[pj]``, ``pk = pj``, ``fase = "rotar"``

    muestra ``pi`` y ``pj`` sin swapear

5. ``fase == "rotar"``: Si ``pk > pi`` desplaza un elemento a la derecha: ``items[pk] = items[pk-1]``, ``pk -= 1``

   cada step retorna ``{"a": pk, "b": pk+1, "swap": True}`` hasta que ``pk <= pi``

6. Ajusta los punteros: ``pi += 1``, ``medio += 1``, ``pj += 1`` y vuelve a ``fase = "comparar"``

7. cuando ``ancho >= cantidad`` finaliza ``"done" = True``

#
- **Quick**: Se implemento un algoritmo quicksort de modo que:
  
1. Si la lista tiene más de 1 elemento, se apila de en el ``stack=[[low, high, i, j, fase]]``
   
    ``low``, ``high`` = primero y ultimo actual
, ``i``, ``j`` = punteros internos
, ``fase == "partition"``

3. ``fase == "partition"``: se setea el pivote ``p`` como el ultimo de la lista acutal ``p = items[high]``
   
4. Se recorre con ``j`` desde ``low`` hasta ``high-1``

   en cada paso si ``items[j] <= p`` se swappean ``items[i]`` e ``items[j]`` y se incrementa ``i``

   si ``items[j] > p`` se muestran en el visualizador sin swapear ``swap=False``

   Siempre incrementa ``j``

5. Cuando ``j == high``, la fase termina y se hace swap entre ``items[i]`` y ``items[high]``, dejando el pivote en su lugar definitivo y se setea el índice ``mid = i`` guardando la posición final del pivote.

6. Se sacan los datos del stack actual ``(pop)`` y se añaden los datos de las sublistas para repetir el proceso

    Si la parte derecha tiene elementos ``(mid+1 < high)``, se añade al stack ``[mid+1, high, mid+1, mid+1, "partition"]``

    Si la parte izquierda tiene elementos ``(low < mid-1)``, se añade al stack ``[low, mid-1, low, low, "partition"]``

7. Se recorren las sublistas de la misma manera que la lista original

8. Cuando el stack queda vacío al ordenar todas las sublistas retorna: ``{"done": True}``

#
- **Shell**: Se implemento el algoritmo shell de modo que:

 1. Se define la distancia entre los numeros a comparar de modo que

    ``gaps = [2, 1]``, ``gap_index = 0``, ``gap = gaps[gap_index]``

2. Se setea ``i = gap`` , ``j = i`` y ``fase = "comparar"``

3.  Si el gap actual es mayor o igual al tamaño de la lista ``gap >= n``, se pasa al siguiente ``gap_index += 1``

4. ``fase == "comparar"``: Compara elementos separados por gap ``if items[j] < items[j-gap]`` si necesita moverlos setea ``fase = "swap"`` si no ``fase = "avanzar"``
  y muestra los valores en el visualizador sin swapear
  
6. ``Fase == "swap"``: Intercambia los elementos separados por gap ``items[j], items[j-gap] = items[j-gap], items[j]``

    ``j -= gap`` (como en inserción sobre sublista)

    Retorna ``"swap"=True`` y vuelve a ``fase = "comparar"``

7. ``Fase == "avanzar"``: Avanza ``i += 1`` y si  ``i < n:`` se setea ``j = i`` y vuelve a ``fase = "comparar"``

    Si ``i >= n:``: se pasa al siguiente gap ``gap_index += 1``, se reinicia ``i = gap`` y ``j = i`` y vuelve a comparar ``fase = "comparar"``

8. Cuando no quedan gaps ``gap_index >= len(gaps)`` finaliza ``{"done": True}``
  
#
- **Visualizador**:
  
---

## ✅ Checklist antes de entregar
- [ ✅ ] Los 3 algoritmos base están implementados y finalizan correctamente  
- [ ✅ ] `init` resetea el estado  
- [ ✅ ] `step` realiza un micro-paso  
- [ ✅ ] Swaps hechos antes de devolver `swap=True`  
- [ ✅ ] Probado con listas vacías, cortas, ordenadas e inversas  
- [  ] Informe y README listos  
