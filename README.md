# 🌱 AI Crop Yield Prediction and Farming Optimization

## 📌 Project Overview

AI Crop Yield Prediction and Farming Optimization is a machine learning-based web application that helps farmers make better agricultural decisions. The system predicts crop yield based on environmental parameters and recommends the most suitable crop for cultivation using AI models.

The project aims to improve farming productivity by providing intelligent recommendations that support data-driven agriculture.

---

## 🚀 Features

* 🌾 Crop Yield Prediction
* 🌱 Crop Recommendation
* 📊 Machine Learning-based Prediction
* 🌐 User-Friendly Flask Web Interface
* 📈 Fast and Accurate Predictions
* 💾 Prediction History (Optional)
* 📱 Responsive Web Design

---

## 🛠 Technologies Used

### Programming Language

* Python

### Framework

* Flask

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Joblib

### Frontend

* HTML
* CSS
* JavaScript

### Development Tools

* VS Code
* Git
* GitHub

---

## 📂 Project Structure

```text
AI_Crop_Project/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── index.html
│   │   ├── recommend.html
│   │   └── predict.html
│   │
│   └── app.py
│
├── data/
│   └── Crop_recommendation.csv
│
├── model/
│   └── crop_model.pkl
│
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Vinitha-paulin/AI-crop-prediction-and-yield-optimization.git
```

### 2. Move to the Project Folder

```bash
cd AI_Crop_Project
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📊 Input Parameters

The prediction model uses the following parameters:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature (°C)
* Humidity (%)
* Rainfall (mm)

---

## 🌾 Crop Recommendation

Based on the soil nutrients and climatic conditions, the application recommends the most suitable crop for cultivation.

Example outputs include:

* Rice
* Wheat
* Maize
* Cotton
* Chickpea
* Coffee
* Mango
* Banana

---

## 📈 Crop Yield Prediction

The system predicts the expected crop yield using machine learning algorithms trained on agricultural datasets.

This helps farmers estimate production before cultivation.

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Model Saving
7. Web Application Deployment

---

## 👩‍💻 Author

**Vinitha Paulin**

Bachelor of Engineering (Electronics and Communication Engineering)

---

## 📄 License

This project is developed for educational and research purposes.
