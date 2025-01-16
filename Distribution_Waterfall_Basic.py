# Distribution Waterfall

def distribution_waterfall(total_cash_flow, capital_contributed, pref_rate, catchup_rate, split_rate):
    """
    Simulates a distribution waterfall for cash flows.

    Parameters:
        total_cash_flow (float): Total cash available for distribution.
        capital_contributed (float): Total capital contributed by investors.
        pref_rate (float): Preferred return rate (as a decimal, e.g., 0.08 for 8%).
        catchup_rate (float): Catch-up rate for the sponsor (as a decimal, e.g., 0.2 for 20%).
        split_rate (tuple): Split of remaining profits (e.g., (0.8, 0.2) for 80% to investors, 20% to sponsor).

    Returns:
        dict: Distribution amounts for each tier.
    """
    distribution = {
        "Return of Capital": 0,
        "Preferred Return": 0,
        "Catch-up": 0,
        "Profit Split (Investor)": 0,
        "Profit Split (Sponsor)": 0,
    }

    remaining_cash = total_cash_flow

    # Tier 1: Return of Capital
    if remaining_cash > 0:
        tier1 = min(remaining_cash, capital_contributed)
        distribution["Return of Capital"] = tier1
        remaining_cash -= tier1

    # Tier 2: Preferred Return
    pref_return = capital_contributed * pref_rate
    if remaining_cash > 0:
        tier2 = min(remaining_cash, pref_return)
        distribution["Preferred Return"] = tier2
        remaining_cash -= tier2

    # Tier 3: Catch-up
    catchup_amount = pref_return * (catchup_rate / (1 - catchup_rate))
    if remaining_cash > 0:
        tier3 = min(remaining_cash, catchup_amount)
        distribution["Catch-up"] = tier3
        remaining_cash -= tier3

    # Tier 4: Profit Sharing
    if remaining_cash > 0:
        distribution["Profit Split (Investor)"] = remaining_cash * split_rate[0]
        distribution["Profit Split (Sponsor)"] = remaining_cash * split_rate[1]
        remaining_cash = 0

    return distribution


# Example Usage
def main():
    print("Distribution Waterfall Model")
    total_cash_flow = float(input("Enter the total cash flow available for distribution: "))
    capital_contributed = float(input("Enter the total capital contributed by investors: "))
    pref_rate = float(input("Enter the preferred return rate (as a decimal, e.g., 0.08 for 8%): "))
    catchup_rate = float(input("Enter the catch-up rate for the sponsor (as a decimal, e.g., 0.2 for 20%): "))
    split_rate = input("Enter the profit split as two percentages (e.g., '80, 20' for 80% to investors, 20% to sponsor): ")
    split_rate = tuple(map(lambda x: float(x) / 100, split_rate.split(",")))

    results = distribution_waterfall(total_cash_flow, capital_contributed, pref_rate, catchup_rate, split_rate)

    print("\nDistribution Waterfall Results:")
    for tier, amount in results.items():
        print(f"{tier}: ${amount:,.2f}")


# Run the program
if __name__ == "__main__":
    main()
