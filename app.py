import streamlit as st

st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="🧬",
    layout="wide"
)

# ------------------- UI HEADER -------------------
st.title("🧬 Multiple Disease Prediction System")
st.write("An AI-based healthcare screening tool for early disease risk prediction.")

st.markdown("---")

# ------------------- SIDEBAR MENU -------------------
menu = st.sidebar.selectbox(
    "Select Prediction Module",
    ("Home", "Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction")
)

# ------------------- HOME PAGE -------------------
if menu == "Home":
    st.subheader("📌 Project Overview")
    st.write("""
    This system provides an easy interface for predicting multiple diseases using patient clinical details.
    
    ✅ Modules included:
    - Diabetes Prediction  
    - Heart Disease Prediction  
    - Parkinson’s Disease Prediction  
    
    🛠 Frontend is implemented using Streamlit.
    """)

# ------------------- DIABETES PAGE -------------------
elif menu == "Diabetes Prediction":
    st.subheader("🩸 Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Pregnancies")
        Glucose = st.text_input("Glucose Level")
        BloodPressure = st.text_input("Blood Pressure")

    with col2:
        SkinThickness = st.text_input("Skin Thickness")
        Insulin = st.text_input("Insulin Level")
        BMI = st.text_input("BMI")

    with col3:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
        Age = st.text_input("Age")

    if st.button("🔍 Predict Diabetes"):
        st.success("✅ Frontend completed! (Model integration pending)")

# ------------------- HEART PAGE -------------------
elif menu == "Heart Disease Prediction":
    st.subheader("❤️ Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
        sex = st.text_input("Sex (0 = Female, 1 = Male)")
        cp = st.text_input("Chest Pain Type (0-3)")

    with col2:
        trestbps = st.text_input("Resting Blood Pressure")
        chol = st.text_input("Serum Cholesterol")
        fbs = st.text_input("Fasting Blood Sugar (0/1)")

    with col3:
        restecg = st.text_input("Resting ECG (0-2)")
        thalach = st.text_input("Max Heart Rate Achieved")
        oldpeak = st.text_input("Oldpeak (ST Depression)")

    if st.button("🔍 Predict Heart Disease"):
        st.success("✅ Frontend completed! (Model integration pending)")

# ------------------- PARKINSON PAGE -------------------
elif menu == "Parkinson's Prediction":
    st.subheader("🧠 Parkinson’s Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        fhi = st.text_input("MDVP:Fhi(Hz)")
        flo = st.text_input("MDVP:Flo(Hz)")

    with col2:
        jitter_percent = st.text_input("MDVP:Jitter(%)")
        shimmer = st.text_input("MDVP:Shimmer")
        nhr = st.text_input("NHR")

    with col3:
        hnr = st.text_input("HNR")
        rpde = st.text_input("RPDE")
        dfa = st.text_input("DFA")

    if st.button("🔍 Predict Parkinson's"):
        st.success("✅ Frontend completed! (Model integration pending)")

# ------------------- FOOTER -------------------
st.markdown("---")
st.caption("⚡ Developed for Final Year Project | Domain: Biotech & Healthcare")
