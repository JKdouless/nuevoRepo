# TP — Visualización de algoritmos de ordenamiento

Grupo 13 — Comisión 11, 2do Cuatrimestre 2025

👥 Integrantes

Thomas Arias 46534733	@ThomasArias55

Laureano Fernández Safuri	47121801	@JKdouless

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
    
---

## 🔗 Contrato de los archivos `sort_<algo>.py`

### `init(vals)`
Se ejecuta una vez al comenzar (o tras mezclar).  
Debe:
- Guardar copia: `items = list(vals)`  
- Guardar `n = len(items)`  
- Inicializar los punteros o estado interno (`i`, `j`, `min_idx`, pila, etc.)

### `step()`
Se llama muchas veces. Cada llamada realiza **un solo micro-paso** y devuelve un diccionario:

```python
{
  "a": int,     # índice A (0..n-1)
  "b": int,     # índice B (0..n-1)
  "swap": bool, # True si hiciste items[a] <-> items[b]
  "done": bool  # True si el algoritmo terminó
}
```

**Reglas:**
- `0 <= a,b < n`
- Si `swap=True`, el intercambio ya debe haberse realizado:
  ```python
  items[a], items[b] = items[b], items[a]
  return {"a": a, "b": b, "swap": True, "done": False}
  ```
- Al finalizar: `return {"done": True}`
- Actualizá correctamente los punteros/estado en cada paso.

---

## Nuevos algoritmos
- Archivo: `algorithms/sort_<algo>.py`  
- Agregar al `<select id="algorithm">` de `index.html` con `value="<algo>"`  
- No hace falta modificar `index.html` para **Bubble**, **Selection** e **Insertion** 

## ✅ Entregables
- **Obligatorio:**  
  - Carpeta `/algorithms/` con **al menos 3** algoritmos (`bubble`, `selection`, `insertion`)  
  - **Informe** detallado con decisiones y dificultades  
  - **README del equipo** con integrantes y notas de implementación  
- **Opcional:**  
  - Nuevos algoritmos (`quick`, `merge`, `shell`, etc.)  
  - Métricas, benchmarks o mejoras visuales  

---

## ✅ Checklist antes de entregar
- [ ✅ ] Los 3 algoritmos base están implementados y finalizan correctamente  
- [ ✅ ] `init` resetea el estado  
- [ ✅ ] `step` realiza un micro-paso  
- [ ✅ ] Swaps hechos antes de devolver `swap=True`  
- [ ✅ ] Probado con listas vacías, cortas, ordenadas e inversas  
- [  ] Informe y README listos  
