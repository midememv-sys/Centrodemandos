---
name: hoy
description: Plan del día de Bruno en el centro de mandos. Usar cuando diga /hoy, "buenos días", "qué hago hoy" o "plan de hoy".
---

# /hoy — plan del día (unos 3 minutos)

1. Ejecuta `python3 scripts/progreso.py` (si falla, `python scripts/progreso.py`) y lee `ESTADO.md`.
2. Lee `METAS.md`, el diario más reciente de `diario/` y las últimas 20 líneas de `log.md`.
3. Si Bruno no lo ha dicho ya, pregunta en UNA sola línea: "¿Algo fijo hoy? (clases, entreno, Indiana, entregas)". Espera su respuesta.
4. Crea `diario/AAAA-MM-DD.md` a partir de `diario/_plantilla.md`:
   - **Fijo hoy**: lo que te haya dicho.
   - **⭐ Destacada**: la tarea que más hace avanzar la meta con peor semáforo.
   - **2 tareas más** como máximo (3 en total).
   - **Arrastradas**: las tareas sin hacer de días anteriores, con su contador `(aplazada ×N)`.
   - Aplica las reglas "Si → entonces" de `METAS.md` que toquen hoy.
5. Si alguna tarea está aplazada ×3 o más, pregunta: ¿la partimos, la delegamos o la borramos?
6. Si en `ESTADO.md` hay "Datos que faltan", pide UNO solo, el de la meta más importante.
7. Responde solo con esto:

~~~
HOY · dom 8 nov
⭐ tarea destacada
• tarea 2
• tarea 3

M1 Aprobar todo   ▓▓░░░░░░░░ hecho 20 % 🟢
M2 Gym −15 kg     ▓▓▓▓▓▓░░░░ faltan 40 % 🟡
M3 Ahorro 1.000 € ▓░░░░░░░░░ hecho 10 % 🔴

⚠ aplazada ×3: ...
❓ Dato que falta: ...
~~~

8. Añade al final de `log.md`: `AAAA-MM-DD HH:MM · codex · /hoy creado`.
