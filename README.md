# 🍽️ Swiggy Delivery Time Prediction

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-green)](https://fastapi.tiangolo.com/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)](https://mlflow.org/)
[![DVC](https://img.shields.io/badge/DVC-Pipeline-red)](https://dvc.org/)

> **End-to-End Machine Learning System** for predicting food delivery time using ensemble methods, complete MLOps pipeline, and production-ready REST API.

---

## 🎯 Overview

This project predicts food delivery time in minutes for Swiggy orders using advanced machine learning techniques. Built with **MLOps best practices**, it includes:

- ✅ **Automated ML Pipeline** with DVC
- ✅ **Experiment Tracking** with MLflow & DagsHub
- ✅ **Production-Ready API** with FastAPI
- ✅ **Model Registry** for version control
- ✅ **Docker Support** for containerization

**Model:** Stacking Regressor (Random Forest + LightGBM)  
**Performance:** R² Score ~0.82, MAE ~5-6 minutes

---

## 🎬 Model Interface Preview

Watch a quick demo of how the model behaves while interacting with user input:

- [▶ View Preview Video](./Swiggy_Delivery_Time_Prediction.mp4)

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **ML/DS** | Python, scikit-learn, LightGBM, pandas, numpy |
| **MLOps** | DVC, MLflow, DagsHub |
| **API** | FastAPI, Uvicorn, Pydantic |
| **DevOps** | Docker, Git |

---

## 🚀 Quick Start

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/AshutoshMishra-UJ/Delivery_Time-Prediction.git
cd Delivery_Time-Prediction

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements-dev.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your credentials

# 5. Install the project package
pip install -e .
```

### Run the Application

```bash
# Start the API server
python app.py

# API available at: http://localhost:8000
# API Docs at: http://localhost:8000/docs
```

---

## ⚙️ Configuration

Create `.env` file with your credentials:

```bash
# DagsHub Configuration (optional for experiment tracking)
DAGSHUB_USER_NAME=AshutoshMishra-UJ
DAGSHUB_REPO_NAME=Delivery_Time-Prediction
DAGSHUB_TOKEN=your_token_here  # Get from https://dagshub.com/user/settings/tokens

# Model Configuration
MODEL_NAME=delivery_time_prediction_model
MODEL_STAGE=Production

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

---

## 📖 Usage

### Train Model from Scratch

```bash
# Run complete ML pipeline
dvc repro
```

### Make Predictions via API

```python
import requests

data = {
    "ID": "order_001",
    "Delivery_person_ID": "person_123",
    "Delivery_person_Age": "25",
    "Delivery_person_Ratings": "4.5",
    "Restaurant_latitude": 12.9716,
    "Restaurant_longitude": 77.5946,
    "Delivery_location_latitude": 12.9352,
    "Delivery_location_longitude": 77.6245,
    "Order_Date": "01-01-2024",
    "Time_Orderd": "12:30",
    "Time_Order_picked": "12:45",
    "Weatherconditions": "Sunny",
    "Road_traffic_density": "High",
    "Vehicle_condition": 2,
    "Type_of_order": "Meal",
    "Type_of_vehicle": "motorcycle",
    "multiple_deliveries": "1",
    "Festival": "No",
    "City": "Urban"
}

response = requests.post("http://localhost:8000/predict", json=data)
print(f"Predicted delivery time: {response.json()} minutes")
```

---

## 🔌 API Endpoints

- `GET /` - Welcome message
- `POST /predict` - Predict delivery time
- `GET /docs` - Interactive API documentation

---

## 📊 Model Performance

| Model | R² Score | MAE | RMSE |
|-------|----------|-----|------|
| Random Forest | 0.79 | 6.1 | 8.3 |
| LightGBM | 0.80 | 5.8 | 8.0 |
| **Stacking (RF+LGBM)** | **0.82** | **5.4** | **7.6** |

---

## 🐳 Docker Deployment

```bash
# Build image
docker build -t swiggy-prediction .

# Run container
docker run -p 8000:8000 swiggy-prediction
```

---

## 📚 Documentation

- **Project Overview:** [PROJECT_OVERVIEW_FOR_INTERVIEW.md](PROJECT_OVERVIEW_FOR_INTERVIEW.md)
- **GitHub Setup:** [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md)
- **API Docs:** http://localhost:8000/docs

---

## 📁 Project Structure

```
├── data/               # Datasets (raw, processed)
├── src/               # Source code
│   ├── config.py     # Configuration management
│   ├── data/         # Data processing
│   ├── features/     # Feature engineering
│   └── models/       # Training & evaluation
├── notebooks/        # Jupyter notebooks
├── models/          # Saved models
├── app.py           # FastAPI application
├── dvc.yaml         # DVC pipeline
└── .env.example     # Environment template
```

---

## 👤 Author

**Ashutosh Mishra**
- GitHub: [@AshutoshMishra-UJ](https://github.com/AshutoshMishra-UJ)

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ **Star this repository** if you find it helpful!

**Built with ❤️ using Python & FastAPI**
