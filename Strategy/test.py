import json

with open(r"C:\Users\Tapan\Documents\testnet_bybit bot\1_price_list.json") as json_file:
    price_data = json.load(json_file)
price_values = price_data['ETHUSDT']

print(price_values['result'])