# Centro de mandos · continuidad común

Actualizado: **25/11/2026**. Entrada única de Codex, Claude y el gestor. Actualizar en su sitio; histórico en Git, sin handoffs por versión ni adjuntos para traslado manual.

## Objetivo permanente

Coordinar **todos** los proyectos desde una cartera global: estado, progreso medido, información pendiente, bloqueo, siguiente acción, responsable, fecha y entregables. Tres prioridades complementan la cartera completa. Jenda conserva agenda/horarios. Calidad de movimiento sigue siendo objetivo, sin acreditación física en iPad.

## Fuente y commits

- Repositorio común: **midememv-sys/Centrodemandos · main**. Head verificado al iniciar y antes de actualizar: `0b16a5a5cf2738bf590088a03c27a70c2fc36f87`. Consultar siempre el head y este archivo desde GitHub.
- Fuente **local, no publicada**: `/workspace/centro-github-preparado/web`, rama `desarrollo/centro-web-local`, commit **`f0b810a18801e7b99962fe9182047beb50f6af06`**. Demo derivada de **411f48b**, conservando f45ba84 y todos los commits posteriores. Identificación base/exacta y hashes en el manifiesto portátil; no afirmar que el binario corregido es idéntico al original 411f48b.
- Cambios: preparar build portátil sintético para la Wi-Fi, UUID compatible con HTTP y corregir close encolado que cancelaba una escena reabierta. **Sin cambiar cálculos, esquema, unidades, cobertura, importación ni añadir efectos/duraciones.**
- Solo continuidad, registro e instrucciones técnicas se comparten en GitHub. Código/medios/build siguen sin permiso de publicación pública. No reintentar subidas rechazadas. La alternativa LAN está autorizada; no implica desplegar ni publicar una rama, ZIP, dist, node_modules o datos personales.

## Acceso: alternativa Wi-Fi preparada

- Carpeta **`/workspace/centro-github-preparado/web/preview-lan`**, ≈1 MB: `demo/` (16 assets compilados), `servir.py`, `LEEME.md`, `demo-manifest.json`. Generada con `npm run prepare:lan`; no ZIP, fuentes, paquetes, secretos o datos reales. Una sola carpeta con nombre fijo; no nuevas memorias.
- **Falta copiarla completa por un canal privado al ordenador de la misma Wi-Fi que el iPad.** La transferencia y la red entre ambos dispositivos no se han validado desde Cloud. Clonar main no obtiene ese build: el código es local. SSH/22 anunciado no acredita por sí solo una sesión de copia utilizable. No se inventaron claves, fingerprints o enlaces.
- En el ordenador, con **Python 3.9+**, abrir terminal dentro de la carpeta y ejecutar `python3 servir.py --bind IP_WIFI` (Windows: `py -3 servir.py --bind IP_WIFI`). Sustituir IP_WIFI por la IPv4 privada de su conexión Wi-Fi; verla en ajustes de Wi-Fi/TCP-IP. **No usar IP de Cloud ni 127.0.0.1.**
- Safari del iPad, misma Wi-Fi: **`http://IP_WIFI:4179`**. Es una plantilla, no una URL comprobada. Ordenador/terminal deben seguir abiertos. Ctrl+C detiene el servicio. Puerto ocupado produce error, sin cambiar silenciosamente a otro.
- Servidor estático sin API de datos: valida hashes, solo sirve assets declarados y rechaza fuente/rutas ajenas/archivo alterado. Cualquier medición sigue guardándose en IndexedDB de Safari, sin envío al ordenador ni sincronización. Preparación requiere Node; **ejecución de la copia no necesita Git, Node ni paquetes Python**.
- **HTTP local sin autenticación ni cifrado:** solo demo sintética en Wi-Fi de confianza, sin puertos del router abiertos. PWA/offline y portapapeles automático no garantizados en HTTP; mantener servidor conectado. Exportar antes de cambiar IP/puerto, que cambia el origen de almacenamiento. No introducir datos personales.
- Cloud sigue mostrando únicamente SSH/22: sin URL HTTP privada para iPad. El HTTP 200 interno comunicado anteriormente solo comprobaba el servidor del entorno. El portal autenticado 4179 continúa como opción pendiente de configuración del propietario, no requisito para preparar la copia LAN.

## Cartera y excepciones

Resumen, tres prioridades y cartera completa; acceso a **Excepciones** en encabezados existentes. Bloqueos explícitos, vencidos/hoy/próximos 7 días de Madrid y decisiones por acción ausente o entregable no aceptado. Completados/archivados excluidos. Motivos, fecha, responsable, siguiente paso y medición visibles; rango/cobertura y desconocidos conservados. «Toda la cartera (24)»/Proyectos devuelve todos con un toque, limpiando filtros explícitamente.

Demo: **4 bloqueos, 6 vencimientos, 5 decisiones; 8 proyectos únicos**. Fechas planificadas relativas al primer día de carga, sin refrescar las observaciones originales. Incluye desconocidos, descenso, pausados, entregables rechazados y títulos largos. 3D inicializado solo al abrir un proyecto; una escena activa, alternativa DOM y liberación al cerrar. PWA precarga el asset para funcionar offline, sin inicializar una escena por fila.

## Verificación nueva · 25/11

