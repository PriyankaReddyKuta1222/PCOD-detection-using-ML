# PCOD-detection-using-ML
This project utilizes machine learning to predict the likelihood of Polycystic Ovary Syndrome (PCOS) in women. By analyzing health data, such as BMI, hormone levels, and menstrual cycle patterns, we aim to assist in early diagnosis and improve clinical decision-making. 
PCOS Prediction Using Machine Learning
Table of Contents
Introduction
Dataset
Features
Technologies Used
Project Workflow
How to Run the Project
Results and Insights
Contributing
License
Introduction
Polycystic Ovary Syndrome (PCOS) is a common endocrine disorder affecting women of reproductive age. This project aims to predict the likelihood of PCOS using machine learning models and healthcare data. The goal is to provide early diagnosis assistance and better clinical decision-making through data-driven insights.

Dataset
The dataset used in this project consists of healthcare information related to PCOS, including:

Features: Patient demographics, BMI, menstrual irregularities, hormonal levels, and more.
Size: 1000+ records of patient data.
The dataset was either sourced from publicly available medical data or simulated to ensure project replicability.

Features
Key attributes of the dataset include:

BMI: Body Mass Index
Insulin levels: Fasting and postprandial insulin
LH/FSH ratio: Hormonal imbalance indicator
Menstrual cycle patterns
Patient age and glucose levels
Technologies Used
This project was implemented using the following technologies and tools:

Programming Languages: Python
Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
Visualization Tools: Power BI
Machine Learning Models: Logistic Regression, Random Forest, SVM
Project Workflow
Data Preprocessing

Handled missing values and outliers.
Performed data normalization and feature encoding.
Exploratory Data Analysis (EDA)

Analyzed trends and patterns in PCOS-related features.
Created visualizations to highlight key insights.
Feature Engineering

Extracted and engineered relevant features for the prediction task.
Model Development

Trained Logistic Regression, Random Forest, and SVM models.
Achieved an accuracy of 87% using Random Forest.
Evaluation

Evaluated models using performance metrics such as accuracy, precision, recall, and F1-score.
Visualization

Created Power BI dashboards for better data visualization and decision-making.
How to Run the Project
Prerequisites:
Python 3.x installed on your system
Required libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
Steps:
Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/pcos-prediction.git
Navigate to the project directory:
bash
Copy
Edit
cd pcos-prediction
Install required dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Run the Jupyter Notebook or Python script:
bash
Copy
Edit
jupyter notebook PCOS_Intro_Final.ipynb
Power BI Visualization:
Open the Power BI dashboard file included in the repository.
Ensure the dataset is loaded correctly to view insights.
Results and Insights
Accuracy: The Random Forest model achieved an accuracy of 87%.
Key Insights:
Higher LH/FSH ratios were strongly correlated with PCOS diagnosis.
Irregular menstrual cycles were a common predictor of PCOS.
These findings can aid clinicians and researchers in identifying patients at risk of PCOS and recommending timely interventions.

Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request.

License
This project is not licensed.
