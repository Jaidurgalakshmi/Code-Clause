import requests

API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key from exchangerate-api.com
BASE_URL = 'https://v6.exchangerate-api.com/v6/'

def get_exchange_rate(base_currency, target_currency):
    url = f"{BASE_URL}{API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Error fetching exchange rate data")
    
    data = response.json()
    if 'conversion_rates' not in data:
        raise Exception("Invalid response data format")
    
    rates = data['conversion_rates']
    if target_currency not in rates:
        raise Exception(f"Currency {target_currency} not found")
    
    return rates[target_currency]

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    return amount * rate

def main():
    print("Welcome to the Currency Converter")
    amount = int(input("Enter the amount to convert: "))
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    
    try:
        converted_amount = convert_currency(amount, base_currency, target_currency)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
