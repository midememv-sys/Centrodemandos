# Centro de mandos · continuidad común

Actualizado: **24/11/2026**. Entrada única de Codex, Claude y el gestor. Actualizar en su sitio; histórico en Git, sin handoffs por versión ni adjuntos para traslado manual.

## Objetivo permanente

Coordinar **todos** los proyectos desde una cartera global: estado, progreso medido, información pendiente, bloqueo, siguiente acción, responsable, fecha y entregables. Tres prioridades complementan la cartera completa. Jenda conserva agenda/horarios. Calidad de movimiento sigue siendo objetivo, sin acreditación física en iPad.

## Fuente y commits

- Repositorio común: **midememv-sys/Centrodemandos · main**. Head comprobado al empezar y antes de actualizar: `6c8658604e70a282837a40ff3d4b22a45fa66a8f`. Consultar el head de este archivo desde GitHub en cada sesión.
- Fuente activa **local, no publicada**: `/workspace/centro-github-preparado/web`, rama `desarrollo/centro-web-local`, commit **`411f48b79406ca48b44c74f47e2376bc33e40f06`**. Deriva de **`f45ba84a8b69a212ede010c462d200ef5e3bc650`**, conservando el trabajo posterior `ac0959c`. Al iniciar se comprobó que `web/app` coincidía con f45ba84.
- Nueva preparación: build de revisión sintética aislada y recorrido para iPad. **Dominio, Markdown y motor/animaciones 3D permanecen iguales a f45ba84**; no se añaden efectos. Las correcciones A1/A2/A3 y S4 siguen integradas.
- Solo continuidad, registro e instrucciones técnicas se comparten en GitHub. Código/medios siguen sin permiso de publicación pública. La vista **privada** sí está autorizada; no autoriza publicar rama, medios, ZIP, dist, node_modules, secretos o documentos operativos. No reintentar la subida pública rechazada.

## Estado real y acceso privado

- `npm run build:review` crea `app/dist-review`; `npm run preview:review` sirve **solo el build** en `0.0.0.0:4179`, con puerto estricto. Servicio iniciado y respuesta HTTP 200 comprobada en el entorno. Peticiones de rutas de fuente/Git devuelven el shell HTML, no archivos del repositorio; host no autorizado devuelve 403.
- Carga automáticamente **24 proyectos sintéticos** en IndexedDB **`centro-review-f45-v1`**, separada de **`centro-demo-v1`** de la app normal. Primera carga concurrente protegida por revisión atómica; no reemplaza cambios ya guardados. Sin sincronización entre dispositivos.
- Medir, guardar, deshacer, editar y exportar funcionan en la revisión. Crear/importar/restaurar se omiten en este modo para mantener el escenario sintético; la aplicación normal conserva esos flujos y su almacenamiento. El modo de build **no es autenticación**.
- **Acceso desde iPad todavía pendiente**: el estado del entorno solo anuncia SSH/22, sin portal HTTP/URL HTTPS. Se solicitó configurar **Edit Environment → HTTP Previews → puerto 4179 → Apply to this chat**. La herramienta no puede añadir puertos. Después hay que consultar/verificar la URL exacta autenticada del propietario; no inventarla ni presentar localhost/SSH como enlace del iPad.
- Si el portal exige su hostname, reiniciar con `CENTRO_PREVIEW_HOST` igual al hostname exacto devuelto por el entorno. No permitir todos los hosts. No guardar URLs privadas o identificadores del entorno en este repo público. No se abrió túnel ni se desplegó/publicó la aplicación.

## Cartera y excepciones

Resumen, tres prioridades y cartera completa; acceso a **Excepciones** en encabezados existentes. Bloqueos explícitos, vencidos/hoy/próximos 7 días de Madrid y decisiones por acción ausente o entregable no aceptado. Completados/archivados excluidos. Motivos, fecha, responsable, siguiente paso y medición visibles; rango/cobertura y desconocidos conservados. «Toda la cartera (24)»/Proyectos devuelve todos con un toque, limpiando filtros explícitamente.

Demo: **4 bloqueos, 6 vencimientos, 5 decisiones; 8 proyectos únicos**. Fechas planificadas relativas al primer día de carga, sin refrescar las observaciones originales. Incluye desconocidos, descenso, pausados, entregables rechazados y títulos largos. 3D inicializado solo al abrir un proyecto; una escena activa, alternativa DOM y liberación al cerrar. PWA precarga el asset para funcionar offline, sin inicializar una escena por fila.

## Verificación nueva · 24/11

