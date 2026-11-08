---
name: estado
description: Actualiza la ficha de un proyecto en proyectos/ con un bloque de estado pegado desde Claude o ChatGPT. Usar cuando Bruno pegue un bloque que empieza por "proyecto:" o diga /estado.
---

# /estado — actualizar un proyecto

1. Lee el bloque pegado. Busca en `proyectos/` la ficha cuyo título coincida con `proyecto:`. Si no existe, créala desde `proyectos/_plantilla.md` y pregunta el área en una línea.
2. Actualiza solo lo que traiga el bloque: submetas (columna `Hecho`: sí / parcial / no / %), `estado`, `proximo_paso`, `fecha_limite` y `enlace`. No borres submetas que el bloque no mencione.
3. Ejecuta `python3 scripts/progreso.py`.
4. Responde solo con esto:

~~~
ESTADO · <proyecto>
▓▓▓░░░ faltan 46 % → faltan 30 % 🟡 · 5 d
Próximo paso: ...
~~~

5. Añade al final de `log.md`: `AAAA-MM-DD HH:MM · codex · /estado <proyecto>`.
