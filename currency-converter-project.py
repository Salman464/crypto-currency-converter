import requests

import requests

class RealTimeCurrencyConverter():
  def __init__(self, url_fiat, url_crypto, api_key):
    self.fiat_data = requests.get(url_fiat).json()
    self.fiat_currencies = self.fiat_data['rates']
    
    self.crypto_data = requests.get(url_crypto, headers={'X-CMC_PRO_API_KEY': api_key}).json()
    self.crypto_symbols = {crypto['symbol'].upper(): crypto['id'] for crypto in self.crypto_data.get('data', [])}

  def convert(self, from_currency, to_currency, amount):
    if from_currency in self.fiat_currencies and to_currency in self.fiat_currencies:
        # Fiat to Fiat conversion
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.fiat_currencies[from_currency]

        # Limiting the precision to 4 decimal places 
        amount = round(amount * self.fiat_currencies[to_currency], 4)
        return amount

    elif from_currency in self.crypto_symbols and to_currency in self.crypto_symbols:
        # Cryptocurrency to Cryptocurrency conversion
        from_symbol = self.crypto_symbols[from_currency]
        to_symbol = self.crypto_symbols[to_currency]

        conversion_rate = self.get_crypto_conversion_rate(from_symbol, to_symbol)
        if conversion_rate is not None:
            converted_amount = amount * conversion_rate
            return converted_amount
        else:
            return "Invalid cryptocurrency pair. Please check your inputs."

    else:
        return "Invalid currency pair. Please check your inputs."

def get_price(api_key, from_currency, to_currency):
    url = f'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
    parameters = {
        'amount': 1,
        'symbol': from_currency,
        'convert': to_currency,
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    if response.status_code == 200:
        return data['data']['quote'][to_currency]['price']
    else:
        print(f"Error: {data['status']['error_message']}")
        return None

def main():
    api_key = '4f5371d4-9976-46cb-8edb-e48fd57e0644'

    print('------------------------Welcome to real-time Crypto Exchange-----------------------------')
    print('\n\n')
    from_currency = input("Enter the FROM currency / cryptocurrency symbol (e.g., BTC, ETH, INR, USD): ").upper()
    to_currency = input("Enter the TO currency / cryptocurrency symbol (e.g., BTC, ETH, INR, USD): ").upper()
    amount = float(input("Enter the amount to convert: "))

    price = get_price(api_key, from_currency, to_currency)

    print('\n')

    if price is not None:
        result = amount * price
        print(f"{amount} {from_currency} is equal to: {round(result, 6)} {to_currency}")
    print('\n\n')
    print('-----------------------------------------------------------------------------------------')
if __name__ == "__main__":
    main()
