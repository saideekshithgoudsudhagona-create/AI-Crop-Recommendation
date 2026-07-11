# import streamlit as st
# import plotly.express as px #new
# import plotly.graph_objects as go #new
# import pandas as pd
# import joblib
# from recommendation import recommend_crop

# # ---------------------------------------------------
# # PAGE CONFIG
# # ---------------------------------------------------

# st.set_page_config(
#     page_title="AI Crop Yield Prediction",
#     page_icon="🌾",
#     layout="wide"
# )

# st.markdown("""
# <style>

# .main{
# background-color:#f7faf7;
# }

# .big-title{
# font-size:42px;
# font-weight:bold;
# color:#1B5E20;
# }

# .sub-title{
# font-size:18px;
# color:gray;
# }

# .card{
# background:#ffffff;
# padding:20px;
# border-radius:15px;
# box-shadow:0px 3px 10px rgba(0,0,0,0.15);
# text-align:center;
# }

# .metric{
# font-size:35px;
# font-weight:bold;
# color:#2E7D32;
# }

# </style>
# """,unsafe_allow_html=True)


# st.markdown(
# "<div class='big-title'>🌾 Crop Recommendation & Yield Prediction</div>",
# unsafe_allow_html=True
# )

# st.markdown(
# "<div class='sub-title'>Machine Learning Powered Agriculture Decision Support System</div>",
# unsafe_allow_html=True
# )

# # st.title("🌾 AI Crop Recommendation & Yield Prediction")
# # st.write("Predict suitable crop and expected production.")

# # ---------------------------------------------------
# # LOAD MODEL
# # ---------------------------------------------------

# model = joblib.load("models/model.pkl")
# encoders = joblib.load("models/encoders.pkl")

# # ---------------------------------------------------
# # LOAD DATASET
# # ---------------------------------------------------

# df = pd.read_csv("dataset/crop_data.csv")
# st.write("8")

# for col in ["State_Name", "District_Name", "Season", "Crop"]:
#     df[col] = df[col].astype(str).str.strip()

# df["District_Name"] = df["District_Name"].str.upper()
# st.write("9")

# # ---------------------------------------------------
# # SIDEBAR
# # ---------------------------------------------------

# st.sidebar.header("Enter Crop Details")

# state = st.sidebar.selectbox(
#     "State",
#     sorted(df["State_Name"].unique())
# )

# district = st.sidebar.selectbox(
#     "District",
#     sorted(
#         df[df["State_Name"] == state]["District_Name"].unique()
#     )
# )

# season = st.sidebar.selectbox(
#     "Season",
#     sorted(df["Season"].unique())
# )

# crop_year = st.sidebar.number_input(
#     "Crop Year",
#     2000,
#     2035,
#     2025
# )

# temperature = st.sidebar.slider(
#     "Temperature",
#     0,
#     50,
#     30
# )

# humidity = st.sidebar.slider(
#     "Humidity",
#     0,
#     100,
#     70
# )

# soil = st.sidebar.slider(
#     "Soil Moisture",
#     0,
#     100,
#     50
# )

# area = st.sidebar.number_input(
#     "Area",
#     1.0,
#     10000.0,
#     5.0
# )
# st.write("10")
# # ---------------------------------------------------
# # RECOMMEND CROP
# # ---------------------------------------------------

# recommended_crop = recommend_crop(
#     temperature,
#     humidity,
#     soil
# )
# st.write("11")
# confidence = 96
# # st.sidebar.success(
# #     f"Recommended Crop : {recommended_crop}"
# # )
# st.sidebar.success("AI Recommendation Ready")
# col1,col2,col3,col4=st.columns(4)

# with col1:
#     st.metric(
#         "🌡 Temperature",
#         f"{temperature}°C"
#     )

# with col2:
#     st.metric(
#         "💧 Humidity",
#         f"{humidity}%"
#     )

# with col3:
#     st.metric(
#         "🌱 Soil Moisture",
#         f"{soil}%"
#     )

# with col4:
#     st.metric(
#         "⭐ Confidence",
#         f"{confidence}%"
#     )
# # ---------------------------------------------------
# # PREDICT BUTTON
# # ---------------------------------------------------
# st.write("12")
# if st.sidebar.button("Predict"):

#     # Check if recommended crop exists in dataset
#     if recommended_crop not in encoders["Crop"].classes_:

