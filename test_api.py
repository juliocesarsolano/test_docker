import requests
import time

# Esperar unos segundos para asegurarse de que Flask ya esté corriendo
time.sleep(3)

url = "http://localhost:8000/predict"
data = {
    "features": [0.038, 0.05, 0.061, 0.021, -0.044, -0.034, -0.043, -0.002, 0.019, -0.017]
}

try:
    response = requests.post(url, json=data)
    print("✅ Respuesta:", response.json())
except Exception as e:
    print("❌ Error al conectar con la API:", e)