import os
import google.generativeai as genai
import streamlit as st

# Configure Google Generative AI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Streamlit interface
st.title("Patient Health Prediction and Caution System")

# Input fields
name = st.text_input("Enter your name :")
age = st.number_input("Enter your age :", min_value=1, max_value=120)
height = st.number_input("Enter your Height (in cm):", min_value=50.0, max_value=250.0)
weight = st.number_input("Enter your Weight (in kg):", min_value=10, max_value=300)

# BMI Calculator
def bmi_cal(h, w):
    BMI = (w / (h * h)) * 10000
    bmi_val = round(BMI, 2)
    return bmi_val

bmi = bmi_cal(height, weight)
st.write("Your BMI is: ", bmi)

# Smoking habit
smoke = st.radio("Do you smoke?", ("Yes", "No"))
if smoke == "Yes":
    smoking = st.slider("How often do you smoke?", 1, 5)
else:
    smoking = "no"

# Alcohol habit
drink = st.radio("Do you consume alcohol?", ("Yes", "No"))
if drink == "Yes":
    alcohol = st.slider("How often do you drink?", 1, 5)
else:
    alcohol = "no"

# Blood Pressure
bp = st.number_input("Enter your blood pressure :", min_value=50, max_value=200)

# Stress level
stress = st.radio("Do you experience stress?", ("Yes", "No"))
if stress == "Yes":
    stress_level = st.slider("How often do you experience stress?", 1, 5)
else:
    stress_level = "not taking"

# Fast food frequency
fast_food = st.slider("How often do you eat fast food? [1-5]", 0, 5)

# Family history
family_history = st.radio("Do you have a family history of diseases?", ("No", "Minor", "Major"))
if family_history in ("Minor", "Major"):
    family_disease = st.text_input("Specify the disease(s) related to your family history :")
else:
    family_disease = "None"

# Occupation
work = st.text_input("Enter your occupation :")

# Generate predictions when button is clicked
if st.button("Predict Health Risk"):
    st.write(f"Hello {name}, here are your predictions based on the inputs:")

    # Construct the prompt for the AI model
    prompt = f"""what health issues may arise in future when person with age : {age} 
    body mass index : {bmi}, smoking habit is : {smoking} out of 5, alcohol habit is : {alcohol} 
    out of 5, blood pressure is : {bp}, stress level is : {stress_level} out of 5, 
    fast food consumption is : {fast_food} out of 5, family history is : {family_history}, 
    family disease specified: {family_disease}. Note that 0 means not applicable. 
    If smoking or alcohol consumption is more than 3, provide suggestions for improvement 
    on how to leave these bad habits and improve health based on current habits. 
    Do not display a warning on top, just give predictions and suggestions without extra words."""

    # Generative AI Model for predictions
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    st.write(response.text)