def kelly_criterion_gambling(probability, odds):
    """
    Calculates the Kelly Criterion for gambling.
    
    Parameters:
        probability (float): Probability of winning (0 < p <= 1).
        odds (float): Decimal odds (e.g., 3 for 3-to-1 odds).
    
    Returns:
        float: Optimal fraction of capital to wager.
    """
    if not (0 < probability <= 1):
        raise ValueError("Probability must be between 0 and 1.")
    if odds <= 0:
        raise ValueError("Odds must be greater than 0.")
    
    q = 1 - probability
    kelly_fraction = (odds * probability - q) / odds
    return max(kelly_fraction, 0)  # Ensure non-negative result


def kelly_criterion_investing(expected_return, risk_free_rate, variance):
    """
    Calculates the Kelly Criterion for investing.
    
    Parameters:
        expected_return (float): Expected return of the investment (annualized).
        risk_free_rate (float): Risk-free rate of return (annualized).
        variance (float): Variance of the investment returns (annualized).
    
    Returns:
        float: Optimal fraction of capital to allocate.
    """
    excess_return = expected_return - risk_free_rate
    if variance <= 0:
        raise ValueError("Variance must be greater than 0.")
    
    kelly_fraction = excess_return / variance
    return max(kelly_fraction, 0)  # Ensure non-negative result


# Main function for user interaction
def main():
    print("Kelly Criterion Calculator")
    print("Choose a mode:")
    print("1. Gambling")
    print("2. Investing")
    mode = input("Enter 1 or 2: ").strip()

    if mode == "1":
        print("\n--- Gambling Mode ---")
        p = float(input("Enter the probability of winning (0 < p <= 1): "))
        odds = float(input("Enter the decimal odds (e.g., 3 for 3-to-1 odds): "))
        kelly_fraction = kelly_criterion_gambling(p, odds)
        print(f"\nOptimal fraction of capital to wager: {kelly_fraction:.4f}")
    elif mode == "2":
        print("\n--- Investing Mode ---")
        expected_return = float(input("Enter the expected return (as a decimal, e.g., 0.08 for 8%): "))
        risk_free_rate = float(input("Enter the risk-free rate (as a decimal, e.g., 0.02 for 2%): "))
        variance = float(input("Enter the variance of returns (e.g., 0.04 for 4% variance): "))
        kelly_fraction = kelly_criterion_investing(expected_return, risk_free_rate, variance)
        print(f"\nOptimal fraction of capital to allocate: {kelly_fraction:.4f}")
    else:
        print("Invalid choice. Please restart and select a valid mode.")

# Run the program
if __name__ == "__main__":
    main()