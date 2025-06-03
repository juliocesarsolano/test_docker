# 🩺 Flask ML API: Predicción de Diabetes

Este proyecto despliega un modelo de regresión lineal entrenado con scikit-learn como una API REST con Flask, integrada en un contenedor Docker.  
Incluye un **dashboard interactivo** en Bootstrap para ingresar variables y obtener una predicción inmediata.

---

## 🚀 Características

- 🔁 Entrenamiento con scikit-learn (`LinearRegression`)
- 🌐 API REST con Flask (`/predict`)
- 📊 Interfaz web profesional con Bootstrap 5
- 🐳 Docker + Docker Compose listo para producción local
- 📦 Modelo pre-entrenado (`modelo.pkl`) incluido

---

## 🖥️ Vista previa del dashboard

![dashboard](docs/dashboard.png)

> Puedes reemplazar esta imagen con una captura tuya real en la carpeta `docs/`.

---

## 🧪 Cómo probar la API

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0.038, 0.05, 0.061, 0.021, -0.044, -0.034, -0.043, -0.002, 0.019, -0.017]}'
```

---

## 🛠️ Ejecución local con Docker

```bash
# Clona el repositorio
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo

# Construye y lanza el contenedor
docker compose up --build
```

Abre tu navegador en:

```
http://localhost:8000
```

---

## 📁 Estructura del proyecto

```
.
├── app.py
├── modelo.pkl
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── favicon.ico
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT.
