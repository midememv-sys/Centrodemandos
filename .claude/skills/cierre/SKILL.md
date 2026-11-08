---
name: cierre
description: Cierre del día de Bruno en el centro de mandos. Usar cuando diga /cierre, "cierra el día", "buenas noches" o "resumen de hoy".
---

# /cierre — cierre del día (unos 3 minutos)

1. Lee el diario de hoy (`diario/AAAA-MM-DD.md`). Si no existe, créalo desde la plantilla con lo que te cuente Bruno.
2. Si Bruno no lo ha dicho ya, pregunta en UN solo mensaje:
   - ¿Qué hiciste de las 3 tareas?
   - ¿Algún número nuevo? (peso, ahorro, nota, práctica entregada…)
   - Nota del día, del 1 al 10.
3. En el diario:
   - Marca cada tarea como `[x]` hecha o `[ ]` no hecha.
   - Las no hechas pasan a "Arrastradas" con el contador `(aplazada ×N)` subido en 1.
   - Rellena "Cierre": hecho x/3, nota del día, lo que funcionó y qué cambiar mañana (una línea cada cosa).
4. Si hay números nuevos, actualiza la columna `Actual` en `METAS.md` y ejecuta `python3 scripts/progreso.py`.
5. Si es domingo, haz además la mini-revisión semanal:
   - Puntúa cada meta de 0 a 1,0 según lo que avanzó esa semana (verde a partir de 0,7).
   - Compara con la semana anterior y propón UN solo ajuste para la siguiente.
   - Escríbelo en el diario bajo `## Semana`.
6. Responde solo con esto:

~~~
CIERRE · dom 8 nov
✅ 2/3 · nota 7
📈 M2 Gym: faltan 42 % → faltan 40 % 🟡
↪ Arrastrada: tarea (aplazada ×2)
Mañana empieza por: ...
~~~

7. Añade al final de `log.md`: `AAAA-MM-DD HH:MM · claude · /cierre hecho`.
