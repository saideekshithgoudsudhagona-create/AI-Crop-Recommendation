def recommend_crop(temp, humidity, soil):

    # Rice
    if temp >= 28 and humidity >= 75 and soil >= 60:
        return "Rice"

    # Sugarcane
    elif temp >= 25 and humidity >= 70:
        return "Sugarcane"

    # Cotton
    elif temp >= 24 and humidity >= 50:
        return "Cotton(lint)"

    # Maize
    elif temp >= 22 and humidity >= 55:
        return "Maize"

    # Groundnut
    elif temp >= 20 and soil < 45:
        return "Groundnut"

    # Wheat
    else:
        return "Wheat"