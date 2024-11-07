import time
from hids import run_hids
from nids import run_nids
from ml_models import load_model, predict_malware
from utils import preprocess_data
import joblib

def main():
    # Load pre-trained ML models (Random Forest and SVM)
    rf_model = load_model('models/random_forest_model.pkl')
    svm_model = load_model('models/svm_model.pkl')

    while True:
        print("Starting malware detection...")

        # Step 1: Run Host-based Intrusion Detection System (HIDS)
        hids_data = run_hids()  # Get data from HIDS
        processed_hids_data = preprocess_data(hids_data)  # Preprocess HIDS data
        
        # Step 2: If HIDS flags something suspicious, process the data with ML model
        if processed_hids_data['flagged']:
            result = predict_malware(processed_hids_data, rf_model)
            print(f"HIDS Detected: {result}")

        # Step 3: Run Network Intrusion Detection System (NIDS) as backup
        nids_data = run_nids()  # Get network traffic data
        processed_nids_data = preprocess_data(nids_data)  # Preprocess NIDS data
        
        # Step 4: If NIDS flags something suspicious, process the data with ML model
        if processed_nids_data['flagged']:
            result = predict_malware(processed_nids_data, svm_model)
            print(f"NIDS Detected: {result}")
        
        # Wait for the next cycle (1 hour as per initial setup)
        time.sleep(3600)  # 3600 seconds = 1 hour

if __name__ == "__main__":
    main()
