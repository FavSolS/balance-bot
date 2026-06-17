# datos.py
import csv
import os
from datetime import date

ARCHIVO_MOVIMIENTOS = "movimientos.csv"
ARCHIVO_PEDIDOS = "pedidos.csv"

COLUMNAS_MOVIMIENTOS = ["fecha", "tipo", "categoria", "monto", "concepto"]
COLUMNAS_PEDIDOS = ["fecha", "descripcion", "estado"]


def _inicializar_csv(archivo, columnas):
    # crea el archivo con encabezados si no existe todavia
    if not os.path.exists(archivo):
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=columnas)
            writer.writeheader()


def guardar_movimiento(tipo, categoria, monto, concepto):
    _inicializar_csv(ARCHIVO_MOVIMIENTOS, COLUMNAS_MOVIMIENTOS)
    with open(ARCHIVO_MOVIMIENTOS, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNAS_MOVIMIENTOS)
        writer.writerow({
            "fecha": date.today(),
            "tipo": tipo,
            "categoria": categoria,
            "monto": monto,
            "concepto": concepto
        })


def guardar_pedido(descripcion):
    _inicializar_csv(ARCHIVO_PEDIDOS, COLUMNAS_PEDIDOS)
    with open(ARCHIVO_PEDIDOS, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNAS_PEDIDOS)
        writer.writerow({
            "fecha": date.today(),
            "descripcion": descripcion,
            "estado": "pendiente"
        })


def calcular_balance_hoy():
    _inicializar_csv(ARCHIVO_MOVIMIENTOS, COLUMNAS_MOVIMIENTOS)
    hoy = str(date.today())
    total_ingresos = 0.0
    total_egresos = 0.0

    with open(ARCHIVO_MOVIMIENTOS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["fecha"] == hoy:
                if fila["tipo"] == "ingreso":
                    total_ingresos += float(fila["monto"])
                elif fila["tipo"] == "egreso":
                    total_egresos += float(fila["monto"])

    balance = total_ingresos - total_egresos
    return total_ingresos, total_egresos, balance


def obtener_movimientos_hoy():
    # devuelve todas las filas del dia de hoy
    _inicializar_csv(ARCHIVO_MOVIMIENTOS, COLUMNAS_MOVIMIENTOS)
    hoy = str(date.today())
    movimientos = []

    with open(ARCHIVO_MOVIMIENTOS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["fecha"] == hoy:
                movimientos.append(fila)

    return movimientos