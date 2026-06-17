# menu.py
BOT_INICIADO = "🏪 Paquito iniciado, esperando mensajes."

BIENVENIDA = (
    "Bienvenido al sistema de caja 🏪\n"
    "Vidrieria familiar\n\n"
    "Que deseas hacer?\n"
    "1 - Registrar ingreso\n"
    "2 - Registrar egreso\n"
    "3 - Ver balance del dia\n"
    "4 - Cerrar caja del dia\n\n"
    "Paquito a tu disposicion!"
)

PEDIR_TIPO_INGRESO = (
    "Tipo de ingreso:\n"
    "1 - Venta en mostrador\n"
    "2 - Seña de pedido\n"
    "3 - Otro"
)

PEDIR_TIPO_EGRESO = (
    "Tipo de egreso:\n"
    "1 - Compra de materiales\n"
    "2 - Gasto fijo\n"
    "3 - Retiro personal"
)

PEDIR_MONTO = "Ingresa el monto:"

PEDIR_CONCEPTO = "Describe brevemente el movimiento:"

MONTO_INVALIDO = (
    "El monto debe ser un numero positivo.\n"
    "Por ejemplo: 1500 o 2350.50\n"
    "Intenta de nuevo:"
)

OPCION_INVALIDA = (
    "Opcion no reconocida.\n"
    "Por favor elegí una de las opciones del menu."
)

TEXTO_INVALIDO = (
    "El concepto no puede estar vacio.\n"
    "Describe brevemente el movimiento:"
)

def confirmar_registro(tipo, categoria, monto, concepto):
    return (
        f"Confirmas el registro?\n\n"
        f"Tipo: {tipo}\n"
        f"Categoria: {categoria}\n"
        f"Monto: ${monto}\n"
        f"Concepto: {concepto}\n\n"
        f"1 - Si, guardar\n"
        f"2 - No, cancelar"
    )

def balance_del_dia(total_ingresos, total_egresos, balance):
    signo = "POSITIVO" if balance >= 0 else "NEGATIVO"
    return (
        f"Balance del dia:\n\n"
        f"Total ingresos: ${total_ingresos}\n"
        f"Total egresos: ${total_egresos}\n"
        f"Balance: ${balance} ({signo})"
    )

def alerta_balance_negativo(balance):
    return (
        f"🚨 Atencion: el balance del dia es negativo. \n"
        f"💰 Balance actual: ${balance}\n"
        f"💸 Revisa los movimientos registrados."
    )

REGISTRO_GUARDADO = "🤑 Movimiento guardado correctamente. Volviendo al menu."

REGISTRO_CANCELADO = "❌ Registro cancelado. Volviendo al menu."

CAJA_CERRADA = "🔒 Caja cerrada. Hasta manana!"