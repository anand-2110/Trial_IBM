import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score

def load_model(model_path):
    """
    Loads a pre-trained ML model from a file.
    """
    return joblib.load(model_path)

def predict_malware(data, model):
    """
    Predicts whether the given data represents malware or benign activity.
    Assumes the model is already trained.
    """
    # Example: data should be preprocessed into a format suitable for ML
    features = [data['cpu_usage'], data['memory_usage']]  # For simplicity, we use CPU and memory as features
    prediction = model.predict([features])
    return "Malware Detected" if prediction == 1 else "Benign"

def train_model(X_train, y_train):
    """
    Trains an SVM and Random Forest model and saves it.
    """
    # SVM model
    svm_model = SVC(kernel='linear')
    svm_model.fit(X_train, y_train)

    # Random Forest model
    rf_model = RandomForestClassifier(n_estimators=100)
    rf_model.fit(X_train, y_train)

    # Save models
    joblib.dump(svm_model, 'models/svm_model.pkl')
    joblib.dump(rf_model, 'models/random_forest_model.pkl')

    # Return trained models
    return svm_model, rf_model
