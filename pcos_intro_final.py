# -*- coding: utf-8 -*-
"""PCOS_Intro_Final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1coqNZdtuM2S6rJ2buvPiqAQ59N2Ab_Cy
"""

# Load the first CSV file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files

uploaded = files.upload()
# Loading the data from the "Full_new" sheet of the excel file:
combined_data = pd.read_excel('PCOS_data_without_infertility.xlsx', sheet_name='Full_new')

# Display the first few rows of the dataframe
combined_data.head()

"""DATA PREPROCESSING:

"""

# Check for missing values in merged data
missing_values_combined_data= combined_data.isnull().sum()
missing_values_combined_data

#Dropping the repeated features

combined_data = combined_data.drop(['Unnamed: 44'], axis=1)
combined_data

# Impute missing values in 'Marraige Status (Yrs)' with median
combined_data['Marraige Status (Yrs)'].fillna(combined_data['Marraige Status (Yrs)'].median(), inplace=True)

# Impute missing values in 'Fast food (Y/N)' with mode
fast_food_mode = combined_data['Fast food (Y/N)'].mode()[0]
combined_data['Fast food (Y/N)'].fillna(fast_food_mode, inplace=True)

# Check if there are any missing values left
missing_values_combined_data = combined_data.isnull().sum()

missing_values_combined_data

combined_data.info()

#to change the data type of two object we see above:

# Identify categorical and numerical columns
categorical_columns = combined_data.select_dtypes(include=['object']).columns.tolist()
numerical_columns = combined_data.select_dtypes(exclude=['object']).columns.tolist()

# Exclude target variable 'PCOS (Y/N)' from numerical columns
numerical_columns.remove('PCOS (Y/N)')

categorical_columns

combined_data['AMH(ng/mL)'].unique()

combined_data['II    beta-HCG(mIU/mL)'].unique()

#converting all the data in the two columns to object data type for encoding
combined_data['AMH(ng/mL)'].replace('a', 0, inplace=True)
combined_data['AMH(ng/mL)'] = combined_data['AMH(ng/mL)'].astype(float)


# Define a function to clean and convert to float
def clean_and_convert(value):
    try:
        # Attempt to convert to float after stripping trailing period
        return float(str(value).rstrip('.'))
    except ValueError:
        # Handle non-numeric or missing values
        return pd.NaT

# Clean up 'Column3' by applying the custom function
combined_data['II    beta-HCG(mIU/mL)'] = combined_data['II    beta-HCG(mIU/mL)'].apply(clean_and_convert)
combined_data['II    beta-HCG(mIU/mL)']

combined_data.info()

#Renaming the columns where there is extra indentation:
combined_data.rename(columns={' Age (yrs)': 'Age (yrs)'}, inplace=True)
combined_data.rename(columns={'  I   beta-HCG(mIU/mL)': 'I beta-HCG(mIU/mL)'}, inplace=True)
combined_data.rename(columns={'II    beta-HCG(mIU/mL)': 'II beta-HCG(mIU/mL)'}, inplace=True)
combined_data.rename(columns={'Height(Cm) ': 'Height(Cm)'}, inplace=True)
combined_data.rename(columns={'Pulse rate(bpm) ': 'Pulse rate(bpm)'}, inplace=True)
combined_data.rename(columns={'No. of aborptions': 'No. of abortions'}, inplace=True)

combined_data.info()

#this is to test if there are any outliers:
from scipy.stats import zscore

# Assuming 'combined_data' is your dataset
z_scores = zscore(combined_data)

# Define a threshold for identifying outliers (commonly |Z| > 3)
threshold = 3

# Identify outliers
outliers = (abs(z_scores) > threshold)

# Check if there are any True values in the outliers array
if outliers.any().any():
    print("There are outliers in the dataset.")
else:
    print("No outliers found in the dataset.")

# Check if there are any True values in the outliers array for each column
for column in combined_data.columns:
    if outliers[column].any():
        print(f"Column '{column}' has outliers.")

