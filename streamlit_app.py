import streamlit as st
import numpy as np
import pickle

# Load the trained diabetes model
model = pickle.load(open('diabetes_model.sav', 'rb'))

# Custom background and text styling with CSS
st.markdown(
    """
    <style>
    /* App background */
    .main {
        background-color: #f4f4f9;
    }

    /* Title text styling */
    h1 {
        color: #3d3c3a;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }

    /* Input button color */
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

# Title with enhanced styling
st.title('🌟 Diabetes Prediction App 🌟')

# Input fields
st.subheader("Please enter the following information:")
pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1, help="Enter the number of pregnancies")
glucose = st.number_input('Glucose Level', min_value=0.0, help="Enter the glucose level")
blood_pressure = st.number_input('Blood Pressure Level', min_value=0.0, help="Enter the blood pressure level")
skin_thickness = st.number_input('Skin Thickness', min_value=0.0, help="Enter the skin thickness")
insulin = st.number_input('Insulin Level', min_value=0.0, help="Enter the insulin level")
bmi = st.number_input('BMI (Body Mass Index)', min_value=0.0, help="Enter the BMI")
diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, help="Enter the pedigree function value")
age = st.number_input('Age', min_value=0, step=1, help="Enter the age")

# Collecting the input data
input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

# Prediction result
result = ''

# Prediction button
if st.button('Predict'):
    # Convert input data to a NumPy array and reshape it for the model
    input_data = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    
    # Display the result based on the prediction
    if prediction[0] == 1:
        result = '🔴 The model predicts that the person has diabetes.'
    else:
        result = '🟢 The model predicts that the person does not have diabetes.'

# Display prediction result
if result:
    st.markdown(f"<h2 style='text-align: center; color: #3d3c3a;'>{result}</h2>", unsafe_allow_html=True)
