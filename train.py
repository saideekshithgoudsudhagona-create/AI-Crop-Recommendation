import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# ----------------------------
# Load Dataset
# ----------------------------
dataset_path = "dataset/crop_data.csv"

print("=" * 50)
print("Loading Dataset...")
print("=" * 50)

if not os.path.exists(dataset_path):
    print("Dataset not found!")
    exit()

df = pd.read_csv(dataset_path)

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# ----------------------------
# Remove Missing Values
# ----------------------------
df = df.dropna()

# ----------------------------
# Clean Text Columns
# ----------------------------
text_columns = [
    "State_Name",
    "District_Name",
    "Season",
    "Crop"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# Convert District names to uppercase
df["District_Name"] = df["District_Name"].str.upper()

# ----------------------------
# Encode Categorical Columns
# ----------------------------
encoders = {}

categorical_columns = [
    "State_Name",
    "District_Name",
    "Season",
    "Crop"
]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# ----------------------------
# Features & Target
# ----------------------------
X = df.drop("Production", axis=1)
y = df["Production"]

# ----------------------------
# Train Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ----------------------------
# Machine Learning Models
# ----------------------------
models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    # "Random Forest": RandomForestRegressor(
    #     n_estimators=50,
    #     max_depth=15,
    #     random_state=42,
    #     n_jobs=-1
    # )
    "Random Forest": RandomForestRegressor(
    n_estimators=20,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)
}
    # "Random Forest": RandomForestRegressor(
    #     n_estimators=200,
    #     random_state=42
    # )


best_model = None
best_score = -999

print("\nTraining Models...\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    r2 = r2_score(y_test, prediction)
    mae = mean_absolute_error(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    rmse = mse ** 0.5

    print("=" * 50)
    print(name)
    print("=" * 50)
    print(f"R2 Score : {r2:.4f}")
    print(f"MAE      : {mae:.4f}")
    print(f"RMSE     : {rmse:.4f}")
    print()

    if r2 > best_score:
        best_score = r2
        best_model = model

# ----------------------------
# Save Model
# ----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(best_model, "models/model.pkl")
joblib.dump(encoders, "models/encoders.pkl")

print("=" * 50)
print("Best Model Saved Successfully!")
print("Accuracy :", round(best_score * 100, 2), "%")
print("=" * 50)