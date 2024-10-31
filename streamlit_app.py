import streamlit as st
import numpy as np
import pickle

# Load the trained diabetes model
model = pickle.load(open('diabetes_model.sav', 'rb'))

# Language selection
language = st.selectbox("Select Language / اختر اللغة", ("English", "العربية"))

# Define texts based on language
if language == "English":
    title = "🌟 Diabetes Prediction App 🌟"
    instructions = "Please enter the following information:"
    fields = {
        "pregnancies": "Number of Pregnancies",
        "glucose": "Glucose Level",
        "blood_pressure": "Blood Pressure Level",
        "skin_thickness": "Skin Thickness",
        "insulin": "Insulin Level",
        "bmi": "BMI (Body Mass Index)",
        "diabetes_pedigree_function": "Diabetes Pedigree Function",
        "age": "Age",
    }
    predict_button = "Predict"
    result_positive = "🔴 The model predicts that the person has diabetes."
    result_negative = "🟢 The model predicts that the person does not have diabetes."
else:
    title = "🌟 تطبيق توقع السكري 🌟"
    instructions = "يرجى إدخال المعلومات التالية:"
    fields = {
        "pregnancies": "عدد مرات الحمل",
        "glucose": "مستوى الجلوكوز",
        "blood_pressure": "مستوى ضغط الدم",
        "skin_thickness": "سُمك الجلد",
        "insulin": "مستوى الأنسولين",
        "bmi": "مؤشر كتلة الجسم",
        "diabetes_pedigree_function": "وظيفة النسب الوراثي للسكري",
        "age": "العمر",
    }
    predict_button = "توقع"
    result_positive = "🔴 النموذج يتوقع أن الشخص لديه السكري."
    result_negative = "🟢 النموذج يتوقع أن الشخص ليس لديه السكري."

# Add background image using CSS
st.markdown(
    """
    <style>
    .main {
        background-image: url("");
        background-size: cover;
        background-position: center;
    }
    h1 {
        color: #3d3c3a;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and instructions
st.title(title)
st.subheader(instructions)

# Divide input fields into columns
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input(fields["pregnancies"], min_value=0, step=1)
    blood_pressure = st.number_input(fields["blood_pressure"], min_value=0.0)
    insulin = st.number_input(fields["insulin"], min_value=0.0)
    diabetes_pedigree_function = st.number_input(fields["diabetes_pedigree_function"], min_value=0.0)

with col2:
    glucose = st.number_input(fields["glucose"], min_value=0.0)
    skin_thickness = st.number_input(fields["skin_thickness"], min_value=0.0)
    bmi = st.number_input(fields["bmi"], min_value=0.0)
    age = st.number_input(fields["age"], min_value=0, step=1)

# Collect input data
input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

# Prediction result
result = ''

# Prediction button
if st.button(predict_button):
    input_data = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    
    # Display result based on prediction
    result = result_positive if prediction[0] == 1 else result_negative

# Display prediction result
if result:
    st.markdown(f"<h2 style='text-align: center; color: #3d3c3a;'>{result}</h2>", unsafe_allow_html=True)