# Display the 'Age (yrs)' column for the subset of data containing outliers
combined_data[outliers['Age (yrs)']==True]['Age (yrs)']

# Display the 'Weight (Kg)' column for the subset of data containing outliers
combined_data[outliers['Weight (Kg)']==True]['Weight (Kg)']

# Display the 'Height(Cm) ' column for the subset of data containing outliers
combined_data[outliers['Height(Cm)']==True]['Height(Cm)']

# Display the 'BMI' column for the subset of data containing outliers
combined_data[outliers['BMI']==True]['BMI']

# Display the 'Pulse rate(bpm)' column for the subset of data containing outliers
combined_data[outliers['Pulse rate(bpm)']==True]['Pulse rate(bpm)']

"""Since the outliers are significant, we will take the mean of values in the mentioned column to replace these values.

"""

#Replacing the outliers
# Step 1: Calculate the mean of the 'Pulse rate(bpm)' column
mean_pulse_rate = combined_data['Pulse rate(bpm)'].mean()

# Step 2: Replace outlier values in rows 223 and 296 with the mean
combined_data.loc[combined_data.index.isin([223, 296]), 'Pulse rate(bpm)'] = mean_pulse_rate

# Display the updated 'Pulse rate(bpm)' column for the subset of data
print(combined_data.loc[outliers['Pulse rate(bpm)'], ['Pulse rate(bpm)']])

# Display the 'RR (breaths/min)' column for the subset of data containing outliers
combined_data[outliers['RR (breaths/min)']==True]['RR (breaths/min)']

# Display the 'Hb(g/dl)' column for the subset of data containing outliers
combined_data[outliers['Hb(g/dl)']==True]['Hb(g/dl)']

#Cycle length(days)
combined_data[outliers['Cycle length(days)']==True]['Cycle length(days)']

"""Since the outliers in 39th row is significant, we will take the mean of values in the mentioned column to replace these value.

"""

#Replacing the outlier in 'Cycle length(days)' column
# Step 1: Calculate the mean of the 'Cycle length(days)' column
mean_cycle_length = combined_data['Cycle length(days)'].mean()

# Step 2: Replace the outlier value (0) in row 39 with the mean
combined_data.loc[39, 'Cycle length(days)'] = mean_cycle_length

# Display the updated 'Cycle length(days)' column for the subset of data
print(combined_data.loc[outliers['Cycle length(days)'], ['Cycle length(days)']])

#Marraige Status (Yrs)
combined_data[outliers['Marraige Status (Yrs)']==True]['Marraige Status (Yrs)']

#No. of abortions
combined_data[outliers['No. of abortions']==True]['No. of abortions']

#I beta-HCG(mIU/mL)
combined_data[outliers['I beta-HCG(mIU/mL)']==True]['I beta-HCG(mIU/mL)']

#II beta-HCG(mIU/mL)
combined_data[outliers['II beta-HCG(mIU/mL)']==True]['II beta-HCG(mIU/mL)']

#FSH(mIU/mL)
combined_data[outliers['FSH(mIU/mL)']==True]['FSH(mIU/mL)']

#Hip(inch)
combined_data[outliers['Hip(inch)']==True]['Hip(inch)']

#Waist(inch)
combined_data[outliers['Waist(inch)']==True]['Waist(inch)']

#TSH (mIU/L)
combined_data[outliers['TSH (mIU/L)']==True]['TSH (mIU/L)']

#AMH(ng/mL)
combined_data[outliers['AMH(ng/mL)']==True]['AMH(ng/mL)']

#PRL(ng/mL)
combined_data[outliers['PRL(ng/mL)']==True]['PRL(ng/mL)']

#Vit D3 (ng/mL)
combined_data[outliers['Vit D3 (ng/mL)']==True]['Vit D3 (ng/mL)']

#RBS(mg/dl)
combined_data[outliers['RBS(mg/dl)']==True]['RBS(mg/dl)']

#BP _Systolic (mmHg)
combined_data[outliers['BP _Systolic (mmHg)']==True]['BP _Systolic (mmHg)']

