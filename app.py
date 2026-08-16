import streamlit as st
import joblib
import pandas as pd

model = joblib.load("pipe.pkl")
data = pd.read_csv("data.csv")

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

/* ---------------- BODY ---------------- */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(198, 164, 93, 0.10), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(30, 41, 59, 0.08), transparent 30%),
        #f7f5f0;
    font-family: 'DM Sans', sans-serif;
}

/* Remove top padding */

.block-container {
    padding-top: 1rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* ---------------- HEADER ---------------- */

.hero {
    background:
        linear-gradient(rgba(15, 23, 42, 0.78), rgba(15, 23, 42, 0.88)),
        linear-gradient(135deg, #172033, #26344d);

    border-radius: 28px;
    padding: 55px 60px;
    margin-bottom: 30px;
    color: white;

    box-shadow: 0 20px 50px rgba(15, 23, 42, 0.18);
}

.hero-small {
    color: #d8b978;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 15px;
}

.hero-description {
    font-size: 17px;
    color: #d5d9e0;
    max-width: 650px;
    line-height: 1.7;
}

/* ---------------- SECTION TITLES ---------------- */

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    font-weight: 600;
    color: #172033;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #6b7280;
    font-size: 15px;
    margin-bottom: 25px;
}

/* ---------------- INPUT CARD ---------------- */

.input-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid #e8e3d9;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 12px 35px rgba(15,23,42,0.07);
    margin-bottom: 25px;
}

/* Labels */

label {
    color: #374151 !important;
    font-weight: 600 !important;
}

/* Inputs */

div[data-baseweb="select"] > div {
    border-radius: 12px !important;
    border: 1px solid #d9d4ca !important;
    background: #fff !important;
}

input {
    border-radius: 12px !important;
}

/* ---------------- BUTTON ---------------- */

div.stButton > button {
    width: 100%;
    height: 58px;

    background: #c6a45d;
    color: #172033;

    border: none;
    border-radius: 14px;

    font-size: 17px;
    font-weight: 700;

    box-shadow: 0 10px 25px rgba(198,164,93,0.28);

    transition: all 0.25s ease;
}

div.stButton > button:hover {
    background: #b6924c;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 14px 30px rgba(198,164,93,0.35);
}

/* ---------------- RESULT CARD ---------------- */

.result-card {
    background:
        linear-gradient(135deg, #172033, #26344d);

    border-radius: 26px;
    padding: 38px;

    color: white;

    box-shadow: 0 20px 45px rgba(15,23,42,0.20);

    margin-top: 10px;
    text-align: center;
}

.result-label {
    color: #d8b978;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.result-price {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 700;
    margin-top: 10px;
}

.result-crore {
    color: #d5d9e0;
    font-size: 17px;
    margin-top: 5px;
}

/* ---------------- STAT CARDS ---------------- */

.stat-card {
    background: white;
    border: 1px solid #e8e3d9;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
}

.stat-number {
    font-size: 26px;
    font-weight: 700;
    color: #172033;
}

.stat-label {
    color: #737b87;
    font-size: 13px;
    margin-top: 5px;
}

/* ---------------- FOOTER ---------------- */

.footer {
    text-align: center;
    color: #8a8f98;
    margin-top: 45px;
    padding-top: 25px;
    border-top: 1px solid #ddd8ce;
    font-size: 13px;
}

.footer strong {
    color: #172033;
}

/* ---------------- HIDE STREAMLIT ELEMENTS ---------------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)



st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title('Banglore House Price Prediction')
st.write('Enter the house details to predict the price.')

locations = sorted(data["location"].dropna().unique())

location = st.selectbox(
    "Select Location",
    locations
)

total_sqft = st.number_input(
    "Total Area (sqft)",
    min_value=300.0,
    max_value=10000.0,
    value=1200.0,
    step=50.0
)

bath = st.number_input(
    "Number of Bathrooms",
    min_value=1.0,
    max_value=10.0,
    value=2.0,
    step=1.0
)

bhk = st.number_input(
    "Number of BHK",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)   

if st.button("Predict Price 🚀"):

    input_data = pd.DataFrame({
        "location": [location],
        "total_sqft": [total_sqft],
        "bath": [bath],
        "bhk": [bhk]
    })

    try:
        prediction = model.predict(input_data)

        st.success(
            f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs"
        )


        if prediction[0] >= 100:
            crore = prediction[0] / 100
            st.info(f"Approximately ₹ {crore:.2f} Crore")

    except Exception as e:
        st.error(f"Prediction error: {e}")