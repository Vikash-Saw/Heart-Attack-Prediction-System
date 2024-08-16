import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load the dataset
heart_data = pd.read_csv('heart.csv')

# checking for missing values
heart_data.isnull().sum()

# statistical measures about the data
heart_data.describe()

# checking the distribution of Target Variable
heart_data['target'].value_counts()

# Split the data into features and target variable
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# Split the data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Create a pipeline that includes scaling and logistic regression with increased max_iter
pipeline = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))

# Fit the model on the training data
pipeline.fit(X_train, Y_train)

# Predictions on training data
X_train_prediction = pipeline.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# Predictions on test data
X_test_prediction = pipeline.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# # Output the accuracy
# print('Accuracy on Training data:', training_data_accuracy)
# print('Accuracy on Test data:', test_data_accuracy)