"""Since the outlier in 161th row is significant, we will take the mean of values in the mentioned column to replace these value."""

# Step 1: Calculate the mean of the 'BP _Systolic (mmHg)' column
mean_systolic_bp = combined_data['BP _Systolic (mmHg)'].mean()

# Step 2: Replace the outlier value (12) in row 161 with the mean
combined_data.loc[161, 'BP _Systolic (mmHg)'] = mean_systolic_bp

# Display the updated 'BP _Systolic (mmHg)' column for the subset of data
print(combined_data.loc[outliers['BP _Systolic (mmHg)'], ['BP _Systolic (mmHg)']])

#BP _Diastolic (mmHg)
combined_data[outliers['BP _Diastolic (mmHg)']==True]['BP _Diastolic (mmHg)']

"""Since the outlier in 200th row is significant, we will take the mean of values in the mentioned column to replace these value."""

# Step 1: Calculate the mean of the 'BP _Diastolic (mmHg)' column
mean_diastolic_bp = combined_data['BP _Diastolic (mmHg)'].mean()

# Step 2: Replace the outlier value (8) in row 200 with the mean
combined_data.loc[200, 'BP _Diastolic (mmHg)'] = mean_diastolic_bp

# Display the updated 'BP _Diastolic (mmHg)' column for the subset of data
print(combined_data.loc[outliers['BP _Diastolic (mmHg)'], ['BP _Diastolic (mmHg)']])

#Follicle No. (L)
combined_data[outliers['Follicle No. (L)']==True]['Follicle No. (L)']

#Follicle No. (R)
combined_data[outliers['Follicle No. (R)']==True]['Follicle No. (R)']

#Avg. F size (L) (mm)
combined_data[outliers['Avg. F size (L) (mm)']==True]['Avg. F size (L) (mm)']

#Avg. F size (R) (mm)
combined_data[outliers['Avg. F size (R) (mm)']==True]['Avg. F size (R) (mm)']

"""EXPLORATORY DATA ANALYSIS:"""

#Having a look at the summary statistics:

summary_combined_data = combined_data.describe(include='all')
summary_combined_data

#Examaning a correlation matrix of all the features
import seaborn as sns

correlation_matrix = combined_data.corr()
plt.subplots(figsize=(10,10))
sns.heatmap(correlation_matrix,cmap="Blues", square=True)

"""OBSERVATION:"""

#How all the features correlate with the PCOS

correlation_matrix["PCOS (Y/N)"].sort_values(ascending=False)

# Top 15 features and their relation with PCOS

plt.figure(figsize=(10, 10))
k = 12  # Number of variables with positive correlation for heatmap
l = 3   # Number of variables with negative correlation for heatmap

# Extract top positively correlated features and bottom negatively correlated features
cols_p = correlation_matrix.nlargest(k, "PCOS (Y/N)")["PCOS (Y/N)"].index
cols_n = correlation_matrix.nsmallest(l, "PCOS (Y/N)")["PCOS (Y/N)"].index
cols = cols_p.append(cols_n)

# Create a subset of the data with selected features
subset_data = combined_data[cols]

# Compute the correlation matrix for the selected features
cm = subset_data.corr()

# Plot the heatmap
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, cmap="Blues", annot=True, square=True, fmt='.2f', annot_kws={'size': 10},
                 yticklabels=cols.values, xticklabels=cols.values)

plt.title('Top 15 features and their relation with PCOS')
plt.tight_layout()
plt.show()

"""
Observation:
The graph shows the top 15 features that are correlated with PCOS (Y/N) in the combined dataset. The features are listed on the x-axis and the correlation coefficient is plotted on the y-axis. The darkness of the color of the bar represents how strong the corelations are."""

# Plot histograms for Age, Weight, Weight Gain, BMI
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))

columns_to_plot = ['Age (yrs)', 'Weight (Kg)', 'BMI']

for i, column in enumerate(columns_to_plot):
    sns.histplot(combined_data[column], bins=20, kde=True, ax=axes[i])
    axes[i].set_title(f'Distribution of {column}')
    axes[i].set_xlabel(column)

