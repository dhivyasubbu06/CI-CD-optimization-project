import pandas as pd
import joblib
import os

# Get absolute path of project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build path to model
model_path = os.path.join(PROJECT_ROOT, 'models', 'job_predictor.pkl')

# Load the trained model
model = joblib.load(model_path)

# Build path to new job data (optional)
# Example new jobs to schedule
new_jobs = pd.DataFrame({
    'job_id': [6, 7, 8],
    'priority': [2, 1, 3],
    'complexity': [4, 2, 5]
})

# Predict build time
new_jobs['predicted_time'] = model.predict(new_jobs[['priority', 'complexity']])

# Optimize queue using Shortest Job First (SJF)
optimized_queue = new_jobs.sort_values(by='predicted_time')

print("Optimized Build Queue:")
print(optimized_queue[['job_id', 'priority', 'complexity', 'predicted_time']])
