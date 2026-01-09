"""
Command-line interface for Health-Co nutrition advisor.
"""
import sys
import os

# Add parent directory to path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import (
    calculate_bmi,
    determine_nutrition_problem,
    determine_dietary_habits,
    get_nutrition_advice
)


def main():
    """Main function for CLI interface."""
    print("Welcome to the Personalized Nutrition Advisor!")
    print("Let's start by gathering your details.\n")

    while True:
        try:
            age = int(input("Enter your age: "))
            gender = input("Enter your gender (Male/Female/Other): ")
            weight = float(input("Enter your weight in kilograms: "))
            height_in_feet = float(input("Enter your height in feet: "))
            health_issues = input("List any health conditions (e.g., diabetes, hypertension) or type 'None': ")

            # Collecting dietary habits
            print("\nPlease provide the following information about your dietary habits:")
            fruits = int(input("How many times per week do you eat fruits? "))
            vegetables = int(input("How many times per week do you eat vegetables? "))
            protein_sources = int(input("How many times per week do you consume protein sources (e.g., meat, legumes)? "))
            whole_grains = int(input("How many times per week do you consume whole grains (e.g., oats, brown rice)? "))
            micronutrient_deficiency = input("Do you have any known micronutrient deficiencies (e.g., iron, vitamin D, calcium)? If none, type 'None': ")

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
                print(f"\n{bmi}\n")
                continue

            # Determine nutrition problem based on BMI and age
            nutrition_problem = determine_nutrition_problem(bmi, age, gender)

            # Determine dietary issue based on dietary habits
            dietary_problem = determine_dietary_habits(dietary_habits)

            # Combine nutrition problem and dietary problem
            overall_problem = nutrition_problem if nutrition_problem != "Healthy weight" else dietary_problem

            print(f"\nBased on the information provided, your nutrition problem is likely: {overall_problem}\n")
            print(f"Your BMI is: {bmi}\n")

            # Get personalized nutrition advice
            print("Generating personalized nutrition advice...")
            advice = get_nutrition_advice(overall_problem, age, gender, health_issues, weight, height_in_feet, bmi, dietary_habits)
            print("\nPersonalized Nutrition Advice:\n", advice)

            exit_choice = input("\nWould you like to check for another user? (yes/no): ").strip().lower()
            if exit_choice == 'no':
                print("Goodbye!")
                break
                
        except ValueError as e:
            print(f"\nInvalid input. Please enter a valid number. Error: {e}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


if __name__ == "__main__":
    main()
