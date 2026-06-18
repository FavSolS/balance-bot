# Diccionario de datos

Descripción de las variables, entidades y archivos que maneja **Paquito** (balance-bot) para la vidriería.

---

## Entidades del dominio

### Movimiento

Registro de un ingreso o egreso de caja. Es la entidad principal del sistema.

| Campo       | Tipo    | Descripción |
|-------------|---------|-------------|
| `fecha`     | fecha   | Día en que se registró el movimiento (`YYYY-MM-DD`). Se asigna automáticamente al guardar. |
| `tipo`      | texto   | `"ingreso"` o `"egreso"`. |
| `categoria` | texto   | Subtipo según el movimiento (ver tablas abajo). |
| `monto`     | número  | Importe en pesos. Debe ser mayor a 0. Acepta decimales (ej.: `2350.50`). |
| `concepto`  | texto   | Descripción breve del movimiento ingresada por el usuario. |

**Categorías de ingreso**

| Valor en CSV | Opción en el bot | Uso típico |
|--------------|------------------|------------|
| `venta`      | 1 — Venta en mostrador | Cobro de productos vendidos en el local. |
| `seña`       | 2 — Seña de pedido | Anticipo de un pedido a medida. |
| `otro`       | 3 — Otro | Ingresos que no encajan en las categorías anteriores. |

**Categorías de egreso**

| Valor en CSV | Opción en el bot | Uso típico |
|--------------|------------------|------------|
| `compra`     | 1 — Compra de materiales | Vidrio, insumos, herrajes, etc. |
| `gasto fijo` | 2 — Gasto fijo | Alquiler, servicios, impuestos recurrentes. |
| `retiro`     | 3 — Retiro personal | Extracción de efectivo del dueño o socio. |

---

### Pedido *(preparado, no expuesto en el bot aún)*

Entidad definida en código para futura gestión de pedidos. Hoy no hay flujo en Telegram que la use.

| Campo         | Tipo  | Descripción |
|---------------|-------|-------------|
| `fecha`       | fecha | Fecha de alta del pedido. |
| `descripcion` | texto | Detalle del pedido (medidas, tipo de vidrio, cliente, etc.). |
| `estado`      | texto | Estado del pedido. Al crear se guarda como `"pendiente"`. |

---

### Balance del día

Valor calculado, no persistido. Se obtiene sumando movimientos de la fecha actual.

| Concepto          | Fórmula |
|-------------------|---------|
| Total ingresos    | Suma de montos donde `tipo = ingreso` y `fecha = hoy` |
| Total egresos     | Suma de montos donde `tipo = egreso` y `fecha = hoy` |
| Balance           | `total_ingresos - total_egresos` |

Si el balance es negativo, el bot envía una alerta automática al consultarlo (opción 3 del menú).

---

## Estado de conversación (en memoria)

El bot usa una máquina de estados por usuario de Telegram. No se guarda en disco; se pierde al reiniciar el proceso.

| Estado           | Descripción |
|------------------|-------------|
| `MENU_PRINCIPAL` | Menú inicial. Estado por defecto de usuarios nuevos. |
| `ELEG_TIPO_ING`  | El usuario está eligiendo categoría de ingreso. |
| `ELEG_TIPO_EGR`  | El usuario está eligiendo categoría de egreso. |
| `INGR_MONTO`     | Esperando monto del movimiento (ingreso o egreso). |
| `INGR_CONCEPTO`  | Esperando descripción del movimiento. |
| `CONFIRMAR`      | Mostrando resumen; el usuario confirma o cancela. |

**Datos temporales por usuario** (mientras completa un registro):

| Clave       | Contenido |
|-------------|-----------|
| `tipo`      | `"ingreso"` o `"egreso"` |
| `categoria` | Una de las categorías listadas arriba |
| `monto`     | Número ya validado |
| `concepto`  | Texto ingresado por el usuario |

Al confirmar el registro o cancelar, estos datos se borran y el estado vuelve a `MENU_PRINCIPAL`.

---

## Archivos persistentes (CSV)

### `movimientos.csv`

Base de datos simulada de la caja. Se crea automáticamente en la raíz del proyecto si no existe.

```csv
fecha,tipo,categoria,monto,concepto
2026-06-18,ingreso,venta,15000.0,Venta espejo 60x80
2026-06-18,egreso,compra,3200.0,Vidrio templado 6mm
```

| Columna    | Tipo   | Obligatorio | Notas |
|------------|--------|-------------|-------|
| `fecha`    | fecha  | Sí          | Generada por el sistema al guardar. |
| `tipo`     | texto  | Sí          | `ingreso` \| `egreso` |
| `categoria`| texto  | Sí          | Ver tablas de categorías. |
| `monto`    | número | Sí          | Positivo. |
| `concepto` | texto  | Sí          | No vacío. |

---

### `pedidos.csv` *(preparado, no en uso)*

```csv
fecha,descripcion,estado
```

| Columna       | Tipo  | Obligatorio | Notas |
|---------------|-------|-------------|-------|
| `fecha`       | fecha | Sí          | Generada al guardar. |
| `descripcion` | texto | Sí          | Detalle del pedido. |
| `estado`      | texto | Sí          | Por defecto: `pendiente`. |

---

## Variables de entorno

| Variable | Archivo | Descripción |
|----------|---------|-------------|
| `TOKEN`  | `.env`  | Token del bot de Telegram obtenido desde [@BotFather](https://t.me/BotFather). No se sube al repositorio. |

---

## Identificadores de Telegram

| Concepto   | Uso en el código | Descripción |
|------------|------------------|-------------|
| `user_id`  | `update.message.chat_id` | Identifica la conversación/usuario. Clave para estado y datos temporales. |

---

## Validaciones aplicadas

| Dato     | Regla | Mensaje al usuario |
|----------|-------|--------------------|
| Monto    | Número positivo (`float > 0`) | *"El monto debe ser un numero positivo..."* |
| Opción   | Debe ser una de las listadas (`1`, `2`, `3`, etc.) | *"Opcion no reconocida..."* |
| Concepto | Texto no vacío (sin contar espacios) | *"El concepto no puede estar vacio..."* |
