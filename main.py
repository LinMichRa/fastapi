from fastapi import FastAPI
import random

app = FastAPI(title="Servicio de cédula")

@app.get("/obtenercedula")
def obtener_cedula():
    numero = random.randint(1000000000, 9999999999)
    return {"cedula": numero}
