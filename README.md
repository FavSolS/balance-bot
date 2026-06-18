# balance-bot

# Bot de Caja — Vidriería (Paquito)

Chatbot desarrollado en Python con Telegram Bot API para la gestión diaria de caja de un pequeño comercio. Permite registrar ingresos y egresos, consultar el balance del día y simular el cierre de caja.

Desarrollado como Trabajo Práctico Integrador para la materia **Organización Empresarial** — TUP UTN.

---

## Tecnologías utilizadas

- Python 3
- [python-telegram-bot](https://docs.python-telegram-bot.org/) 22.8
- python-dotenv
- CSV como base de datos simulada

---

## Estructura del proyecto

```
balance-bot/
├── main.py              # Arranque del bot y conexión con Telegram
├── handlers.py          # Lógica principal según estado del usuario
├── estados.py           # Máquina de estados por usuario
├── menu.py              # Textos y mensajes del bot
├── validaciones.py      # Validación de datos ingresados
├── datos.py             # Lectura y escritura de archivos CSV
├── requirements.txt     # Dependencias del proyecto
├── docs/                # Documentación ampliada (ver sección Documentación)
├── .env                 # Token de Telegram (no se sube a GitHub)
└── .gitignore
```

Archivos generados en runtime (no versionados por defecto):

- `movimientos.csv` — registros de ingresos y egresos
- `pedidos.csv` — preparado para futura gestión de pedidos

---

## Cómo inicializar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/balance-bot.git
cd balance-bot
```

### 2. Crear y activar el entorno virtual

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar el token de Telegram

Crear un archivo `.env` en la raíz del proyecto:

```env
TOKEN=tu_token_aqui
```

Para obtener el token:

1. Abrí Telegram y buscá **@BotFather**
2. Mandá el comando `/newbot`
3. Seguí los pasos y copiá el token que te da

### 5. Correr el bot

```bash
python main.py
```

Si el bot inició correctamente vas a ver:

```
🏪 Paquito iniciado, esperando mensajes.
```

### 6. Usar el bot

Buscá tu bot en Telegram por el username que le diste a BotFather y mandále un mensaje para comenzar. Consultá el [Manual de usuario](docs/manual-usuario.md) para el detalle de cada opción.

---

## Funcionalidades

| Funcionalidad | Descripción |
|---------------|-------------|
| Registrar ingresos | Categorías: venta, seña, otro |
| Registrar egresos | Categorías: compra, gasto fijo, retiro |
| Validación de datos | Montos positivos, opciones de menú y conceptos no vacíos |
| Balance del día | Suma ingresos y egresos de la fecha actual |
| Alerta de balance negativo | Aviso automático al consultar balance si el resultado es negativo |
| Cierre de caja | Resumen del día y reinicio de la conversación |
| Persistencia | Movimientos guardados en `movimientos.csv` |

> **Nota:** la gestión de pedidos está preparada en código (`pedidos.csv`) pero aún no está disponible desde el menú del bot.

---

## Documentación y calidad

| Documento | Contenido |
|-----------|-----------|
| [Manual de usuario](docs/manual-usuario.md) | Guía paso a paso: menú, registro de movimientos, balance y cierre de caja |
| [Diccionario de datos](docs/diccionario-datos.md) | Variables, entidades, estados, archivos CSV y validaciones |
| [Proceso de desarrollo](docs/proceso-desarrollo.md) | BPMN AS-IS/TO-BE, decisiones técnicas, arquitectura e integración de 9 capturas de IA |
| [Capturas IA](docs/assets/conversaciones-ia/) | Imágenes fuente de las conversaciones de diseño |

### Diccionario de datos (resumen)

- **Movimiento:** `fecha`, `tipo` (ingreso/egreso), `categoria`, `monto`, `concepto`
- **Estados de conversación:** `MENU_PRINCIPAL`, `ELEG_TIPO_ING`, `ELEG_TIPO_EGR`, `INGR_MONTO`, `INGR_CONCEPTO`, `CONFIRMAR`
- **Archivos:** `movimientos.csv` (en uso), `pedidos.csv` (futuro)

Detalle completo en [docs/diccionario-datos.md](docs/diccionario-datos.md).

### Manual de usuario (resumen)

El bot responde a números de texto en cada pantalla:

1. **Menú:** `1` ingreso · `2` egreso · `3` balance · `4` cerrar caja  
2. **Registro:** elegir categoría → monto → concepto → confirmar (`1` sí / `2` no)

Detalle completo con diagramas de flujo en [docs/manual-usuario.md](docs/manual-usuario.md).

---

## Autores

- Agustín Chaves
- María Sol Savid Patoco

Tecnicatura Universitaria en Programación — Universidad Tecnológica Nacional
