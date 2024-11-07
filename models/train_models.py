import joblib

# Load the Random Forest model
rf_model = joblib.load('features.pkl')

# Load the SVM model
svm_model = joblib.load('svm_model.pkl')

# Example input data for prediction (replace with actual data)
sample_input = [[0.5, 1.2, -0.8, 0.1, 0.3, ...]]  # Example feature values

# Predict using the Random Forest model
rf_prediction = rf_model.predict(sample_input)
print(f"Random Forest Prediction: {rf_prediction}")

# Predict using the SVM model
svm_prediction = svm_model.predict(sample_input)
print(f"SVM Prediction: {svm_prediction}")
