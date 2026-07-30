💰 Income Prediction using Machine Learning

📌 Project Overview

This project focuses on predicting whether an individual’s annual income exceeds $50K based on demographic, educational, and work-related attributes. The objective is to analyze the factors that influence income levels and build a machine learning model capable of making accurate predictions.

The project covers the complete machine learning workflow, including data exploration, preprocessing, feature engineering, model building, and evaluation.

⸻

🎯 Problem Statement

Identify the socioeconomic and occupational factors that influence an individual’s likelihood of earning more than $50K per year. The insights from this analysis can help support data-driven business strategies, policymaking, and targeted interventions.

⸻

📊 Business Requirements

* Analyze income distribution across different demographic groups such as gender, race, and education.
* Identify occupations with a higher probability of earning more than $50K annually.
* Study the relationship between working hours per week and annual income.
* Evaluate the impact of capital gains and capital losses on income classification.

⸻

📂 Dataset

The dataset contains demographic, educational, occupational, and financial information about individuals. It includes features such as:

* Age
* Workclass
* Education
* Marital Status
* Occupation
* Relationship
* Race
* Gender
* Capital Gain
* Capital Loss
* Hours per Week
* Native Country
* Income (Target Variable)

Target Variable:

* <=50K
* >50K

⸻

🔍 Exploratory Data Analysis (EDA)

During the exploratory data analysis phase, the dataset was examined to understand its structure, identify missing values, and explore relationships between different variables.

The following analyses were performed:

* Dataset overview and statistical summary
* Missing value identification
* Distribution analysis of numerical features
* Categorical feature analysis
* Income distribution visualization
* Outlier detection using Box Plots
* Count plots for demographic comparison
* Correlation analysis between numerical variables

⸻

⚙️ Data Preprocessing

Several preprocessing techniques were applied to prepare the data for machine learning.

Data Cleaning

* Handled missing values
* Removed unnecessary columns (if applicable)
* Checked for duplicate records

Feature Engineering

* One-Hot Encoding for categorical variables
* Label Encoding where required

Data Transformation

* Converted categorical features into numerical format
* Prepared features and target variable
* Split the dataset into training and testing sets

⸻

🤖 Machine Learning Model

The processed dataset was used to train a classification model capable of predicting whether an individual’s annual income is above or below $50K.

The model was evaluated using standard classification metrics to measure prediction performance.

⸻

📈 Project Workflow

1. Load Dataset
2. Data Exploration
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Data Preprocessing
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Income Prediction

⸻

📚 Python Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib

⸻

📊 Key Insights

* Education plays a significant role in determining income levels.
* Certain occupations have a much higher probability of earning above $50K.
* Individuals working more hours per week generally have a greater chance of higher income.
* Capital gains show a positive relationship with higher income categories.
* Income distribution varies across demographic groups such as gender and race.

⸻

✅ Conclusion

This project demonstrates how machine learning can be applied to predict income levels using demographic and occupational information.

The analysis revealed that education, occupation, working hours, and capital gains are among the most influential factors affecting income prediction. Although the model achieved promising results, there is still room for improvement by experimenting with advanced algorithms, feature engineering techniques, and hyperparameter tuning.

Overall, this project provides valuable insights into income prediction while showcasing an end-to-end machine learning workflow, from data preprocessing to model evaluation.

⸻

🚀 Future Improvements

* Hyperparameter tuning
* Feature selection techniques
* Advanced ensemble models
* Cross-validation
* Model deployment using Flask/FastAPI
* Interactive dashboard using Streamlit

⸻

👨‍💻 Author

Sumit Darji

Machine Learning | Data Science | Python Developer