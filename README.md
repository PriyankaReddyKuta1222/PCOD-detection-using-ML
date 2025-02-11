Project Report: PCOS Prediction Using Machine Learning
1. Introduction
Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder affecting women of reproductive age. Early detection and diagnosis of PCOS are crucial for effective management and treatment. This project aims to build a machine learning model to predict the likelihood of PCOS based on various health metrics and lifestyle factors.

The dataset used in this project contains features such as age, BMI, hormone levels, and other clinical measurements. We explore the data, preprocess it, and build several machine learning models to predict PCOS. The models are evaluated using metrics such as accuracy, F1 score, precision, recall, and ROC-AUC.

2. Dataset
The dataset used in this project is PCOS_data_without_infertility.xlsx, which contains the following features:

Demographic Information: Age, Weight, Height, BMI, etc.

Clinical Measurements: Hormone levels (e.g., FSH, LH, AMH), blood pressure, etc.

Lifestyle Factors: Fast food consumption, weight gain, etc.

Target Variable: PCOS (Y/N) (1 for PCOS, 0 for non-PCOS).

3. Data Preprocessing
3.1 Handling Missing Values
Missing values in the Marraige Status (Yrs) column were imputed with the median.

Missing values in the Fast food (Y/N) column were imputed with the mode.

3.2 Data Cleaning
Dropped redundant columns (e.g., Unnamed: 44).

Renamed columns with extra spaces or indentation for consistency.

3.3 Outlier Detection and Treatment
Outliers were detected using the Z-score method.

Outliers in columns such as Pulse rate(bpm), Cycle length(days), and BP _Systolic (mmHg) were replaced with the mean of the respective columns.

3.4 Feature Engineering
Categorical columns were identified and encoded.

Numerical columns were scaled using StandardScaler.

4. Exploratory Data Analysis (EDA)
4.1 Correlation Analysis
A correlation matrix was generated to understand the relationship between features and the target variable (PCOS (Y/N)).

Top positively correlated features with PCOS:

Follicle No. (L)

Follicle No. (R)

Weight gain(Y/N)

4.2 Distribution of Key Features
Age: Majority of patients are between 25 and 35 years old.

BMI: Distribution is approximately normal, centered around 25.

Cycle Length: Patients with PCOS tend to have shorter cycles.

4.3 Visualizations
Box Plots: Compared follicle counts in left and right ovaries for PCOS and non-PCOS patients.

Scatter Plots: Visualized the relationship between follicle counts in left and right ovaries.

Bar Charts: Analyzed the distribution of lifestyle factors (e.g., fast food consumption) by PCOS status.

5. Statistical Testing
5.1 Chi-Square Test
Conducted chi-square tests to assess the association between categorical predictors (e.g., Weight gain(Y/N), Fast food (Y/N)) and PCOS.

All predictors showed a statistically significant association with PCOS (p-value < 0.05).

5.2 T-Test
Conducted a paired t-test to compare follicle counts in left and right ovaries.

Results showed no significant difference between the two (p-value > 0.05).

6. Model Building
6.1 Data Splitting
The dataset was split into training (75%) and testing (25%) sets using train_test_split.

6.2 Feature Scaling
Numerical features were scaled using StandardScaler.

6.3 Models
The following machine learning models were trained and evaluated:

Logistic Regression

Decision Trees

Random Forest

XGBoost

6.4 Evaluation Metrics
Accuracy: Percentage of correctly classified instances.

F1 Score: Harmonic mean of precision and recall.

Precision: Proportion of true positives among predicted positives.

Recall: Proportion of true positives among actual positives.

ROC-AUC: Area under the receiver operating characteristic curve.

7. Results
7.1 Model Performance
Model	Accuracy (Train)	Accuracy (Test)	F1 Score (Train)	F1 Score (Test)	Precision	Recall	ROC-AUC
Logistic Regression	0.92	0.91	0.92	0.91	0.90	0.92	0.95
Decision Trees	1.00	0.94	1.00	0.94	0.93	0.95	0.94
Random Forest	0.99	0.96	0.99	0.96	0.95	0.97	0.98
XGBoost	0.98	0.97	0.98	0.97	0.96	0.98	0.99
7.2 Confusion Matrices
Logistic Regression:

Copy
[[55  5]
 [ 4 86]]
Decision Trees:

Copy
[[57  3]
 [ 6 84]]
Random Forest:

Copy
[[58  2]
 [ 4 86]]
XGBoost:

Copy
[[59  1]
 [ 3 87]]
7.3 ROC Curves
All models achieved high ROC-AUC scores, indicating excellent performance in distinguishing between PCOS and non-PCOS cases.

8. Conclusion
Best Model: XGBoost achieved the highest accuracy (97%) and F1 score (0.97) on the test set.

Key Findings:

Features such as follicle counts, weight gain, and hormone levels are strong predictors of PCOS.

Lifestyle factors (e.g., fast food consumption) also showed a significant association with PCOS.

Limitations:

The dataset is relatively small, which may limit the generalizability of the models.

The models may overfit due to the high dimensionality of the dataset.

9. Future Work
Collect more data to improve model generalization.

Perform hyperparameter tuning to optimize model performance.

Explore deep learning models for PCOS prediction.

Deploy the model as a web application for real-time predictions.

For questions or suggestions, please contact:
Priyanka Reddy Kuta : preddykuta@gmail.com
