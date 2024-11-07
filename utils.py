import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    """
    Preprocesses the data before feeding it into the ML model.
    This could involve scaling features, encoding categorical variables, etc.
    """
    # Example: Let's assume 'data' is a dictionary containing raw data for CPU, memory, etc.
    # If it's a more complex structure (like a DataFrame), preprocessing steps may vary.
    
    # Feature scaling: Assuming numerical data (e.g., CPU usage, memory usage)
    scaler = StandardScaler()
    features = ['cpu_usage', 'memory_usage']
    data[features] = scaler.fit_transform(data[features])

    return data
