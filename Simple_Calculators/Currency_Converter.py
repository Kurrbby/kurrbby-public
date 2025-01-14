import requests

def fetch_exchange_rates(base_currency="USD"):
    """
    Fetches current exchange rates dynamically from an API.
    
    Parameters:
        base_currency (str): The base currency for the rates (default is "USD").
    
    Returns:
        dict: A dictionary of exchange rates with currency codes as keys.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates. Please check your internet connection or try again later.")
    
    data = response.json()
    return data["rates"]

def currency_converter_dynamic(amount, from_currency, to_currency, rates):
    """
    Converts an amount from one currency to another using dynamic exchange rates.
    
    Parameters:
        amount (float): The amount in the source currency.
        from_currency (str): The source currency code (e.g., "USD").
        to_currency (str): The target currency code (e.g., "EUR").
        rates (dict): A dictionary of exchange rates with currency codes as keys.
    
    Returns:
        float: The converted amount in the target currency.
    """
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code.")
    
    # Convert to base currency (e.g., USD) and then to target currency
    base_amount = amount / rates[from_currency]
    converted_amount = base_amount * rates[to_currency]
    return converted_amount


def main():
    print("Dynamic Currency Converter")

    # Fetch the latest exchange rates
    print("Fetching current exchange rates...")
    try:
        exchange_rates = fetch_exchange_rates()
        print("Available currencies:", ", ".join(exchange_rates.keys()))
    except Exception as e:
        print(f"Error: {e}")
        return

    # Get user input
    from_currency = input("Enter the source currency code: ").strip().upper()
    to_currency = input("Enter the target currency code: ").strip().upper()
    try:
        amount = float(input(f"Enter the amount in {from_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    try:
        # Perform the conversion
        converted_amount = currency_converter_dynamic(amount, from_currency, to_currency, exchange_rates)
        print(f"\n{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(f"Error: {e}")


# Run the program
if __name__ == "__main__":
    main()
