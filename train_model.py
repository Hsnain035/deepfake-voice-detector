from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

# Create random training data
X = np.random.rand(100, 40)
y = np.random.randint(0, 2, 100)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "saved_model/model.pkl")

print("Model saved successfully!")