# crypto-currency-converter

A small command-line tool that converts between fiat currencies and cryptocurrencies using live rates from the CoinMarketCap API.

## How it works

The script asks for three things: the currency to convert from, the currency to convert to, and an amount. It requests the current price of one unit of the source currency in the target currency from CoinMarketCap's price-conversion endpoint, multiplies it by your amount, and prints the result.

Any symbol CoinMarketCap supports works on either side, for example `BTC`, `ETH`, `USD`, `INR`.

```
Enter the FROM currency / cryptocurrency symbol (e.g., BTC, ETH, INR, USD): BTC
Enter the TO currency / cryptocurrency symbol (e.g., BTC, ETH, INR, USD): USD
Enter the amount to convert: 0.5
```

## Requirements

- Python 3
- `requests` (`pip install requests`)
- A CoinMarketCap API key (free tier is enough): https://coinmarketcap.com/api/

## Running it

```
git clone https://github.com/Salman464/crypto-currency-converter.git
cd crypto-currency-converter
pip install requests
python3 currency-converter-project.py
```

Before running, set your own API key in `main()` in `currency-converter-project.py`. Don't commit a real key to a public repo.

## Files

- `currency-converter-project.py` - the converter script

## Notes

- Rates come from the API at the moment you run the script, so results change between runs.
- Results are rounded to 6 decimal places.
- If the API returns an error (bad symbol, invalid key, rate limit), the error message is printed and no conversion is shown.
