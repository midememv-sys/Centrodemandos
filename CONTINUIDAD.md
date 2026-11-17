# Centro de mandos · continuidad común

Actualizado: **17/11/2026**. Entrada única para Codex, Claude y el chat gestor. Actualizar en su sitio; histórico en Git, sin nuevos handoffs, memorias por versión o adjuntos que Bruno tenga que transferir.

## Objetivo permanente

Coordinar **todos** los proyectos desde una cartera global: estado, progreso medido, información pendiente, bloqueo, siguiente acción, responsable, fecha y entregables. Tres prioridades complementan la cartera completa. Jenda conserva agenda/horarios. Máxima calidad espacial y de movimiento es el objetivo; no está acreditada frente a la referencia ausente ni en iPad físico.

## Fuente activa y commits

- GitHub compartido: **midememv-sys/Centrodemandos · main**. Al empezar se verificó `8e99c2616b80c0a64023411ceaa2a0a3644f7da2`; este incremento actualiza únicamente Markdown de continuidad, incidencias e instrucciones comunes. Confirmar siempre el head de main y el commit del archivo al leerlo.
- Aplicación activa **local**: `/workspace/centro-github-preparado/web`. Git local en su padre, rama `desarrollo/centro-web-local`. Código de app en **`9b8b9f0c9493f7781ae9730d4598e01abe79f732`**, sobre `561407b` (escena) y `8386748` (integridad). Commit inicial recuperable `195825b`; carpetas visual5/6/7 y trabajo previo conservados.
- **El código y los medios NO están publicados en GitHub.** `desarrollo/centro-web` remota no existe. Otro chat no puede afirmar que ha leído web/ desde main. La autorización de publicación sigue pendiente; no reintentar la subida rechazada ni reutilizar blobs huérfanos. No se ha desplegado ni abierto un túnel.
- Registro técnico único: **[FALLOS.md](FALLOS.md)**. A1/A2/A3 y S1/S2/S3 validados en el alcance indicado. V1, V2 y R1 abiertos: dispositivo físico, rendimiento/calidad objetivo y referencia ausente. Ningún P1 de integridad conocido queda abierto en esta revisión.

GitHub comparte documentación autorizada, no conversaciones ni IndexedDB. La fuente operativa del prototipo es local al navegador/origen, sin sincronización. Markdown personal y ESTADO.md no se modificaron ni se reafirmó su frescura. Demo/evidencia exclusivamente sintéticas; repositorio público, sin nuevos datos personales, secretos o información ECC.

## Qué funciona y qué cambió

Se reprodujeron los tres fallos sobre visual7; no se localizó visual7-corregido. IDs externos escapados en HTML conservando identidad no UUID; commit/Markdown bloquean cambios de unidad con observaciones; backups antiguos conservan unidad original y la última incompatible queda no calculable, sin precarga ni comparación falsa. Cachés/inspector/3D usan identidad proyecto/submeta.

Primera escena **Three.js real**, diferida y única para el proyecto seleccionado: base y objetos paramétricos por categoría, materiales/reflejo local/sombras, piezas de submetas reales, selección, reunión/despliegue reversible y medición convencional. Guardar/deshacer actualiza representación; cerrar libera recursos y recupera foco/contexto. DOM equivalente y alternativa sin WebGL; reduced motion y render bajo demanda. Etiquetas móviles en rejilla frontal para evitar solapamientos.

Cartera completa de 24 proyectos/títulos largos, edición, medición directa, resultado/trabajo/evidencia separados, historial, importación reconciliada atómica e idempotente, backup/restauración, conflictos y borradores preservados. Sin backend, Hermes, runner, agenda nueva, servicios de pago ni IA para consultar/editar/calcular. Conversión explícita de unidades pendiente; no improvisarla.

## Verificación ejecutada ahora

