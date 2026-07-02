# 🔋 EV Battery Passport Intelligence Platform

An AI-powered EV Battery Passport platform that predicts battery degradation and health using a Teacher–Student Machine Learning architecture. The platform exposes production-style REST APIs with FastAPI, tracks experiments using MLflow, logs predictions into PostgreSQL, and is fully containerized using Docker.

---

# 🚀 System Architecture

```text
                           ┌────────────────────┐
                           │ React + Vite UI    │
                           │  Dashboard         │
                           └─────────┬──────────┘
                                     │
                                     │ REST API
                                     ▼
                     ┌────────────────────────────────┐
                     │        FastAPI Backend         │
                     │                                │
                     │ Vehicle Registration API       │
                     │ Battery Prediction API         │
                     │ Prediction Logging             │
                     └──────────────┬─────────────────┘
                                    │
                ┌───────────────────┼────────────────────┐
                │                   │                    │
                ▼                   ▼                    ▼
      Teacher Models         Student Model         PostgreSQL
 (Virtual Sensor Models)   (Battery Health)    Vehicle & Prediction Logs

                                    │
                                    ▼
                              MLflow Tracking
                          Experiments & Registry

```

---

# ✨ Features

- Teacher–Student Machine Learning Architecture
- Battery Health & Degradation Prediction
- Vehicle Registration APIs
- Prediction Logging in PostgreSQL
- MLflow Experiment Tracking
- MLflow Model Registry
- Dockerized Frontend + Backend + Database
- Interactive React Dashboard

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|-------------|
| Frontend | React, Vite |
| Backend | FastAPI |
| ML | Scikit-Learn |
| Database | PostgreSQL |
| Experiment Tracking | MLflow |
| Containerization | Docker, Docker Compose |
| Serialization | Joblib |

---

# 📂 Project Structure

```
EV_LOCAL_MLOPS
│
├── backend/
├── frontend/
├── models/
├── notebooks/
├── results/
├── docker-compose.yml
└── README.md
```

---

# ▶️ Run the Project

```bash
docker compose up --build
```

Frontend

```
http://localhost:5173
```

Backend

```
http://localhost:8000/docs
```

MLflow

```
http://localhost:5000
```

---

# 🔗 API Endpoints

| Method | Endpoint |
|---------|----------|
| POST | /register_vehicle |
| GET | /get_vehicles/{user_id} |
| POST | /predict |
| POST | /chat |

---

# 📊 Sample Prediction Output

```json
{
  "predicted_soh": 86.99,
  "degradation": 13.01,
  "estimated_soc": 100,
  "risk_rating": "Low Risk",
  "anomaly_warning": false,
  "model_version": "Student-v1"
}
```

---

# 📈 Highlights

- Teacher–Student ML Architecture
- Virtual Sensor Estimation
- Experiment Tracking with MLflow
- Model Registry
- Prediction Audit Logging
- Production-ready Docker Deployment

---

## 👨‍💻 Author

**Harsh Gangurde**

AI Engineer | Machine Learning | MLOps | FastAPI | Docker | PostgreSQL
