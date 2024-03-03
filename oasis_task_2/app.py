def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight_kg, height_m)
        bmi_classification = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {bmi_classification}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
