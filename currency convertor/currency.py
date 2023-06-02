currencies = {
    "USD": 1,
    "EUR": 0.91,
    "GBP": 0.81,
    "JPY": 120,
    "CAD": 1.25,
    "INR": 74,
}

def convert_currency(amount, from_currency, to_currency):
    """
    Convert a currency amount from one currency to another.

    Args:
        amount (float): The amount to convert.
        from_currency (str): The currency to convert from.
        to_currency (str): The currency to convert to.

    Returns:
        float: The converted amount.
    """

    exchange_rate = currencies[to_currency] / currencies[from_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == "__main__":
    # Get the amount and currencies from the user
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from: ")
    to_currency = input("Enter the currency to convert to: ")

    # Convert the currency
    converted_amount = convert_currency(amount, from_currency, to_currency)

    # Print the converted amount
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")