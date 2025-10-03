import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Get the absolute path of the project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build path to CSV file
data_path = os.path.join(PROJECT_ROOT, 'data', 'build_jobs.csv')

# Load historical build data
data = pd.read_csv(data_path)

# Features and target
X = data[['priority', 'complexity']]
y = data['estimated_time']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
model_path = os.path.join(PROJECT_ROOT, 'models', 'job_predictor.pkl')
joblib.dump(model, model_path)

print("Model trained and saved successfully!")