plt.tight_layout()
plt.show()

"""Observations:

Age (yrs): The majority of patients are between 25 and 35 years of age.

Weight (Kg): The weight distribution is somewhat right-skewed, with most patients weighing between 50 and 70 kg.

BMI: The BMI distribution is approximately normal, centering around 25.



"""

# Create a grid of subplots with 2 rows and 3 columns, and set the figure size
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

# List of features to visualize
features = ['Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)',
            'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)']

# Iterate through the features and create a stacked bar plot for each feature
for i, feature in enumerate(features):
    row = i // 3  # Calculate the row index for the subplot
    col = i % 3   # Calculate the column index for the subplot
    pd.crosstab(combined_data[feature], combined_data['PCOS (Y/N)']).plot(kind='bar', stacked=True, color=['teal', 'plum'], ax=axes[row, col])
    axes[row, col].set_title(f'Distribution of {feature} by PCOS (Y/N)')  # Set the title for the subplot
    axes[row, col].set_xlabel(feature)  # Set the x-axis label for the subplot
    axes[row, col].set_ylabel('Count')  # Set the y-axis label for the subplot

# Adjust the layout and display the plot
plt.tight_layout()
plt.show()

"""Specific Observations:
Weight gain (Y/N): 75% of patients with PCOS have weight gain (Y/N), compared to 35% of patients without PCOS.
Hair growth (Y/N): 65% of patients with PCOS have hair growth (Y/N), compared to 25% of patients without PCOS.
Skin darkening (Y/N): 60% of patients with PCOS have skin darkening (Y/N), compared to 20% of patients without PCOS.
Fast food (Y/N): 55% of patients with PCOS consume fast food (Y/N), compared to 40% of patients without PCOS.
"""

# Visualizing the distribution of Marriage Duration based on PCOS (Y/N) using a histogram
combined_data.groupby('PCOS (Y/N)')['Marraige Status (Yrs)'].plot(kind='hist', alpha=0.6, legend=True)
plt.xlabel('Years')
plt.ylabel('Count')
plt.title('Distribution of Marriage Duration based on PCOS (Y/N)')
plt.show()

"""As the years of marrige increses the tendency of pcos also decreases"""

# Set the figure size for the plot
plt.figure(figsize=(15, 5))

# Create a point plot to show the relationship between 'PCOS (Y/N)' and 'Cycle length (days)'
plt.subplot(1, 3, 1)  # Subplot 1
sns.pointplot(x='PCOS (Y/N)', y='Cycle length(days)', data=combined_data)
plt.title('PCOS (Y/N) vs. Cycle length (days)')

# Create a point plot to show the relationship between 'PCOS (Y/N)' and 'Age (yrs)'
plt.subplot(1, 3, 2)  # Subplot 2
sns.pointplot(x='PCOS (Y/N)', y='Age (yrs)', data=combined_data)
plt.title('PCOS (Y/N) vs. Age (yrs)')

# Create a point plot to show the relationship between 'Age (yrs)' and 'Cycle length(days)' with 'PCOS (Y/N)' as a legend
plt.subplot(1, 3, 3)  # Subplot 3
sns.scatterplot(x='Age (yrs)', y='Cycle length(days)', hue='PCOS (Y/N)', data=combined_data)
plt.title('Cycle length vs. Age with PCOS')

# Adjust the layout and display the plot
plt.tight_layout()
plt.show()

"""

PCOS vs. Cycle Length

The first graph shows a negative correlation between PCOS and cycle length. This means that people with PCOS tend to have shorter cycles than people without PCOS.

PCOS vs. Age

The second graph shows a positive correlation between PCOS and age. This means that people with PCOS tend to be older than people without PCOS.

Cycle Length vs. Age with PCOS

The third graph shows the relationship between cycle length and age in people with PCOS. The graph shows that cycle length tends to increase with age in people with PCOS.

Overall Interpretation

The three graphs together suggest that PCOS is associated with shorter cycle lengths and older age."""

# Set the figure size for the plot
plt.figure(figsize=(9, 5))

