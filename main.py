from fastapi import FastAPI
import random

app = FastAPI(title="Servicio de cédula")


@app.get("/obtenercedula")
def obtener_cedula():
    numero = random.randint(1000000000, 9999999999)
    return {"cedula": numero}


def convertir_a_romano(numero: int) -> str:
    valores = (
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )
    romano = ""

    for valor, simbolo in valores:
        while numero >= valor:
            romano += simbolo
            numero -= valor

    return romano


@app.get("/obtenerromano")
def obtener_romano():
    numero = random.randint(50, 100)
    return {"romano": convertir_a_romano(numero)}

