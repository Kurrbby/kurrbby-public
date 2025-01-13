# Solar System Weight Calculator
# Calculate your weight on different planets based on your Earth weight.

'''
Overview:
    1. define calculations (ratios and lbs to kg conversion)
    2. define user input handling (main function)
    3. Run the program
'''


def calculate_planet_weights(earth_weight, unit="kg"):
    """
    Calculates your weight on other planets based on your Earth weight.
    
    Parameters:
        earth_weight (float): Weight on Earth.
        unit (str): Unit of weight ('kg' or 'lbs').
    
    Returns:
        dict: A dictionary with planet names as keys and weights as values.
    """
    # Surface gravity ratios relative to Earth
    gravity_ratios = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19
    }
    
    # Conversion factor for lbs to kgs
    lbs_to_kg = 0.453592

    # Convert input weight to kilograms if in lbs
    if unit.lower() == "lbs":
        earth_weight_kg = earth_weight * lbs_to_kg
    else:
        earth_weight_kg = earth_weight

    # Calculate weights on each planet in kilograms
    planet_weights_kg = {
        planet: earth_weight_kg * ratio for planet, ratio in gravity_ratios.items()
    }

    # Convert weights back to lbs if required
    if unit.lower() == "lbs":
        planet_weights = {planet: weight / lbs_to_kg for planet, weight in planet_weights_kg.items()}
    else:
        planet_weights = planet_weights_kg

    return planet_weights


# Input handling
def main():
    print("Solar System Weight Calculator")
    print("Choose the unit of your weight:")
    print("1. Kilograms (kg)")
    print("2. Pounds (lbs)")
    
    unit_choice = input("Enter 1 or 2: ").strip()
    if unit_choice == "1":
        unit = "kg"
    elif unit_choice == "2":
        unit = "lbs"
    else:
        print("Invalid choice. Defaulting to kilograms (kg).")
        unit = "kg"
    
    earth_weight = float(input(f"Enter your weight on Earth ({unit}): "))
    weights_on_planets = calculate_planet_weights(earth_weight, unit=unit)
    
    # Display results
    print(f"\nYour weight on different planets ({unit}):")
    for planet, weight in weights_on_planets.items():
        print(f"{planet}: {weight:.2f} {unit}")



# Run the program
if __name__ == "__main__":
    main()
