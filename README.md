# 💰 Income Prediction using Machine Learning

An end-to-end Machine Learning project that predicts whether an individual's annual income exceeds **$50K** based on demographic, educational, and occupational attributes. The project includes data analysis, preprocessing, model training, evaluation, and an interactive **Streamlit web application** for real-time income prediction.

---

# 📌 Project Overview

This project aims to predict whether an individual's annual income is greater than **$50K** using demographic and work-related information. It demonstrates the complete Machine Learning workflow, including Exploratory Data Analysis (EDA), data preprocessing, feature engineering, model training, evaluation, and deployment through a Streamlit web application.

The Streamlit application allows users to enter their own information and instantly receive income predictions using the trained Machine Learning model.

---

# 🎯 Problem Statement

Develop a Machine Learning model that accurately predicts whether an individual's annual income exceeds **$50K**. The project also identifies the key socioeconomic and occupational factors influencing income to support better business decisions and data-driven insights.

---

# 📊 Business Requirements

- Analyze income distribution across different demographic groups such as gender, race, and education.
- Identify occupations with a higher probability of earning more than **$50K** annually.
- Study the relationship between weekly working hours and annual income.
- Analyze the impact of capital gains and capital losses on income prediction.

---

# 📂 Dataset Information

The project uses the **Adult Census Income Dataset**, which contains demographic and employment-related information.

### Features

- Age
- Workclass
- Education
- Marital Status
- Occupation
- Relationship
- Race
- Gender
- Capital Gain
- Capital Loss
- Hours per Week
- Native Country

### Target Variable

- <=50K
- >50K

---

# 🔍 Exploratory Data Analysis (EDA)

Several exploratory analyses were performed to better understand the dataset.

### EDA Includes

- Dataset Overview
- Statistical Summary
- Missing Value Analysis
- Duplicate Record Detection
- Outlier Detection
- Income Distribution
- Gender-wise Income Analysis
- Education-wise Income Analysis
- Occupation Analysis
- Correlation Analysis
- Feature Visualization using Charts

---

# ⚙️ Data Preprocessing

The following preprocessing techniques were applied before training the Machine Learning model.

- Handling Missing Values
- Removing Duplicate Records
- Feature Selection
- One-Hot Encoding
- Label Encoding
- Feature Scaling
- Train-Test Split

---

# 🤖 Machine Learning Model

A supervised Machine Learning classification model was trained to predict whether an individual's annual income is above or below **$50K**.

After training, the model was saved using **Joblib** and integrated into a **Streamlit Web Application**, allowing users to make predictions using new input data without retraining the model.

---

# 🌐 Streamlit Web Application

The project includes a user-friendly Streamlit application that allows users to:

- Enter demographic information
- Enter work-related information
- Predict annual income instantly
- Get real-time prediction results

---

# 📈 Project Workflow

```text
Dataset
   │
   ▼
Data Collection
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis (EDA)
   │
   ▼
Feature Engineering
   │
   ▼
Data Preprocessing
   │
   ▼
Train-Test Split
   │
   ▼
Machine Learning Model
   │
   ▼
Model Evaluation
   │
   ▼
Model Saving (Joblib)
   │
   ▼
Streamlit Web Application
   │
   ▼
Real-Time Income Prediction
```

---

# 🛠️ Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

# 📁 Project Structure

```text
Income_Prediction_with_EDA/
│── Income_Prediction_with_EDA_3.ipynb
│── income_prediction_form_ui.py
│── income_prediction_info.py
│── requirements.txt
│── README.md
│── Project-report-Documentation.pdf
│── Dataset Information & Visualization.pdf
│── Data Visualization.pdf
```

---

# 🚀 Installation

```bash
git clone https://github.com/sumit170704/Income_Prediction_with_EDA.git

cd Income_Prediction_with_EDA

pip install -r requirements.txt
```

---

# ▶️ Run the Project

### Run Jupyter Notebook

```bash
jupyter notebook
```

### Run Streamlit Application

```bash
streamlit run income_prediction_form_ui.py
```

---

# 📊 Key Insights

- Education significantly influences annual income.
- Occupation is one of the strongest indicators of higher earnings.
- Individuals working more hours per week generally have a greater chance of earning above **$50K**.
- Capital gains positively influence income prediction.
- Demographic factors such as education, occupation, gender, and working hours contribute significantly to income classification.

---

# 📈 Results

- Successfully built an end-to-end Machine Learning pipeline.
- Performed comprehensive Exploratory Data Analysis (EDA).
- Built an accurate income classification model.
- Developed an interactive Streamlit web application for real-time predictions.
- Created a reusable prediction system using Joblib.

---

# 🚀 Future Improvements

- Hyperparameter Tuning
- Feature Selection Techniques
- Advanced Ensemble Models
- Deep Learning Approaches
- Cloud Deployment
- REST API using Flask/FastAPI
- Docker Integration
- CI/CD Pipeline
- User Authentication
- Database Integration

---

# 👨‍💻 Author

## Sumit Darji

**Machine Learning | Data Science | Python Developer**

📧 Email: sumitdarji1707@gmail.com

🔗 GitHub: https://github.com/sumit170704

---

⭐ If you found this project useful, don't forget to **Star** this repository.
