# handlers.py
from estados import get_estado, set_estado, reset_estado, guardar_dato_temp, get_dato_temp, get_todos_datos_temp
from validaciones import es_monto_valido, es_opcion_valida, es_texto_valido, convertir_monto
from datos import guardar_movimiento, calcular_balance_hoy
from menu import (
    BIENVENIDA, PEDIR_TIPO_INGRESO, PEDIR_TIPO_EGRESO,
    PEDIR_MONTO, PEDIR_CONCEPTO, MONTO_INVALIDO,
    OPCION_INVALIDA, TEXTO_INVALIDO, REGISTRO_GUARDADO,
    REGISTRO_CANCELADO, confirmar_registro,
    balance_del_dia, alerta_balance_negativo
)

TIPOS_INGRESO = {"1": "venta", "2": "seña", "3": "otro"}
TIPOS_EGRESO  = {"1": "compra", "2": "gasto fijo", "3": "retiro"}


async def manejar_mensaje(update, context):
    user_id = update.message.chat_id
    texto   = update.message.text.strip()
    estado  = get_estado(user_id)

    # ---- MENU PRINCIPAL ----
    if estado == "MENU_PRINCIPAL":
        if texto == "1":
            set_estado(user_id, "ELEG_TIPO_ING")
            await update.message.reply_text(PEDIR_TIPO_INGRESO)

        elif texto == "2":
            set_estado(user_id, "ELEG_TIPO_EGR")
            await update.message.reply_text(PEDIR_TIPO_EGRESO)

        elif texto == "3":
            total_ing, total_egr, balance = calcular_balance_hoy()
            await update.message.reply_text(
                balance_del_dia(total_ing, total_egr, balance)
            )
            if balance < 0:
                await update.message.reply_text(
                    alerta_balance_negativo(balance)
                )
            # no cambia estado, vuelve a mostrar el menu
            await update.message.reply_text(BIENVENIDA)

        elif texto == "4":
            total_ing, total_egr, balance = calcular_balance_hoy()
            await update.message.reply_text(
                balance_del_dia(total_ing, total_egr, balance)
            )
            reset_estado(user_id)
            await update.message.reply_text("Caja cerrada. Hasta manana!")

        else:
            # camino infeliz: opcion no reconocida
            await update.message.reply_text(OPCION_INVALIDA)
            await update.message.reply_text(BIENVENIDA)

    # ---- ELEGIR TIPO INGRESO ----
    elif estado == "ELEG_TIPO_ING":
        if not es_opcion_valida(texto, ["1", "2", "3"]):
            await update.message.reply_text(OPCION_INVALIDA)
            await update.message.reply_text(PEDIR_TIPO_INGRESO)
            return

        guardar_dato_temp(user_id, "tipo", "ingreso")
        guardar_dato_temp(user_id, "categoria", TIPOS_INGRESO[texto])
        set_estado(user_id, "INGR_MONTO")
        await update.message.reply_text(PEDIR_MONTO)

    # ---- ELEGIR TIPO EGRESO ----
    elif estado == "ELEG_TIPO_EGR":
        if not es_opcion_valida(texto, ["1", "2", "3"]):
            await update.message.reply_text(OPCION_INVALIDA)
            await update.message.reply_text(PEDIR_TIPO_EGRESO)
            return

        guardar_dato_temp(user_id, "tipo", "egreso")
        guardar_dato_temp(user_id, "categoria", TIPOS_EGRESO[texto])
        set_estado(user_id, "INGR_MONTO")
        await update.message.reply_text(PEDIR_MONTO)

    # ---- INGRESAR MONTO ----
    elif estado == "INGR_MONTO":
        if not es_monto_valido(texto):
            # camino infeliz: monto invalido
            await update.message.reply_text(MONTO_INVALIDO)
            return  # no cambia estado, vuelve a pedir

        guardar_dato_temp(user_id, "monto", convertir_monto(texto))
        set_estado(user_id, "INGR_CONCEPTO")
        await update.message.reply_text(PEDIR_CONCEPTO)

    # ---- INGRESAR CONCEPTO ----
    elif estado == "INGR_CONCEPTO":
        if not es_texto_valido(texto):
            # camino infeliz: concepto vacio
            await update.message.reply_text(TEXTO_INVALIDO)
            return

        guardar_dato_temp(user_id, "concepto", texto)
        datos = get_todos_datos_temp(user_id)
        set_estado(user_id, "CONFIRMAR")
        await update.message.reply_text(
            confirmar_registro(
                datos["tipo"],
                datos["categoria"],
                datos["monto"],
                datos["concepto"]
            )
        )

    # ---- CONFIRMAR REGISTRO ----
    elif estado == "CONFIRMAR":
        if texto == "1":
            datos = get_todos_datos_temp(user_id)
            guardar_movimiento(
                datos["tipo"],
                datos["categoria"],
                datos["monto"],
                datos["concepto"]
            )
            reset_estado(user_id)
            await update.message.reply_text(REGISTRO_GUARDADO)
            await update.message.reply_text(BIENVENIDA)

        elif texto == "2":
            reset_estado(user_id)
            await update.message.reply_text(REGISTRO_CANCELADO)
            await update.message.reply_text(BIENVENIDA)

        else:
            # camino infeliz: respuesta no reconocida
            await update.message.reply_text(OPCION_INVALIDA)
            datos = get_todos_datos_temp(user_id)
            await update.message.reply_text(
                confirmar_registro(
                    datos["tipo"],
                    datos["categoria"],
                    datos["monto"],
                    datos["concepto"]
                )
            )

    # ---- ESTADO DESCONOCIDO (por las dudas) ----
    else:
        reset_estado(user_id)
        await update.message.reply_text(BIENVENIDA)