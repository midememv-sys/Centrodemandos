# Registro técnico único

Actualizado 19/11/2026. Estados: abierto → corregido en código → validado. Validación de navegador significa Linux emulado, nunca iPad físico. Histórico en Git; actualizar estas entradas, no duplicarlas por versión.

## A1 · P1 · IDs externos en HTML · validado

- Reproducción: restaurar IDs con comillas y `<img onerror>`; abrir cartera/detalle/historial. Antes se truncaba el ID y se creaban atributos/elementos.
- Causa: interpolaciones sin escape contextual en main.ts. Corrección: escape HTML de todos los IDs externos en atributos/textos; CSS.escape solo para selectores. No se restringen IDs a UUID.
- Regresión: web/tests/e2e/integrity.spec.ts A1; identidad exacta, sin atributos/elementos inyectados ni ejecución, abrir medición/entregable/lote.
- Evidencia nueva: Chromium y WebKit, 17/11, prueba aprobada. Límite: no auditoría de seguridad exhaustiva. Cierre funcional satisfecho; mantener regresión.

## A2 · P1 · Reinterpretación de unidades · validado

- Reproducción: medir 500 EUR y cambiar unidad a céntimos desde línea base o Markdown.
- Causa: progress/prefill/textos usaban unidad de la métrica sin comprobar observation.unit. Corrección: commit y reconciliación rechazan cambio con mediciones; observaciones existentes no se reetiquetan. La última incompatible queda no calculable, con unidad original visible; sin precarga ni comparación entre unidades distintas. Backup antiguo admite lectura/restauración en origen vacío.
- Regresión: web/tests/integrity.test.ts (6 casos A2); web/tests/e2e/integrity.spec.ts A2 conserva borrador y verifica backup incompatible.
- Evidencia nueva: 6 casos TS A2, Chromium y WebKit aprobados. Límite: conversión explícita NO implementada; requiere factor, previsualización, historial y deshacer. No normalizar nombres de unidades ni convertir automáticamente.

## A3 · P2 · Caché visual compartida entre proyectos · validado

- Reproducción: dos proyectos con metric.id igual; abrir ambos y seleccionar submeta. Antes aparecía un cambio ajeno.
- Causa: previous/shown/changes e inspector consultaban solo metric.id. Corrección: clave JSON de [project.id, metric.id], incluyendo lecturas del inspector. Solo comparar observaciones de igual unidad.
- Regresión: web/tests/e2e/integrity.spec.ts A3: aislamiento; guardar y deshacer dentro del proyecto conserva cambios legítimos.
- Evidencia nueva: Chromium y WebKit aprobados. Límite: sin Safari físico; cierre funcional satisfecho.

## V1 · Safari/iPad físico · abierto (pendiente de acceso)

- Comprobación de acceso: 19/11/2026. Solo entorno Linux y navegadores headless; no hay iPad físico/Safari conectado ni portal HTTP del entorno. **La prueba física solicitada no se ejecutó**.
- Recorrido que falta: con 24 proyectos sintéticos, abrir desde Excepciones → seleccionar submeta → medir 84→100 de 200 → confirmar 50 %/faltan 100 → deshacer a 42 %/faltan 116 → cerrar al mismo control/grupo. Probar toque/trackpad reales, precisión, fluidez, teclado virtual, orientación y foco.
- Cierre: registrar modelo de iPad, iPadOS/Safari, fecha, viewport, resultado del recorrido y perfil del dispositivo; corregir hallazgos antes de efectos nuevos. Chromium/WebKit y toque emulados no cierran V1. Las comprobaciones anteriores de emulación conservan su alcance.

## R1 · Referencia ausente · abierto

No se localiza `ScreenRecording_11-17-2026 09-20-53_1.mp4` (≈8,47s) ni imágenes originales Jenda/Apple en los materiales disponibles. Se trabaja con descripción del gestor, sin afirmar inspección ni tiempo real. No confundir recorrido propio ni vídeo del 11/11. Cierre: inspeccionar archivo original accesible y contrastar geometría/material/coreografía.

## S1 · P2 · Interacción inicial de la escena · validado

- Reproducción nueva: pulsar etiqueta 3D desplazaba el hit target; Escape durante carga podía perder retorno inmediato de foco.
- Causa: transform global de pulsación sustituía el centrado; inicialización diferida no comprobaba cierre en curso, entorno reflectante renderizado costoso en software.
- Corrección: centrado con propiedad translate independiente, etiquetas en estaciones estables; cancelar montaje al iniciar cierre; mapa local de estudio pequeño en vez de seis renders de entorno.
- Regresión: web/tests/e2e/scene.spec.ts (clic real, interrupciones, ausencia de RAF en reposo, degradación). 96 casos funcionales aprobados en ambos motores; 18 afectados repetidos tras los ajustes finales, también aprobados.
- Cierre funcional satisfecho: ejecución ampliada aprobada, revisión visual y límite físico V1 registrado. No se confunde duración programada con fluidez medida.

## S2 · P2 · Selección fuera de la primera página 3D · validado

