"""
Streamlit web application for Health-Co nutrition advisor.
"""
import streamlit as st
import base64
import os
import sys

# Add parent directory to path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import (
    calculate_bmi,
    determine_nutrition_problem,
    determine_dietary_habits,
    get_nutrition_advice,
    ask_ai_question
)

# Set Streamlit page configuration
st.set_page_config(
    page_title="Health & Co",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to set background image and font color
def set_background(image_file):
    """
    Uses Streamlit's built-in markdown function to set a background image and font color.
    """
    page_bg_img = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{image_file}") no-repeat center center fixed;
        background-size: cover;
        color: black;
    }}
    .stTextInput label, .stNumberInput label, .stSelectbox label, .stTextArea label {{
        color: black !important;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


# Function to encode an image file to base64
def get_base64_image(image_path):
    """Encode image file to base64 string."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.warning(f"Image file not found: {image_path}")
        return None


# Load and apply the background image
background_path = os.path.join("assets", "background.png")
if os.path.exists(background_path):
    image_base64 = get_base64_image(background_path)
    if image_base64:
        set_background(image_base64)

# Display the logo
logo_path = os.path.join("assets", "logo.png")
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

# App title and description
st.title("Health & Co - Personalized Nutrition Advisor")
st.markdown("### Your AI-powered nutrition companion for a healthier life")
st.markdown("### Welcome to HEALTH & CO")

# Sidebar for additional information
with st.sidebar:
    st.header("About Health & Co")
    st.markdown("""
    Health & Co is an AI-powered nutrition advisor that provides personalized 
    nutrition recommendations based on your:
    - BMI (Body Mass Index)
    - Age and gender
    - Health conditions
    - Dietary habits
    
    Get expert nutrition advice tailored to your specific needs!
    """)
    
    st.header("How it works")
    st.markdown("""
    1. Enter your personal details
    2. Provide information about your dietary habits
    3. Get personalized nutrition advice powered by AI
    """)

# Main content area
st.subheader("Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)
    gender = st.selectbox("Enter your gender:", ["Male", "Female", "Other"])
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, value=70.0, step=0.1)

with col2:
    height_in_feet = st.number_input("Enter your height (feet):", min_value=1.0, value=5.5, step=0.1)
    health_issues = st.text_input("List any health conditions (e.g., diabetes, hypertension) or type 'None'", value="None")

# Input fields for dietary habits
st.subheader("Dietary Habits")

col3, col4 = st.columns(2)

with col3:
    fruits = st.number_input("How many times per week do you eat fruits?", min_value=0, value=3)
    vegetables = st.number_input("How many times per week do you eat vegetables?", min_value=0, value=3)
    protein_sources = st.number_input("How many times per week do you consume protein sources (e.g., meat, legumes)?", min_value=0, value=2)

with col4:
    whole_grains = st.number_input("How many times per week do you consume whole grains (e.g., oats, brown rice)?", min_value=0, value=2)
    micronutrient_deficiency = st.text_input("Do you have any known micronutrient deficiencies (e.g., iron, vitamin D, calcium)? If none, type 'None'", value="None")

# Button to generate nutrition advice
if st.button("Get Nutrition Advice", type="primary"):
    dietary_habits = {
        "fruits": fruits,
        "vegetables": vegetables,
        "protein_sources": protein_sources,
        "whole_grains": whole_grains,
        "micronutrient_deficiency": micronutrient_deficiency
    }

    # Calculate BMI
    bmi = calculate_bmi(weight, height_in_feet)
    
    if isinstance(bmi, str):
        st.error(bmi)
    else:
        # Determine nutrition problem based on BMI and age
        nutrition_problem = determine_nutrition_problem(bmi, age, gender)

        # Determine dietary issue based on dietary habits
        dietary_problem = determine_dietary_habits(dietary_habits)

        # Combine nutrition problem and dietary problem
        overall_problem = nutrition_problem if nutrition_problem != "Healthy weight" else dietary_problem

        # Display results
        st.success(f"Your BMI is: **{bmi}**")
        st.info(f"Your Nutrition Problem: **{overall_problem}**")

        # Get personalized nutrition advice
        with st.spinner("Generating personalized nutrition advice..."):
            advice = get_nutrition_advice(overall_problem, age, gender, health_issues, weight, height_in_feet, bmi, dietary_habits)
        
        st.subheader("Personalized Nutrition Advice:")
        st.write(advice)

# Section for users to ask any question
st.divider()
st.subheader("Ask Any Question")
st.markdown("Have a general nutrition question? Ask our AI assistant!")

user_question = st.text_input("Type your question here:", placeholder="e.g., What are the benefits of a Mediterranean diet?")

if st.button("Get Answer"):
    if user_question:
        with st.spinner("Thinking..."):
            ai_response = ask_ai_question(user_question)
        st.subheader("AI's Answer:")
        st.write(ai_response)
    else:
        st.warning("Please type a question to ask the AI.")
