# Centro de mandos · continuidad común

Actualizado: **19/11/2026**. Entrada única de Codex, Claude y el gestor. Actualizar en su sitio; histórico en Git, sin handoffs por versión ni adjuntos para traslado manual.

## Objetivo permanente

Coordinar **todos** los proyectos desde una cartera global: estado, progreso medido, información pendiente, bloqueo, siguiente acción, responsable, fecha y entregables. Tres prioridades complementan la cartera completa. Jenda conserva agenda/horarios. Máxima calidad de movimiento sigue siendo objetivo, sin acreditación física en iPad.

## Fuente y commits

- Repositorio **midememv-sys/Centrodemandos · main**. Al iniciar este incremento se verificó `61904210e10b45b76b3585d682ad04e04baf14bd`. Confirmar siempre el head y commit de este archivo desde GitHub.
- Fuente activa **local**: `/workspace/centro-github-preparado/web`; Git en su padre, rama `desarrollo/centro-web-local`. **App en `f45ba84a8b69a212ede010c462d200ef5e3bc650`**. Continúa `bd23cbc` / app `9b8b9f0`; no se reinició el producto ni se descartó trabajo anterior.
- **Código y medios siguen locales, sin publicación ni despliegue.** La autorización continúa pendiente; no reintentar medios rechazados ni interpretar la actualización Markdown como permiso. `desarrollo/centro-web` es una rama remota prevista, no una fuente publicada que se pueda afirmar leída.
- Registro técnico único: **[FALLOS.md](FALLOS.md)**. E1/E2/S4 corregidos y validados en el alcance indicado. V1 (Safari/iPad físico), V2 (rendimiento objetivo) y R1 (referencia original) continúan abiertos. No P1 de integridad conocido abierto.

El repositorio es público. No se añadieron datos personales, secretos o ECC ni se modificaron documentos operativos originales/ESTADO.md. Tampoco se confirmó su frescura. GitHub comparte documentación autorizada; no IndexedDB, conversaciones, memoria o cuota de los chats.

## Incremento vigente: excepciones

Vista derivada del mismo estado, sin nueva fuente canónica:

- Bloqueos registrados, con motivo o indicación de que falta describirlo.
- Fechas vencidas y vencimientos entre hoy y **+7 días de calendario de Europe/Madrid**, incluidos ambos extremos. Sin fecha no equivale a vencido. Pausar no borra un plazo.
- Decisiones derivadas de falta de siguiente acción o última evaluación de entregables pendiente/rechazada/con cambios. Se explican los criterios; no se inventan decisiones de negocio.

Completados y archivados quedan fuera de las excepciones, presentes en la cartera. Motivo, responsable, fecha, siguiente acción y resultado siguen accesibles. Un proyecto puede figurar en varios grupos; el total cuenta proyectos distintos. Buscar filtra la vista; **«Toda la cartera» o Proyectos desde Excepciones recuperan todos en un toque**, incluso con búsqueda activa y scroll.

Demo opcional en espacio vacío: Excepciones → «Cargar demo de excepciones (24)»; también Ajustes. **24 proyectos, 4 bloqueos, 6 vencimientos, 5 decisiones, 8 proyectos distintos con excepciones.** Fechas relativas de demostración; observaciones conservadas, no actualizadas artificialmente. Si ya hay datos, no los reemplaza; usar otro perfil/origen sin borrar el existente.

El acceso ocupa encabezados existentes para mantener densidad y controles de 44px. El detalle conserva el origen por proyecto **y grupo**, o vuelve a un control visible si la excepción desaparece. Se preservan medición directa, importación reconciliada/idempotente, historial, conflictos, borradores, backup y deshacer. Dominio, cálculo, unidades y zona horaria no se alteraron.

## 3D y fallos corregidos

Se inicializa una sola escena al abrir un proyecto, ninguna por fila. En desarrollo se comprobó ausencia de canvas/solicitud del motor mientras se consultaban listas; la PWA precarga su asset para offline, sin inicializar la escena.

La regresión de teclado reprodujo un fallo al reunir/desplegar rápido: las etiquetas podían seguir ocultas hasta el próximo frame. **S4:** disponibilidad DOM y estado de animación ahora cambian sincrónicamente; RAF solo representa. Caso determinista de enfocar/seleccionar en el mismo turno aprobado. No se añadieron efectos.

E1 corrigió la barra adicional que restaba una fila visible; E2 corrigió un contenedor heredado que ocultaba el acceso a 1024px. Se vuelven a mostrar ≥2 filas completas de cartera en horizontal y la acción/medición destacadas en iPhone. Desconocidos, cobertura, estimaciones heredadas y resultados medidos conservan su significado. A1/A2/A3 siguen protegidos.