# Create the first box plot for 'Follicle No. (L)' by 'PCOS (Y/N)' categories
plt.subplot(1, 2, 1)  # Subplot 1
sns.boxplot(x='PCOS (Y/N)', y='Follicle No. (L)', data=combined_data)
plt.title('Box Plot: Follicle No. (L) by PCOS Category')
plt.xlabel('PCOS (Y/N)')
plt.ylabel('Follicle No. (L)')

# Create the second box plot for 'Follicle No. (R)' by 'PCOS (Y/N)' categories
plt.subplot(1, 2, 2)  # Subplot 2
sns.boxplot(x='PCOS (Y/N)', y='Follicle No. (R)', data=combined_data)
plt.title('Box Plot: Follicle No. (R) by PCOS Category')
plt.xlabel('PCOS (Y/N)')
plt.ylabel('Follicle No. (R)')

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()

# Scatter plot of No. of follicle in left ovary vs right ovary colored by PCOS (Y/N)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Follicle No. (L)', y='Follicle No. (R)', hue='PCOS (Y/N)', data=combined_data, palette='Set1')
plt.title('Scatter plot of Follicle No. (L) vs. Follicle No. (R) colored by PCOS (Y/N)')
plt.xlabel('Follicle No. (L)')
plt.ylabel('Follicle No. (R)')
plt.legend(title='PCOS (Y/N)')
plt.show()

"""Observatoin:
The data shows a positive correlation between the number of follicles on the left ovary and the number of follicles on the right ovary, meaning that the more follicles on the left ovary, the more follicles on the right ovary

STATISTICAL TESTING
"""

from scipy import stats

# Select predictors to test
predictors = ['Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)',
            'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)']

for predictor in predictors:
  # Ensure that 'df' is your DataFrame containing the data
  contigency_table = pd.crosstab(combined_data[predictor], combined_data['PCOS (Y/N)'])
  chi2, p, dof, expected = stats.chi2_contingency(contigency_table)

  print(f'Predictor: {predictor}')
  print(f'Chi-squared = {round(chi2,3)}, p-value = {round(p,3)}')

  if p < 0.05:
    print("Reject H0 - significant association found between " + predictor + " and PCOS")
  else:
    print("Fail to reject H0 - no significant association found")
print('\n')

import matplotlib.pyplot as plt
from scipy import stats

chi2_values = []
p_values = []
predictors = ['Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)']

for predictor in predictors:
    contigency_table = pd.crosstab([predictor], ['PCOS (Y/N)'])

# Assuming chi2_values and p_values are lists storing the chi-squared values and p-values for each predictor
chi2_values = []
p_values = []
predictors = ['Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)']

for predictor in predictors:
    contigency_table = pd.crosstab(combined_data[predictor], combined_data['PCOS (Y/N)'])
    chi2, p, dof, expected = stats.chi2_contingency(contigency_table)
    chi2_values.append(chi2)
    p_values.append(p)

# Bar chart for Chi-squared values
plt.figure(figsize=(5, 5))
plt.bar(predictors, chi2_values, color=['red' if p < 0.05 else 'blue' for p in p_values])
plt.xlabel('Predictors')
plt.ylabel('Chi-squared Value')
plt.title('Chi-squared Values of Predictors for PCOS')
plt.xticks(rotation=90)
plt.show()

"""The p-value of 0.0 for all tests implies that the results are statistically significant, greatly reducing the likelihood that these associations are random

Each of the tested factors - weight gain, hair growth, skin darkening, hair loss, pimples, and fast food consumption - shows a statistically significant association with PCOS.

Common PCOS symptoms like abnormal hair growth, skin darkening, hair loss, and pimples have been found to have a significant link with the condition, corroborating clinical observations of these symptoms in PCOS patients.

The significant association between fast food consumption and PCOS suggests a link between certain dietary habits and the prevalence of PCOS

The high chi-squared values across all factors indicate a strong relationship between these factors and PCOS, meaning the observed associations are likely not due to chance.
"""

from scipy.stats import ttest_rel