#         st.error(
#             f"{recommended_crop} is not available in the training dataset."
#         )

#     else:

#         state_encoded = encoders["State_Name"].transform([state])[0]

#         district_encoded = encoders["District_Name"].transform([district])[0]

#         season_encoded = encoders["Season"].transform([season])[0]

#         crop_encoded = encoders["Crop"].transform(
#             [recommended_crop]
#         )[0]

#         input_df = pd.DataFrame({

#             "State_Name":[state_encoded],

#             "District_Name":[district_encoded],

#             "Crop_Year":[crop_year],

#             "Season":[season_encoded],

#             "Crop":[crop_encoded],

#             "Temperature":[temperature],

#             "Humidity":[humidity],

#             "Soil_Moisture":[soil],

#             "Area":[area]

#         })

#         prediction = model.predict(input_df)[0]

#         st.success("Prediction Completed Successfully")

#         st.header("Prediction Result")

#         st.write("### 🌱 Recommended Crop")

#         # st.success(recommended_crop)
#         st.markdown("## 🌱 Recommended Crop")

#         st.success(recommended_crop)

#         st.info(
# """
# Reason

# ✔ Climate matches crop requirements

# ✔ Suitable humidity

# ✔ Suitable soil moisture

# ✔ Historical production is high
# """
# )

#         # st.write("### 🌾 Expected Production")

#         # st.metric(
#         #     "Production",
#         #     f"{prediction:.2f} Tons"
#         # )
#     st.markdown("## 📈 Expected Production")

#     st.metric(
#     label="Production",
#     value=f"{prediction:.2f} Tons"
# )
# # ---------------------------------------------------
# # DATASET
# # ---------------------------------------------------

# st.header("Dataset Preview")

# # st.dataframe(df.head())
# filtered_df=df[
# (df["State_Name"]==state)&
# (df["District_Name"]==district)&
# (df["Season"]==season)
# ]

# st.dataframe(
# filtered_df,
# use_container_width=True
# )
# st.write("13")
# # ---------------------------------------------------
# # ANALYTICS
# # ---------------------------------------------------

# # st.header("📊 Analytics")

# # if not filtered_df.empty:

# #     crop_chart = (
# #         filtered_df
# #         .groupby("Crop")["Production"]
# #         .sum()
# #         .reset_index()
# #     )

# #     fig = px.bar(
# #         crop_chart,
# #         x="Crop",
# #         y="Production",
# #         color="Production",
# #         title="Production by Crop"
# #     )

# #     # st.plotly_chart(
# #     #     fig,
# #     #     use_container_width=True
# #     # )
# #     st.write("14")
# # else:
# #     st.warning("No data available for the selected filters.")
# # # ---------------------------------------------------
# # # ABOUT
# # # ---------------------------------------------------

# # st.header("About")
# st.header("📊 Analytics")

# st.write("Reached Analytics")

# import plotly.express as px

# test = pd.DataFrame({
#     "Crop": ["Rice", "Wheat", "Maize"],
#     "Production": [100, 200, 150]
# })

# fig = px.bar(
#     test,
#     x="Crop",
#     y="Production",
#     title="Test Chart"
# )

# st.plotly_chart(fig)

# st.header("About")

# st.write("About section")

# st.write("""
# ### Algorithms Used

# - Linear Regression
# - Decision Tree
# - Random Forest

# ### Functional Flow

# User Input

# ↓

# Crop Recommendation

# ↓

# Yield Prediction

# ↓

# Display Result
# """)
# # import streamlit as st
# # st.write("1")

# # import pandas as pd
# # st.write("2")

# # import joblib
# # st.write("3")

# # import plotly.express as px
# # st.write("4")

# # from recommendation import recommend_crop
# # st.write("5")

# # model = joblib.load("models/model.pkl")
# # st.write("6")

# # encoders = joblib.load("models/encoders.pkl")
# # st.write("7")
# st.write("15")
import streamlit as st
import pandas as pd
import joblib

st.title("Debug Test")

st.write("1. Imports OK")

df = pd.read_csv("dataset/crop_data.csv")
st.write("2. Dataset Loaded")

model = joblib.load("models/model.pkl")
st.write("3. Model Loaded")

encoders = joblib.load("models/encoders.pkl")
st.write("4. Encoders Loaded")

import recommendation
st.write("5. recommendation.py Imported")

st.success("Everything loaded successfully")