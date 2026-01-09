"""
Utility functions for Health-Co nutrition advisor.
Shared functions used by both CLI and web interface.
"""
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini AI
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please create a .env file.")

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"


def calculate_bmi(weight, height_in_feet):
    """
    Calculates BMI based on weight (kg) and height in feet.
    
    Args:
        weight: Weight in kilograms
        height_in_feet: Height in feet
        
    Returns:
        BMI value rounded to 2 decimal places
    """
    # Convert height from feet to meters (1 foot = 0.3048 meters)
    height_in_meters = height_in_feet * 0.3048
    try:
        bmi = weight / (height_in_meters ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."


def determine_nutrition_problem(bmi, age, gender):
    """
    Determines the likely nutrition problem based on BMI, age, and gender.
    
    Args:
        bmi: Body Mass Index
        age: Age in years
        gender: Gender (Male/Female/Other)
        
    Returns:
        String describing the nutrition problem
    """
    # Nutrition problem based on BMI
    if bmi < 18.5:
        return "Malnutrition (underweight)"
    elif 18.5 <= bmi < 24.9:
        return "Healthy weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif bmi >= 30:
        return "Obesity"
    
    # If BMI falls in the healthy range, check for age-related factors (e.g., elderly)
    if age >= 65:
        return "Potential age-related malnutrition"
    return "Undetermined nutrition problem"


def determine_dietary_habits(dietary_habits):
    """
    Determines the likelihood of poor dietary diversity or micronutrient deficiency based on user input.
    
    Args:
        dietary_habits: Dictionary containing dietary habit information
        
    Returns:
        String describing the dietary issue
    """
    fruits = int(dietary_habits["fruits"])  # Number of times per week
    vegetables = int(dietary_habits["vegetables"])
    protein_sources = int(dietary_habits["protein_sources"])
    whole_grains = int(dietary_habits["whole_grains"])
    micronutrient_deficiency = dietary_habits["micronutrient_deficiency"]

    if fruits < 3 or vegetables < 3 or protein_sources < 2 or whole_grains < 2:
        return "Poor dietary diversity"

    if micronutrient_deficiency.lower() != "none":
        return f"Possible micronutrient deficiency (e.g., {micronutrient_deficiency})"

    return "Balanced diet"


def get_nutrition_advice(category, age, gender, health_issues, weight, height_in_feet, bmi, dietary_habits):
    """
    Fetches personalized nutrition advice based on category, age, gender, health issues, weight, height, BMI, and dietary habits.
    
    Args:
        category: Nutrition problem category
        age: Age in years
        gender: Gender
        health_issues: Health conditions
        weight: Weight in kg
        height_in_feet: Height in feet
        bmi: Body Mass Index
        dietary_habits: Dictionary of dietary habits
        
    Returns:
        String containing personalized nutrition advice
    """
    prompts = {
        "Malnutrition (underweight)": "Explain how to prevent and treat malnutrition, including essential nutrients and diet recommendations.",
        "Healthy weight": "Provide general health and nutrition advice for maintaining a healthy weight.",
        "Overweight": "Provide expert advice on managing overweight, including diet, exercise, and healthy lifestyle changes.",
        "Obesity": "Give expert advice on managing obesity, including diet, exercise, and healthy lifestyle changes.",
        "Potential age-related malnutrition": "Provide nutrition advice for elderly individuals, focusing on preventing age-related malnutrition.",
        "Poor dietary diversity": "Provide advice on how to improve dietary diversity, including incorporating more food groups.",
        "Possible micronutrient deficiency": "Provide advice on addressing micronutrient deficiencies, including food sources and supplementation recommendations.",
        "Balanced diet": "Give general advice on maintaining a balanced and healthy diet."
    }

    user_prompt = (
        f"{prompts[category]} Consider a {gender}, {age} years old, with a weight of {weight} kg, "
        f"height of {height_in_feet} feet (BMI: {bmi}). The individual has the following health concerns: {health_issues}. "
        f"Dietary habits: {dietary_habits}. Make the advice specific to this individual's needs."
    )

    try:
        response = requests.post(
            f"{GEMINI_API_URL}?key={GENAI_API_KEY}",
            json={
                "contents": [{
                    "parts": [{
                        "text": user_prompt
                    }]
                }]
            },
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error: {e}"


def ask_ai_question(question):
    """
    Sends the user's question to the AI model and returns the response.
    
    Args:
        question: User's question string
        
    Returns:
        String containing AI's response
    """
    prompt = f"Answer the following question: {question}"

    try:
        response = requests.post(
            f"{GEMINI_API_URL}?key={GENAI_API_KEY}",
            json={
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }]
            },
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Error: {e}"