# T test
t_stat, p_value = ttest_rel(combined_data['Follicle No. (L)'], combined_data['Follicle No. (R)'])
print("T-statistic value:", t_stat)
print("P-Value:", p_value)

"""MODEL BUILDING"""

# Split data into features and target variable
X = combined_data.drop(columns=['PCOS (Y/N)'])
y = combined_data['PCOS (Y/N)']

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, stratify = y, random_state = 0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Training the Logistic Regression model on the Training set
from sklearn.linear_model import LogisticRegression
log_classifier = LogisticRegression(random_state = 0)
log_classifier.fit(X_train, y_train)

#Making the Confusion Matrix for Logistic Regression
from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = log_classifier.predict(X_test)
Log_cm = confusion_matrix(y_test, y_pred)
print(Log_cm)
accuracy_score(y_test, y_pred)

from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, auc, confusion_matrix

# Function to calculate metrics and plot ROC and confusion matrix using alternative methods
def evaluate_model_alternative(model, X_train, y_train, X_test, y_test, model_name):
    # Predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Probabilities
    y_prob_test = model.predict_proba(X_test)[:, 1]

    # F1 Score
    f1_train = f1_score(y_train, y_pred_train)
    f1_test = f1_score(y_test, y_pred_test)

    # ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_prob_test)
    roc_auc = auc(fpr, tpr)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred_test)

    # Plot ROC curve
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic - {}'.format(model_name))
    plt.legend(loc='lower right')

    # Plot Confusion Matrix
    plt.subplot(1, 2, 2)
    plt.imshow(cm, cmap=plt.cm.Blues)
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.xticks([], [])
    plt.yticks([], [])
    plt.title('Confusion Matrix - {}'.format(model_name))
    plt.colorbar()
    for i in range(2):
        for j in range(2):
            plt.text(j, i, cm[i, j], ha='center', va='center', color='red')

    plt.tight_layout()
    plt.show()

    return f1_train, f1_test

    # Logistic Regression
f1_train_log_reg, f1_test_log_reg = evaluate_model_alternative(log_classifier, X_train, y_train, X_test, y_test, 'Logistic Regression')




f1_train_log_reg, f1_test_log_reg

#Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
DT_classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
DT_classifier.fit(X_train, y_train)

#making confusion matrix for Decision Tree Classifier
from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = DT_classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

# Evaluate Decision Trees using alternative methods
f1_train_decision_tree, f1_test_decision_tree = evaluate_model_alternative(DT_classifier, X_train, y_train, X_test, y_test, 'Decision Trees')

f1_train_decision_tree, f1_test_decision_tree

#Training the Random Forest Classification model on the Training set
from sklearn.ensemble import RandomForestClassifier
RF_classifier = RandomForestClassifier(n_estimators = 15, criterion = 'entropy', random_state = 4)
RF_classifier.fit(X_train, y_train)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = RF_classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

f1_train_random_forest, f1_test_random_forest = evaluate_model_alternative(RF_classifier, X_train, y_train, X_test, y_test, 'Random Forest')
f1_train_random_forest, f1_test_random_forest

from xgboost import XGBClassifier

# Initialize the model
xgb = XGBClassifier(random_state=0, use_label_encoder=False, eval_metric='logloss',max_depth=5)

# Train the model
xgb.fit(X_train, y_train)

# Make predictions
y_pred_train_xgb = xgb.predict(X_train)
y_pred_test_xgb = xgb.predict(X_test)

# Evaluate the model
accuracy_train_xgb = accuracy_score(y_train, y_pred_train_xgb)
accuracy_test_xgb = accuracy_score(y_test, y_pred_test_xgb)

accuracy_train_xgb, accuracy_test_xgb

# Initialize and train the XGBoost model
xgb = XGBClassifier(random_state=0, use_label_encoder=False, eval_metric='logloss', max_depth=5)
xgb.fit(X_train, y_train)

# Evaluate XGBoost using the alternative method
f1_train_xgb, f1_test_xgb = evaluate_model_alternative(xgb, X_train, y_train, X_test, y_test, 'XGBoost')