- **35 TypeScript y 4 Python**, aprobadas.
- **96 E2E funcionales** (48 Chromium, 48 WebKit), excluyendo vídeo. Tras ajustes de selección >6/objetivo desconocido, **18 afectadas repetidas**; tras CSS móvil, **4 afectadas repetidas**, todas aprobadas. El estado final tiene regresiones selectivas posteriores; no se declara otra ejecución completa de 96 ni se suman repeticiones.
- **2 PWA Chromium** sobre build final, aprobadas: precarga/primera exploración offline, edición y recarga. WebKit 27.2 también mostró escena WebGL; no es Safari/iPad físico.
- Build y reconstrucción limpia con lockfile (`npm ci`): **16 archivos de salida idénticos SHA-256**. Advertencia de tamaño del chunk 3D: ≈534 kB minificado / ≈142 kB gzip diferidos.
- Vídeo sintético nuevo **57s, velocidad normal**, una prueba de grabación aprobada. Capturas antes/después con mismos proyectos y viewport, vertical, oscuro/reduced y cartera 24. Todo preparado localmente bajo `web/docs/revision/`, con nombres fijos; no adjuntado para traslado ni publicado.
- Medición en VM Linux AMD EPYC, Chromium 159/ANGLE SwiftShader: RAF p95 ≈300 ms, máximo ≈917 ms en el recorrido, con arranque/compilación; renders estables en reposo 5/5. **No acredita fluidez ni 60/120 fps en iPad**. No se reintrodujo blur completo. Detalle, método y límites en la verificación local y V2.

Evidencia heredada de visual7/copia externa no se presenta como nueva. Fuentes locales vigentes: web/README.md, BRIEF.md, DESIGN.md, DECISIONES.md, docs/VERIFICACION.md. Registro técnico compartido aquí enlazado; no crear otro.

## Abrir, recuperar y siguiente paso

Desde la fuente local: `npm ci`, `npm run dev -- --host 127.0.0.1 --port 5177`; build con `npm run build`. Sin secretos ni variables obligatorias. Localhost pertenece al servidor, **no es un enlace accesible desde el iPad**. El entorno solo anuncia SSH y no ofrece URL HTTP de vista previa.

Ajustes → exportar backup JSON antes de actualizar. Restaurar en origen vacío compatible, verificar observaciones/unidades/historial. Rollback del código en checkout separado, conservando el origen y el backup; no hacer reset sobre trabajo posterior ni borrar IndexedDB. `8386748` conserva los arreglos de integridad sin 3D; visual7 original también se conserva, pero contiene los fallos corregidos.

**Siguiente paso:** perfilar y ajustar esta misma escena en Safari/iPad físico con el recorrido representativo, y contrastarla con el archivo original accesible en los materiales autorizados. Falta exactamente **ScreenRecording_11-17-2026 09-20-53_1.mp4** (≈8,47s), además de imágenes originales Jenda/Apple; no se ha visto. Se usó la descripción del gestor (mecanismos/reloj, capas, reflejos y perspectiva), sin afirmar tiempo real. No confundirlo con el vídeo del 11/11 ni con nuestro recorrido. No pedir a Bruno otro traslado manual.

## Protocolo común

- Leer esta nota desde main y confirmar commit en cada sesión. Memoria del chat/Conocimiento no sustituye el estado actual. Si no hay acceso a la fuente local, declararlo; el código no está publicado aún.
- Un responsable de escritura por tarea. Codex implementa; Claude opcional. Paralelo solo con ramas/checkouts separados y revisión acotada. No cargar diarios, log completo o documentos personales para frontend.
- Leer FALLOS antes de ampliar efectos. Reproducir/corregir/validar integridad primero. Valores externos: escape contextual o DOM/dataset; CSS.escape solo selectores. Unidades observadas no reinterpretadas. Cachés de submeta por proyecto/submeta.
- No inventar progreso, cobertura, resultados, conexiones, pruebas o independencia de revisión. Parcial desconocido; estimación heredada separada. Animación nunca anuncia guardado antes del commit.
- Actualizar archivos vigentes, evidencia mínima en rutas fijas e histórico en Git. No nuevos handoffs/memorias, ZIP, dist, node_modules, secretos o capturas descartadas. Retirar solo generados propios; conservar trabajo ajeno y datos operativos.
- Código/medios, despliegues y gasto requieren la autorización que corresponda. La centralización Markdown no autoriza su publicación.

## Acceso del chat gestor

ChatGPT → Ajustes → Apps/Plugins → GitHub → conectar y autorizar midememv-sys/Centrodemandos. Seleccionar GitHub en el chat cuando esté disponible. En GPT personalizado, habilitar Apps si su configuración lo ofrece; en otro caso usar un chat normal compatible. Conocimiento subido es estático; no transfiere conversaciones, memoria, cuota o acceso al código no publicado. No pegar tokens ni cambiar visibilidad.

Fuentes: [GitHub en ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt-deep-resear), [capacidades de GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts).