- Reproducción: proyecto sintético con 8 submetas; seleccionar la octava y medir. El inspector conserva la octava, pero la escena volvía a piezas 1–6.
- Causa: el constructor iniciaba page=0 sin usar selected. Corrección: página inicial calculada por la identidad de la submeta seleccionada.
- Regresión: web/tests/e2e/scene.spec.ts «pérdida de contexto, paginación explícita y selección fuera de página», ampliada para guardar la octava. Falló antes de la corrección; aprobada después en Chromium y WebKit.
- Cierre funcional satisfecho mediante ejecución selectiva final de 18 casos; no se atribuye esa corrección a la ejecución anterior completa de 96. Límite físico V1 pendiente.

## V2 · Rendimiento y calidad objetivo · abierto (verificación/mejora)

- Evidencia histórica del 17/11/2026: cinco ciclos en Chromium 159 headless, Linux AMD EPYC, ANGLE/SwiftShader; RAF p95 ≈300 ms y máximo ≈917 ms durante apertura/selección/cierre, incluyendo compilación. El contador de renders queda estable en reposo en 5/5 ciclos. No son fps presentados ni medición del iPad.
- Reproducción local: web/scripts/measure_spatial.mjs; detalle actual en web/docs/revision/rendimiento.json. El muestreo espera un frame de la nueva selección antes de declarar reposo, para no leer el indicador del frame previo.
- Causa/alcance: renderizado software y arranque WebGL; no hay evidencia suficiente para atribuir esos costes al dispositivo objetivo. Ya se evita entorno de seis renders, se limita DPR y se libera escena; no se afirma resuelto el presupuesto de movimiento.
- Criterio de cierre: perfil en Safari/iPad físico con el recorrido y mismos datos, revisar tiempos de respuesta/frames y adaptar calidad/presupuesto antes de afirmar fluidez o máxima calidad de referencia. No es un fallo P1 de integridad.

## S3 · P2 · Etiquetas proyectadas solapadas en móvil · validado

- Reproducción visual: mesa sintética de 3 submetas, 390×844; la tercera etiqueta intersectaba las dos primeras. El escenario de cartera con una submeta no lo detectaba.
- Causa: proyección de etiquetas al plano 2D sin espacio suficiente en la segunda fila. Corrección: en móvil, rejilla DOM frontal y estable; las mallas continúan siendo 3D y los números vinculan cada pieza con su submeta.
- Regresión: scene.spec.ts «transición reversible» comprueba los rectángulos de las tres etiquetas después de resize/teclado/reducir movimiento. Cuatro casos afectados repetidos, Chromium/WebKit, aprobados. Captura móvil renovada.
- Cierre funcional satisfecho en emulación; Safari/iPad físico sigue en V1. No se alteró dominio/progreso.

## E1 · P2 · Densidad al añadir Excepciones · validado

- Regresión introducida durante este incremento: barra adicional sobre el resumen reducía a una las filas completas de cartera visibles en 1366×1024. Reproducción: cargar cartera sintética 24 y contar filas completas.
- Causa: nuevo bloque vertical permanente antes de En foco. Corrección: acceso en encabezados existentes; barra de retorno solo dentro de Excepciones. Sin reducir letra ni controles de 44px.
- Regresión: revision3.spec.ts «primera pantalla...» exige ≥2 filas completas en horizontal y siguiente acción/medición destacada en iPhone. Prueba falló antes; comprobación específica posterior aprobada en ambos motores. Regresión específica en ambos motores aprobada; vuelta a la cartera y vista de 24 proyectos aprobadas en las 24 afectadas finales.
- Cierre funcional satisfecho en emulación con 24 proyectos/títulos largos. Límite físico V1.

## E2 · P2 · Acceso oculto a 1024px · validado

- Regresión introducida al mover el acceso: Excepciones quedaba invisible a 1024px, detectado en WebKit; la misma regla aplica a cualquier navegador estrecho.
- Causa: contenedor span heredaba la regla que oculta texto secundario del encabezado. Corrección: contenedor propio de controles, sin depender de esa regla de metadatos.
- Regresión: exceptions.spec.ts inicia la vista en ambos viewports/motores y comprueba retorno a 24 con búsqueda activa; primera ejecución estrecha falló, smoke posterior aprobado. Regresión específica en ambos motores aprobada; vuelta a la cartera y vista de 24 proyectos aprobadas en las 24 afectadas finales.
- Cierre funcional satisfecho: acceso operable por teclado/toque emulado y visible en ambas orientaciones. V1 pendiente para dispositivo real.

## S4 · P2 · Teclado durante despliegue rápido · validado

- Reproducción observada 19/11: reunir/desplegar rápidamente, enfocar segunda etiqueta y Enter. Se mantenía la primera submeta porque la etiqueta todavía tenía visibility:hidden.
- Causa: clase de disponibilidad de controles actualizada al dibujar un frame en lugar de al cambiar el estado. Disponibilidad DOM y frame podían discrepar. El indicador diagnóstico de animación también podía conservar el valor del frame anterior.
- Corrección integrada: clase de visibilidad y estado diagnóstico de animación se actualizan sincrónicamente con la intención, reservando RAF para representación. Sin cambiar medidas, progreso ni añadir efectos.
- Regresión: scene.spec.ts «mismo turno, sin esperar un frame» ejecuta despliegue/foco dentro de un único turno JS; falló antes de corregir. La batería selectiva de 60 también reprodujo el fallo en ambos motores (58 aprobadas, 2 fallidas). Cierre funcional satisfecho: 24 casos afectados finales aprobados en Chromium/WebKit, incluido el caso determinista. No se repitieron las 60 completas tras esta corrección. V1/V2 físicos siguen pendientes.
