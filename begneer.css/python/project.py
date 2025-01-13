def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        # Get user input
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        # Validate inputs
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values. Please try again.")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI
        category = classify_bmi(bmi)

        # Display the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()