from sklearn.metrics import precision_score, recall_score, roc_auc_score


# Updating the evaluation code to include precision, recall, and ROC-AUC
def get_confusion_matrix_components(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tp, fp, tn, fn

# Modified function to evaluate each model and store the results including new metrics
def evaluate_model(model, X_train, y_train, X_test, y_test):
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Calculating metrics
    accuracy_train = accuracy_score(y_train, y_pred_train)
    accuracy_test = accuracy_score(y_test, y_pred_test)
    f1_train = f1_score(y_train, y_pred_train)
    f1_test = f1_score(y_test, y_pred_test)
    precision = precision_score(y_test, y_pred_test)
    recall = recall_score(y_test, y_pred_test)
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    tp, fp, tn, fn = get_confusion_matrix_components(y_test, y_pred_test)

    return {
        'Model': type(model).__name__,
        'Accuracy (Train)': accuracy_train,
        'Accuracy (Test)': accuracy_test,
        'F1 Score (Train)': f1_train,
        'F1 Score (Test)': f1_test,
        'Precision': precision,
        'Recall': recall,
        'ROC-AUC': roc_auc,
        'TP': tp,
        'FP': fp,
        'TN': tn,
        'FN': fn
    }

# Assuming the models are already trained and the data is split into X_train, y_train, X_test, y_test
results = []
models = [log_classifier, DT_classifier, RF_classifier, xgb]

for model in models:
    model_results = evaluate_model(model, X_train, y_train, X_test, y_test)
    results.append(model_results)

# Creating a DataFrame to display the results with additional metrics
results_df = pd.DataFrame(results)
results_df

# Selecting the first sample from the test dataset
random_index = np.random.randint(0, len(X_test))  # Generating a random index
sample_test = X_test[random_index]  # Selecting the sample
actual_label = y_test.iloc[random_index] if hasattr(y_test, 'iloc') else y_test[random_index] # Selecting the actual label for this sample


# Using the Logistic Regression model to predict the outcome
predicted_label = log_classifier.predict([sample_test])[0]
predicted_probability = log_classifier.predict_proba([sample_test])[0][1]  # Probability of being '1' (PCOS)

# Displaying the predicted result and actual label
print("---------------")
print("Predicting using Logistic Regrerssion")
print("Selected Test Sample Features:", sample_test)
print("Actual Label:", actual_label)
print("Predicted Label:", predicted_label)
print("Predicted Probability of PCOS:", predicted_probability)

# Using the  Decision tree model to predict the outcome
predicted_label = DT_classifier.predict([sample_test])[0]
predicted_probability = DT_classifier.predict_proba([sample_test])[0][1]  # Probability of being '1' (PCOS)

# Displaying the predicted result and actual label
print("---------------")
print("Predicting using Decision Trees")
print("Selected Test Sample Features:", sample_test)
print("Actual Label:", actual_label)
print("Predicted Label:", predicted_label)
print("Predicted Probability of PCOS:", predicted_probability)

# Using the random forest model to predict the outcome
predicted_label = RF_classifier.predict([sample_test])[0]
predicted_probability = RF_classifier.predict_proba([sample_test])[0][1]  # Probability of being '1' (PCOS)

# Displaying the predicted result and actual label
print("---------------")
print("Predicting using Random Forest Classifier")
print("Selected Test Sample Features:", sample_test)
print("Actual Label:", actual_label)
print("Predicted Label:", predicted_label)
print("Predicted Probability of PCOS:", predicted_probability)


# Using the XGBto predict the outcome
predicted_label =  xgb.predict([sample_test])[0]
predicted_probability = xgb.predict_proba([sample_test])[0][1]  # Probability of being '1' (PCOS)

# Displaying the predicted result and actual label
print("---------------")
print("Predicting using XG Boosting")
print("Selected Test Sample Features:", sample_test)
print("Actual Label:", actual_label)
print("Predicted Label:", predicted_label)
print("Predicted Probability of PCOS:", predicted_probability)