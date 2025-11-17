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
  index.html                     
  /algorithms/
    sort_bubble.py
    sort_selection.py
    sort_merge.py
    sort_quick.py
    sort_insertion.py
    sort_shell.py
    
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
- **Insertion**:
#
- **Selection**:
#
- **Merge**:
#
- **Quick**:
#
- **Shell**:
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
