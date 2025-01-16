# Distribution Waterfall IRR Hurdles

def calculate_irr_hurdle_distribution(
    total_cash_flow, capital_contributed, hurdles, splits
):
    """
    Simulates a waterfall distribution model based on IRR hurdles.
    
    Parameters:
        total_cash_flow (float): Total cash available for distribution.
        capital_contributed (float): Total capital contributed by investors.
        hurdles (list): List of IRR hurdle rates (e.g., [0.08, 0.15, 0.20]).
        splits (list): List of split ratios for each hurdle (e.g., [(80, 20), (70, 30), (50, 50)]).
    
    Returns:
        dict: A dictionary showing distributions at each hurdle.
    """
    if len(hurdles) != len(splits):
        raise ValueError("Hurdles and splits must have the same length.")
    
    distribution = {}
    remaining_cash = total_cash_flow
    investor_capital_remaining = capital_contributed

    for i, (hurdle, split) in enumerate(zip(hurdles, splits)):
        tier_name = f"Tier {i+1} (Hurdle: {hurdle*100:.1f}%)"
        investor_share = split[0] / 100
        sponsor_share = split[1] / 100
        
        if remaining_cash <= 0:
            distribution[tier_name] = {"Investor": 0, "Sponsor": 0}
            continue

        if i == 0:  # Return of Capital Tier
            tier_distribution = min(remaining_cash, investor_capital_remaining)
            remaining_cash -= tier_distribution
            investor_capital_remaining -= tier_distribution
            distribution[tier_name] = {"Investor": tier_distribution, "Sponsor": 0}
        else:
            # For other tiers, calculate distribution based on splits
            tier_distribution = remaining_cash
            investor_distribution = tier_distribution * investor_share
            sponsor_distribution = tier_distribution * sponsor_share
            remaining_cash = 0
            distribution[tier_name] = {
                "Investor": investor_distribution,
                "Sponsor": sponsor_distribution,
            }
    
    return distribution


def main():
    print("Waterfall Distribution Model (IRR Hurdles)")

    # Get total cash flow and capital contributed
    total_cash_flow = float(input("Enter the total cash flow available for distribution: "))
    capital_contributed = float(input("Enter the total capital contributed by investors: "))

    # Input hurdles
    hurdles = []
    print("\nEnter IRR hurdles as percentages (e.g., 8 for 8%). Type 'done' when finished.")
    while True:
        hurdle = input("Enter an IRR hurdle (or 'done' to finish): ").strip()
        if hurdle.lower() == "done":
            break
        try:
            hurdles.append(float(hurdle) / 100)  # Convert to decimal
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Input splits
    splits = []
    print("\nEnter split ratios for each hurdle (e.g., '80,20' for 80% to investors, 20% to sponsor).")
    for i in range(len(hurdles)):
        while True:
            split = input(f"Enter split for Tier {i+1} (Hurdle: {hurdles[i]*100:.1f}%): ").strip()
            try:
                split_values = tuple(map(float, split.split(",")))
                if len(split_values) == 2 and sum(split_values) == 100:
                    splits.append(split_values)
                    break
                else:
                    print("Invalid split. Ensure two numbers add up to 100.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma (e.g., '80,20').")

    # Perform calculation
    results = calculate_irr_hurdle_distribution(total_cash_flow, capital_contributed, hurdles, splits)

    # Display results
    print("\nWaterfall Distribution Results:")
    for tier, amounts in results.items():
        print(f"{tier}: Investor = ${amounts['Investor']:.2f}, Sponsor = ${amounts['Sponsor']:.2f}")


# Run the program
if __name__ == "__main__":
    main()      