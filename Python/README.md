# 💳 Credit Card Fraud Analytics & Machine Learning Prediction System

## 📌 Project Objective

This project was developed to demonstrate end-to-end Data Analytics and Machine Learning skills by analysing real-world credit card transaction data and building a fraud prediction system.

The project begins with understanding and analysing the dataset using Exploratory Data Analysis (EDA), identifying fraud patterns, performing feature engineering, and preparing the data for Machine Learning.

A Random Forest Classifier was then trained to predict whether a transaction is Genuine or Fraudulent.

Finally, the trained model was deployed using FastAPI as a REST API capable of providing real-time fraud predictions along with business-friendly risk recommendations.

This project demonstrates practical skills required for Data Analyst and Machine Learning roles.


## 🏦 Business Problem

Credit card fraud is one of the biggest challenges faced by financial institutions. Every day, millions of transactions are processed, making it difficult to identify fraudulent activities in real time.

A delayed or incorrect fraud detection decision can lead to financial losses, customer dissatisfaction, and security risks.

This project aims to analyse transaction data, identify fraud-related patterns, and build a prediction system that assists financial institutions in classifying transactions based on their fraud risk.


## 📂 Dataset Overview

The project uses the **Credit Card Fraud Detection Dataset**, which contains anonymised credit card transactions made by European cardholders.

### Dataset Information

- Total Transactions: **284,807**
- Genuine Transactions: **284,315**
- Fraudulent Transactions: **492**
- Fraud Rate: **0.17%**
- Features: **30 input features + 1 target column (Class)**

### Important Columns

- **Time** – Time elapsed between transactions
- **Amount** – Transaction amount
- **V1 – V28** – Anonymised features generated using Principal Component Analysis (PCA)
- **Class** – Target variable
  - 0 = Genuine Transaction
  - 1 = Fraudulent Transaction


## 📊 Data Cleaning & Exploratory Data Analysis (EDA)

Before building the Machine Learning model, the dataset was thoroughly analysed to understand transaction behaviour and fraud patterns.

### Data Cleaning

The following preprocessing steps were performed:

- Checked dataset shape and data types
- Verified missing values
- Identified duplicate records
- Removed duplicate transactions
- Validated target variable distribution

### Exploratory Data Analysis (EDA)

The following analyses were performed:

- Analysed class imbalance between Genuine and Fraud transactions
- Examined transaction amount distribution
- Compared fraud and genuine transaction amounts
- Created transaction hour from the Time feature
- Created Log Amount feature to reduce skewness
- Generated a correlation heatmap
- Identified important fraud-related features such as V14, V17, V12 and V10
- Analysed feature relationships with the target variable (Class)

### Key Insights

- The dataset is highly imbalanced with only **0.17% fraudulent transactions**
- Fraudulent transactions showed different behaviour compared to genuine transactions
- Certain anonymised features (especially V14, V17, V12 and V10) were highly correlated with fraud
- Feature engineering improved the quality of the input data before model training


## ⚙️ Feature Engineering

To improve model performance and better represent transaction behaviour, several feature engineering techniques were applied.

### Features Created

- Created **Transaction Hour** from the original Time feature to analyse transaction patterns across different hours of the day.
- Created **Log Amount** using logarithmic transformation to reduce skewness in transaction amounts.

### Data Transformation

- Applied **StandardScaler** to standardise numerical features before training the Machine Learning model.

### Why Feature Engineering?

Feature engineering helps Machine Learning models learn meaningful patterns more effectively by improving data quality and reducing the impact of extreme values.


## 🤖 Machine Learning Model

After completing data analysis and feature engineering, a Machine Learning model was developed to classify transactions as **Genuine** or **Fraudulent**.

### Model Used

- **Random Forest Classifier**

### Why Random Forest?

Random Forest was selected because:

- It handles large datasets efficiently.
- It is robust to noise and outliers.
- It reduces overfitting by combining multiple decision trees.
- It provides good performance for classification problems.
- It can model complex relationships between features.

### Model Training

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

The model was trained using the processed dataset and evaluated on unseen test data.

### Evaluation Metrics

The following metrics were used to evaluate model performance:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

These metrics helped assess the model's ability to correctly identify fraudulent transactions while minimising false positives and false negatives.


## 🌐 FastAPI REST API

To make the Machine Learning model usable in a real-world environment, the trained model was deployed using **FastAPI** as a REST API.

The API receives transaction details in JSON format, processes the input, loads the trained Random Forest model, predicts whether the transaction is Genuine or Fraudulent, and returns a business-friendly response.

### API Features

- Real-time Fraud Prediction
- Fraud Probability Score
- Risk Score (%)
- Risk Level Classification
- Business Recommendation
- Transaction ID Generation
- Timestamp Generation
- Health Check Endpoint
- Model Information Endpoint

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API Home |
| `/health` | GET | Health Status |
| `/model-info` | GET | Model Details |
| `/predict` | POST | Predict Fraud Transaction |


## 📤 Sample API Response

```json
{
  "Transaction ID": "TXN-26FFA4AF",
  "Timestamp": "2026-07-27 20:26:28",
  "Prediction": "Genuine",
  "Fraud Probability": 0.00,
  "Risk Score (%)": 0,
  "Risk Level": "Low Risk",
  "Recommendation": "Approve Transaction",
  "Model": "Random Forest",
  "API Version": "1.0"
}
```



## 📁 Project Structure

```text
Credit Card Fraud Detection/
│
├── API/
│   └── main.py
│
├── Model/
│   ├── rf_model.pkl
│   └── scaler.pkl
│
├── data/
│   └── creditcard.csv
│
├── Credit_Card_Fraud_Detection_Project.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```


## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI Server

```bash
cd API
uvicorn main:app --reload
```

### 4. Open Swagger UI


```text
http://127.0.0.1:8000/docs
```

Use the interactive Swagger interface to test the API.


## 🚀 Future Improvements

This project can be further enhanced by:

- Improving fraud detection using advanced Machine Learning algorithms
- Handling class imbalance using techniques such as SMOTE
- Hyperparameter tuning for better model performance
- Deploying the API on a cloud platform (Render, Railway or Azure)
- Building a user-friendly web dashboard for bank employees
- Integrating the API with a real-time transaction monitoring system


