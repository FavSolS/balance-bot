# balance-bot

# Bot de Caja — Vidriería

Chatbot desarrollado en Python con Telegram Bot API para la gestión diaria de caja de un pequeño comercio. Permite registrar ingresos y egresos, gestionar pedidos y consultar el balance del día.

Desarrollado como Trabajo Práctico Integrador para la materia Organización Empresarial — TUP UTN.

---

## Tecnologías utilizadas

- Python 3
- python-telegram-bot 22.8
- python-dotenv
- CSV como base de datos simulada

---

## Estructura del proyecto
balance-bot/

├── main.py           # arranque del bot y conexión con Telegram

├── handlers.py       # lógica principal según estado del usuario

├── estados.py        # máquina de estados por usuario

├── menu.py           # textos y mensajes del bot

├── validaciones.py   # validación de datos ingresados

├── datos.py          # lectura y escritura de archivos CSV

├── requirements.txt  # dependencias del proyecto

├── .env              # token de Telegram (no se sube a GitHub)

└── .gitignore

---

## Cómo inicializar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/balance-bot.git
cd balance-bot
```

### 2. Crear y activar el entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar el token de Telegram

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:
TOKEN=tu_token_aqui

Para obtener el token:
1. Abrí Telegram y buscá **@BotFather**
2. Mandá el comando `/newbot`
3. Seguí los pasos y copiá el token que te da

### 5. Correr el bot

```bash
python3 main.py
```

Si el bot inició correctamente vas a ver:
Bot iniciado, esperando mensajes...


### 6. Usar el bot

Buscá tu bot en Telegram por el username que le diste a BotFather y mandále un mensaje para comenzar.

---

## Funcionalidades

- Registrar ingresos con categoría (venta, seña, otro)
- Registrar egresos con categoría (compra, gasto fijo, retiro)
- Validación de datos con manejo de errores
- Consultar balance del día
- Alerta automática si el balance es negativo
- Cierre de caja diario
- Persistencia de datos en archivos CSV

---

## Autores

- Agustín Chaves
- María Sol Savid Patoco

Tecnicatura Universitaria en Programación — Universidad Tecnológica Nacional