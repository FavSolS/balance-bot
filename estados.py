# estados.py

# diccionario que guarda el estado actual de cada usuario
# clave: user_id (numero que da Telegram)
# valor: string con el nombre del estado
_estados = {}

# diccionario que guarda datos temporales mientras el usuario
# esta en medio de un registro (tipo, monto, concepto, etc)
_datos_temporales = {}


def get_estado(user_id):
    # si el usuario es nuevo, lo mandamos al menu principal
    return _estados.get(user_id, "MENU_PRINCIPAL")


def set_estado(user_id, nuevo_estado):
    _estados[user_id] = nuevo_estado


def reset_estado(user_id):
    # vuelve al menu y limpia los datos temporales
    _estados[user_id] = "MENU_PRINCIPAL"
    _datos_temporales.pop(user_id, None)


def guardar_dato_temp(user_id, clave, valor):
    # guarda un dato intermedio, por ejemplo el monto
    # antes de tener el concepto
    if user_id not in _datos_temporales:
        _datos_temporales[user_id] = {}
    _datos_temporales[user_id][clave] = valor


def get_dato_temp(user_id, clave):
    return _datos_temporales.get(user_id, {}).get(clave, None)


def get_todos_datos_temp(user_id):
    return _datos_temporales.get(user_id, {})