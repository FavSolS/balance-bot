# validaciones.py

def es_monto_valido(texto):
    # verifica que el texto sea un numero positivo
    # acepta enteros (1500) y decimales (1500.50)
    try:
        monto = float(texto)
        return monto > 0
    except ValueError:
        return False


def es_opcion_valida(texto, opciones_validas):
    # verifica que el texto sea una de las opciones permitidas
    # opciones_validas es una lista, por ejemplo ["1", "2", "3"]
    return texto.strip() in opciones_validas


def es_texto_valido(texto):
    # verifica que el concepto no este vacio ni sea solo espacios
    return texto.strip() != ""


def convertir_monto(texto):
    # convierte el texto a float una vez que ya fue validado
    return float(texto)