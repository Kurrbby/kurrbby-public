def calculate_bmi(weight, height, unit="metric"):
    """
    Calculates Body Mass Index (BMI).
    
    Parameters:
        weight (float): Weight of the person (kg or lbs).
        height (float): Height of the person (cm or in).
        unit (str): Unit system ('metric' or 'imperial').
    
    Returns:
        float: The calculated BMI.
    """
    if unit.lower() == "metric":
        height_meters = height / 100 # Convert cm to m
        bmi = weight / (height_meters ** 2)
    elif unit.lower() == "imperial":
        bmi = (weight * 703) / (height ** 2)
    else:
        raise ValueError("Invalid unit. Choose 'metric' or 'imperial'.")
    
    return bmi


def main():
    print("BMI Calculator")
    print("Choose the unit system:")
    print("1. Metric (kg, cm)")
    print("2. Imperial (lbs, in)")
    
    unit_choice = input("Enter 1 or 2: ").strip()
    
    if unit_choice == "1":
        unit = "metric"
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
    elif unit_choice == "2":
        unit = "imperial"
        weight = float(input("Enter your weight (lbs): "))
        height = float(input("Enter your height (in): "))
    else:
        print("Invalid choice. Please restart and select a valid unit system.")
        return
    
    bmi = calculate_bmi(weight, height, unit)
    print(f"\nYour BMI is: {bmi:.2f}")
    
    # BMI Categories (Standard WHO Classification)
    print("\nBMI Categories:")
    print("Underweight: <18.5")
    print("Normal weight: 18.5–24.9")
    print("Overweight: 25–29.9")
    print("Obesity: 30 or greater")
    
    # Provide category feedback
    if bmi < 18.5:
        print("BMI: ", bmi, ". You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("BMI: ", bmi, ". You are in the normal weight range.")
    elif 25 <= bmi < 29.9:
        print("BMI: ", bmi, ". You are overweight.")
    else:
        print("BMI: ", bmi, ". You are in the obesity range.")


# Run the program
if __name__ == "__main__":
    main()
