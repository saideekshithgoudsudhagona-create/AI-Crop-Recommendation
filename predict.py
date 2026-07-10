import joblib
import pandas as pd
from recommendation import recommend_crop

# Load model
model = joblib.load("models/model.pkl")

# Load encoders
encoders = joblib.load("models/encoders.pkl")


def predict_crop_production(
    state,
    district,
    crop_year,
    season,
    crop,
    temperature,
    humidity,
    soil_moisture,
    area
):

    # Clean user inputs
    state = state.strip()
    district = district.strip().upper()
    season = season.strip()
    crop = recommend_crop(
    temperature,
    humidity,
    soil_moisture
)

    # Encode categorical values
    state = encoders["State_Name"].transform([state])[0]
    district = encoders["District_Name"].transform([district])[0]
    season = encoders["Season"].transform([season])[0]
    crop = encoders["Crop"].transform([crop])[0]

    # Create input dataframe
    data = pd.DataFrame({
        "State_Name": [state],
        "District_Name": [district],
        "Crop_Year": [crop_year],
        "Season": [season],
        "Crop": [crop],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "Soil_Moisture": [soil_moisture],
        "Area": [area]
    })

    prediction = model.predict(data)

    return round(prediction[0], 2)


# ----------------------------
# Test Prediction
# ----------------------------
if __name__ == "__main__":

    result = predict_crop_production(
        state="Andhra Pradesh",
        district="ANANTAPUR",
        crop_year=2015,
        season="Kharif",
        crop="Rice",
        temperature=30,
        humidity=70,
        soil_moisture=55,
        area=5
    )

    print("\nPredicted Production:", result)