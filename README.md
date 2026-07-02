# 🔋 EV Battery Passport Intelligence Platform

AI-powered EV Battery Health Intelligence Platform built with a **Teacher–Student Machine Learning architecture**, **FastAPI**, **React**, **Docker**, **PostgreSQL**, and **MLflow** for battery health prediction, lifecycle monitoring, and production-grade MLOps.

---

## 🚀 Features

- 🔹 Teacher–Student ML architecture for battery degradation prediction
- 🔹 FastAPI REST APIs for real-time inference
- 🔹 React + Vite interactive dashboard
- 🔹 PostgreSQL integration for vehicle registration and prediction logging
- 🔹 MLflow experiment tracking and Model Registry
- 🔹 Dockerized frontend, backend, and database
- 🔹 DVC-based dataset versioning
- 🔹 Prediction history and battery analytics

---

## 🏗️ System Architecture

<p align="center">
    <img src="assets/architecture.png" width="900">
</p>

---

## 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Frontend | React, Vite |
| Backend | FastAPI |
| Machine Learning | Scikit-Learn, Teacher–Student Learning |
| Database | PostgreSQL |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Containerization | Docker, Docker Compose |
| Visualization | Matplotlib, Seaborn |

---

## 📂 Project Structure

```text
EV-Battery-Passport-Intelligence-Platform/
│
├── backend/
├── frontend/
├── data/
├── models/
├── results/
├── notebooks/
├── assets/
│   └── architecture.png
├── docker-compose.yml
├── Dockerfile
├── train_student_model.py
├── anomaly_detection.py
├── README.md
```

---

## ⚙️ Getting Started

### Clone Repository

```bash
git clone https://github.com/HarshGangurde/EV-Battery-Passport-Intelligence-Platform.git

cd EV-Battery-Passport-Intelligence-Platform
```

### Run using Docker

```bash
docker compose up --build
```

---

## 🌐 Access the Application

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| FastAPI | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |
| PostgreSQL | localhost:5432 |

---

## 📊 ML Pipeline

```
Battery Dataset
        │
        ▼
Teacher Models
(Virtual Sensor Prediction)
        │
        ▼
Latent Feature Generation
        │
        ▼
Student SOH Model
        │
        ▼
FastAPI Inference
        │
        ▼
Prediction Logging
(PostgreSQL)
```

---

## 📈 MLflow

Track experiments and compare model performance using MLflow.

```bash
mlflow ui
```

Open:

```
http://localhost:5000
```

---

## 📸 Application Preview

### Dashboard

<img src="assets/dashboard.png">

### Battery Prediction

<img src="assets/prediction.png">

### MLflow Tracking

<img src="assets/mlflow.png">

---

## 📌 Future Improvements

- Battery anomaly detection
- Battery lifecycle forecasting
- Model monitoring dashboard
- CI/CD with GitHub Actions
- Cloud deployment (AWS)

---

## 👨‍💻 Author

**Harsh Gangurde**

AI Engineer | Machine Learning | MLOps

- GitHub: https://github.com/HarshGangurde
- LinkedIn: https://www.linkedin.com/in/harsh-gangurde/

---

⭐ If you found this project useful, consider giving it a star!