- **43 TypeScript + 8 Python aprobadas**: caso nuevo UUID sin randomUUID; cuatro casos nuevos del servidor (assets/MIME, rutas y fuente inaccesibles, hashes/incompleto, puerto ocupado). Builds normal/revisión aprobados. Sin dependencias nuevas; Three.js diferido conserva la advertencia ≈534 kB minificado/≈142 kB gzip.
- Reproducción L1: origen HTTP no seguro, randomUUID ausente, 0 proyectos y error de carga. Corregido con getRandomValues, sin aleatoriedad débil ni reinterpretar valores.
- Primera batería HTTP: **5 aprobadas y 1 fallida** (Chromium bloqueado en «Preparando vista 3D» tras apertura/cierre rápido). Corregido L2: close nativo anterior no cancela el montaje reabierto ni borra su origen. **Batería final HTTP completa: 8 aprobadas**, 4 por motor, incluido caso explícito de reapertura en el mismo turno JS.
- **12 regresiones selectivas de escena aprobadas** en Chromium/WebKit, **2 PWA normales Chromium aprobadas**. No se ejecutó de nuevo toda la suite ni la batería selectiva de 50 del 24/11. Resultados/capturas del 19/11 y verificaciones del 24/11 son históricos, conservados en Git.
- Copia portátil fuera del repositorio: `servir.py` arrancó sin Git/Node/dependencias, **16/16 assets iguales SHA-256**, fuentes 404. Metadatos: base 411f48b, fuente exacta f0b810a, `sourceDirty: false`.
- Entorno: Linux headless, Chromium/WebKit; 1366×1024, 1024×1366 y móvil/altura reducida 390×480, oscuro/reducido, teclado/ratón/toque **emulados**. El gateway no enruta a su propia IP privada: los tests usan un origen HTTP no seguro con relay local de peticiones. Se verificó contexto realmente no seguro y ausencia de randomUUID. **No demuestra una conexión Wi-Fi ni un iPad físico.**

**Safari/iPad físico: pendiente, NO ejecutado.** También pendiente copiar la carpeta al ordenador y comprobar acceso entre dispositivos. Fluidez, precisión táctil/trackpad, teclado virtual, foco físico y fps siguen sin validar. No perfil RAF nuevo: el p95 de VM SwiftShader del 17/11 es histórico, no medición del iPad. V1/V2 abiertos; L1/L2 validados funcionalmente. Registro técnico único: [FALLOS.md](FALLOS.md).

## Recorrido y siguiente paso

Copiar la carpeta preparada al ordenador por un canal privado, arrancar el servidor en su IP Wi-Fi y abrir su dirección local en Safari del iPad. No afirmar que ese traslado ya ocurrió. Después:

1. Resumen → **Excepciones** → **Toda la cartera (24)**.
2. Abrir **Encuentro de diseño · edición abierta** desde la fila y seleccionar **Inscripciones confirmadas** en la pieza/etiqueta accesible: **42 % / faltan 116**.
3. Medir **100**, fuente **Prueba sintética iPad**, **Ahora** → confirmar. Tras guardado real: **50 % / faltan 100**.
4. **Deshacer cambio** → **42 % / faltan 116** → cerrar. Foco y scroll en la misma fila. Recargar y comprobar persistencia. Repetir teclado, reducir movimiento y apertura/cierre rápidos.

Registrar modelo, iPadOS/Safari, fecha/orientación, toque/trackpad, teclado virtual, foco y perfil del dispositivo. Corregir y repetir hallazgos reproducibles **antes de ampliar efectos**. Sin acceso físico, V1 sigue pendiente; no simular una ficha de dispositivo.

## Arranque, backup y reversión

Desde `web/`: Node 22.12+, `npm ci`; app normal `npm run dev -- --port 5177`, `npm run build`; revisión `npm run build:review`, `npm run preview:review`; copia portátil `npm run prepare:lan`. En el ordenador LAN: Python 3.9+ únicamente. Ningún secreto obligatorio. PWA normal de pruebas usa 4180 para no reutilizar la revisión de 4179. Guía detallada vigente: web/README.md, DECISIONES.md, DESIGN.md y docs/VERIFICACION.md.

Exportar JSON desde Ajustes antes de cambiar origen, navegador o versión. Restaurar backup compatible en otro origen vacío con la app normal y verificar observaciones/unidades/historial. Rollback en checkout separado conservando backup y origen; no reset sobre trabajo posterior ni borrar IndexedDB. `f45ba84`/`ac0959c` conservan la base. Sin nuevos ZIPs, memorias o medios para traslado manual.

## Protocolo compartido

Leer esta nota y FALLOS desde main y confirmar commit. Un responsable de escritura; paralelo solo con checkout propio. Claude opcional. No cargar notas personales para frontend. IDs externos escapados; unidades no reinterpretadas; cachés proyecto/submeta y origen proyecto/grupo. Animación no gobierna guardado ni disponibilidad. Cada configuración de pruebas usa resultados y puerto propios.

En HTTP LAN no se habilita la importación normal que requiere contexto seguro; los flujos completos de importación permanecen en la aplicación normal. La demo conserva su base aislada y sus 24 proyectos.

R1 conserva pendiente `ScreenRecording_11-17-2026 09-20-53_1.mp4` (~8,47s) e imágenes originales; no se afirma inspección. Nuestro vídeo no es esa referencia. Sin backend, sincronización, Hermes, runners, agenda nueva, pagos o IA para consultar/editar/calcular.

ChatGPT gestor: Ajustes → Apps/Plugins → GitHub → autorizar midememv-sys/Centrodemandos y leer esta nota desde main. En GPT personalizado, habilitar Apps si lo permite; si no, usar chat compatible. Conocimiento subido es copia estática. La continuidad Markdown pública no vuelve accesible el código local ni autoriza publicarlo.