## Verificación del 19/11

- **42 TypeScript + 4 Python**, aprobadas. Build aprobado.
- Batería **selectiva de 60 E2E**: 58 aprobadas y 2 reprodujeron S4 (mismo caso en ambos motores). Después de corregir: **24 afectadas finales**, 12 Chromium/12 WebKit, todas aprobadas, incluido el caso determinista. No se repitieron las 60 completas ni se suman repeticiones como casos únicos.
- **2 PWA Chromium** sobre build final, aprobadas. Instalación limpia con lockfile y build en carpeta temporal: **16 archivos de salida idénticos SHA-256**.
- Toque, ratón/teclado, orientaciones, modo oscuro/reducido, 24 proyectos, títulos largos, búsqueda, foco, medir/guardar/deshacer/recargar, fallos/conflictos, restauración e importar/deshacer/reimportar se comprobaron en emulación Linux. WebKit 27.2 no es Safari físico.
- Grabación sintética nueva a velocidad normal y capturas preparadas localmente en `web/docs/revision/`, nombres fijos. Los resultados del 17/11 quedan históricos en Git; no se presentan como verificación nueva.

**Safari/iPad físico: pendiente, NO ejecutado por falta de acceso.** No se han validado fluidez, precisión táctil, trackpad, teclado virtual ni fps del dispositivo real. No se repitió el perfil RAF: p95 ≈300 ms en VM SwiftShader del 17/11 es histórico, no un resultado del 19/11 ni del iPad. V2 sigue abierto. Sin blur completo ni promesas de 60/120 fps.

Fuentes locales vigentes: web/README.md, BRIEF.md, DESIGN.md, DECISIONES.md y docs/VERIFICACION.md. Historial/evidencia anterior en Git, sin nuevas memorias.

## Abrir, recuperar y siguiente paso

Desde web/: `npm ci`, `npm run dev -- --host 127.0.0.1 --port 5177`; build con `npm run build`. No secretos ni variables obligatorias. El entorno solo ofrece SSH, **sin URL HTTP de vista previa para iPad**; localhost pertenece al servidor. No se abrió túnel ni se desplegó.

Ajustes → Exportar backup JSON antes de actualizar. Restaurar en origen vacío compatible y verificar unidades/observaciones/historial. Rollback en checkout separado con backup; no hacer reset sobre trabajo posterior ni borrar IndexedDB. `bd23cbc` conserva la entrega anterior, `8386748` los arreglos de integridad sin 3D. Visual7 original se conserva pero contiene fallos ya corregidos.

**Siguiente paso concreto:** ejecutar sobre esta app y demo de 24 el recorrido Safari/iPad **abrir → seleccionar → medir 84→100/200 → guardar 50 %/faltan 100 → deshacer 42 %/faltan 116 → cerrar al mismo grupo**. Registrar modelo, iPadOS/Safari, orientación, foco, precisión táctil/trackpad y perfil del dispositivo; corregir hallazgos antes de efectos nuevos. V1 define el cierre. Acceso al dispositivo pendiente, sin pedir a Bruno otro traslado de archivos.

R1 conserva pendiente `ScreenRecording_11-17-2026 09-20-53_1.mp4` (~8,47s) e imágenes originales. No se afirma haberlos observado ni contrastado de nuevo; la descripción del gestor no demuestra tiempo real. Nuestro vídeo no es esa referencia. Sin backend, sincronización, Hermes, runners, agenda nueva, servicios de pago o IA para consultar/editar/calcular.

## Protocolo y acceso compartido

Leer esta nota y FALLOS desde main y confirmar commit en cada sesión. Si no se dispone de fuente local, declararlo; el código no está publicado. Un responsable de escritura; paralelo solo con checkout/rama propios. Claude opcional. No cargar diarios/log completo o notas personales para frontend.

Escapar valores externos en HTML o usar DOM/dataset, CSS.escape solo selectores. No reinterpretar unidades observadas; conversión explícita pendiente. Cachés de submeta por proyecto/submeta, origen por proyecto/grupo. Animaciones no gobiernan guardado ni disponibilidad de controles. Actualizar archivos vigentes y retirar solo generados propios; no ZIP, dist, node_modules, secretos o capturas descartadas en Git.

ChatGPT gestor: Ajustes → Apps/Plugins → GitHub → autorizar midememv-sys/Centrodemandos y leer esta nota desde main. En GPT personalizado, habilitar Apps si su configuración lo permite; si no, usar un chat normal compatible. Conocimiento subido es una copia estática. No pegar tokens ni cambiar visibilidad. La centralización Markdown no autoriza publicar código/medios, desplegar o activar gasto.