- **42 TypeScript + 4 Python**, aprobadas. Builds normal/revisión aprobados. Instalación limpia con lockfile y builds: **16 archivos idénticos por SHA-256 en cada salida**. Three.js diferido ≈534 kB minificado/≈142 kB gzip; advertencia conservada, sin dependencia nueva.
- Build de revisión: **9 E2E aprobadas**, 5 Chromium y 4 WebKit; **1 PWA WebKit omitida**. Primera carga concurrente, aislamiento respecto a base normal, Excepciones → cartera → seleccionar → medir → guardar → recargar → deshacer → foco, toque/teclado/reducir movimiento, fallo de disco y conflicto con borrador conservado. PWA revisión offline comprobada en Chromium.
- Regresión **selectiva de 50 E2E** de excepciones, escena, integridad e incremento 3: primera ejecución **39 aprobadas, 11 fallidas** (4 errores de trazas compartidas y 7 timeouts de 30s bajo concurrencia). Corregido el instrumental T1: **las 11 afectadas repetidas en serie con timeout 90s, todas aprobadas**. No se repitieron sus 39 aprobadas ni se afirma una ejecución completa de toda la suite en verde.
- **2 PWA normales Chromium aprobadas** sobre build de producción, con puerto/carpeta propios. Sin reimportación rota, reinterpretación de unidades ni cambios ficticios entre proyectos en los casos regresados.
- Entorno probado: **Linux headless, Chromium 159 y WebKit 27.2**; anchuras 1366×1024, 1024×1366 y 390px, altura reducida 480px, oscuro/reducido, teclado/ratón/toque emulados. WebKit automatizado **no es Safari del iPad**. Resultados del 19/11 y sus capturas/vídeo son históricos; no presentarlos como prueba física o nueva grabación.

**Safari/iPad físico: pendiente, NO ejecutado por falta de acceso.** Precisión táctil, trackpad, teclado virtual, fluidez/fps y foco reales no están validados. No se repitió el perfil RAF; p95 ≈300 ms de VM SwiftShader del 17/11 es histórico, no medida del iPad. V1/V2 siguen abiertos; sin blur completo ni promesas de 60/120 fps. Registro técnico único: [FALLOS.md](FALLOS.md); T1 validado como defecto del instrumental, no de dominio.

## Recorrido y siguiente paso

Habilitar/verificar el portal privado y abrir su URL exacta desde Safari del iPad con la cuenta propietaria. Después:

1. Resumen → **Excepciones** → **Toda la cartera (24)**.
2. Abrir **Encuentro de diseño · edición abierta** desde la fila y seleccionar **Inscripciones confirmadas** en la pieza/etiqueta accesible: **42 % / faltan 116**.
3. Medir **100**, fuente **Prueba sintética iPad**, **Ahora** → confirmar. Tras guardado real: **50 % / faltan 100**.
4. **Deshacer cambio** → **42 % / faltan 116** → cerrar. Foco y scroll en la misma fila. Recargar y comprobar persistencia. Repetir teclado, reducir movimiento y apertura/cierre rápidos.

Registrar modelo, iPadOS/Safari, fecha/orientación, toque/trackpad, teclado virtual, foco y perfil del dispositivo. Corregir y repetir hallazgos reproducibles **antes de ampliar efectos**. Sin acceso físico, V1 sigue pendiente; no simular una ficha de dispositivo.

## Arranque, backup y reversión

Desde `web/`: Node 22.12+, `npm ci`; app normal `npm run dev -- --port 5177`, `npm run build`; revisión `npm run build:review`, `npm run preview:review`. Ningún secreto obligatorio. PWA normal de pruebas usa 4180 para no reutilizar la revisión de 4179. Guía detallada vigente: web/README.md, DECISIONES.md, DESIGN.md y docs/VERIFICACION.md.

Exportar JSON desde Ajustes antes de cambiar origen, navegador o versión. Restaurar backup compatible en otro origen vacío con la app normal y verificar observaciones/unidades/historial. Rollback en checkout separado conservando backup y origen; no reset sobre trabajo posterior ni borrar IndexedDB. `f45ba84`/`ac0959c` conservan la base. Sin nuevos ZIPs, memorias o medios para traslado manual.

## Protocolo compartido

Leer esta nota y FALLOS desde main y confirmar commit. Un responsable de escritura; paralelo solo con checkout propio. Claude opcional. No cargar notas personales para frontend. IDs externos escapados; unidades no reinterpretadas; cachés proyecto/submeta y origen proyecto/grupo. Animación no gobierna guardado ni disponibilidad. Cada configuración de pruebas usa resultados y puerto propios.

R1 conserva pendiente `ScreenRecording_11-17-2026 09-20-53_1.mp4` (~8,47s) e imágenes originales; no se afirma inspección. Nuestro vídeo no es esa referencia. Sin backend, sincronización, Hermes, runners, agenda nueva, pagos o IA para consultar/editar/calcular.

ChatGPT gestor: Ajustes → Apps/Plugins → GitHub → autorizar midememv-sys/Centrodemandos y leer esta nota desde main. En GPT personalizado, habilitar Apps si lo permite; si no, usar chat compatible. Conocimiento subido es copia estática. La continuidad Markdown pública no vuelve accesible el código local ni autoriza publicarlo.
