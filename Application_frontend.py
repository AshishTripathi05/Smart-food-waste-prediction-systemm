import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Smart Food Waste Predictor",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling: Crisp Light Theme (White Background + Dark Green Headings)
st.markdown("""
    <style>
    /* Main Background & Text Colors */
    .stApp {
        background-color: #FAFAFA;
        color: #1E293B;
    }

    /* Green Main Titles and Subheadings */
    h1 {
        color: #166534 !important;
        font-weight: 700;
    }
    h2, h3 {
        color: #15803D !important;
        font-weight: 600;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #F1F5F9;
        border-right: 1px solid #E2E8F0;
    }

    /* Green Primary Action Button */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #166534;
        color: #FFFFFF;
        font-weight: 600;
        border: none;
    }
    .stButton>button:hover {
        background-color: #15803D;
        color: #FFFFFF;
    }

    /* Metric Card Custom White Background */
    [data-testid="stMetricValue"] {
        color: #166534 !important;
        font-size: 1.8rem !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌱 Smart Food Waste Prediction System")
st.caption("Forecast daily meal demand using machine learning to minimize food waste.")
st.markdown("---")


# Load Trained Model & Column Features
@st.cache_resource
def load_ml_assets():
    model = joblib.load('models/food_waste_model.pkl')
    columns = joblib.load('models/model_columns.pkl')
    return model, columns


try:
    model, model_columns = load_ml_assets()
except Exception:
    st.error("⚠️ Error loading trained model. Make sure model files exist in the 'models/' folder.")
    st.stop()

# Sidebar Input Setup
st.sidebar.header("📊 Operating Inputs")

day_of_week = st.sidebar.selectbox("Day of Week",
                                   ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
weather = st.sidebar.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy", "Windy"])
temp = st.sidebar.slider("Temperature (°C)", min_value=10, max_value=45, value=28)

weekend = st.sidebar.selectbox("Is Weekend?", ["No", "Yes"])
festival = st.sidebar.selectbox("Is Festival?", ["No", "Yes"])
holiday = st.sidebar.selectbox("Is Holiday?", ["No", "Yes"])

prev_sales = st.sidebar.number_input("Previous Day Sales (Meals)", min_value=0, max_value=1000, value=200, step=10)

# Main Dashboard Display
st.subheader("💡 Predictions & Recommended Plan")

if st.sidebar.button("🚀 Generate Forecast"):
    input_data = pd.DataFrame([{
        'Day_of_Week': day_of_week,
        'Weather': weather,
        'Temperature': temp,
        'Weekend': weekend,
        'Festival': festival,
        'Holiday': holiday,
        'Previous_Day_Sales': prev_sales
    }])

    # Process One-Hot Encoding Alignment
    input_encoded = pd.get_dummies(input_data)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Predict & Compute Buffer
    predicted_sales = max(0, round(model.predict(input_encoded)[0]))
    recommended_prep = round(predicted_sales * 1.05)
    expected_surplus = recommended_prep - predicted_sales

    # Display Output Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Predicted Meal Sales", f"{predicted_sales} meals")
    c2.metric("Recommended Prep (5% Buffer)", f"{recommended_prep} meals", delta=f"+{expected_surplus} safety margin")
    c3.metric("Target Waste Threshold", "< 2%", delta="Optimal Range", delta_color="normal")

    st.markdown("---")
    st.success(
        f"✅ **Kitchen Action:** Prepare **{recommended_prep} meals** for optimal service coverage with minimal food waste.")
else:
    st.info("👈 Set daily operating parameters in the sidebar and click **'Generate Forecast'**.")