import warnings
warnings.simplefilter(action='ignore', category='FutureWarning')
from get_symbols import get_tradeable_symbols
from prices_json import store_price_history
from cointegration import get_cointegrated_pairs
from plot_trends import plot_trends
import json
import pandas as pd

#STRATEGY CODE

if __name__ == "__main__":
    # #Step 1 - Get list of symbols
    # print("Getting Symbols")
    # sym_response = get_tradeable_symbols()
    #
    # #STEP 2 - Construct and save price history
    # print("Constructing and saving price data to JSON...")
    # if len(sym_response) > 0:
    #     store_price_history(sym_response)

    # #STEP 3 - FIND COINTEGRATED PAIRS
    # print("Calculating co-integration...")
    # with open("1_price_list.json") as json_file:
    #     price_data = json.load(json_file)
    #     if len(price_data) > 0:
    #         coint_pairs = get_cointegrated_pairs(price_data)

    #STEP 4 - Plot trends and save for backtesting
    print("Plotting Trends")
    symbol_1 = "NEOUSDT"
    symbol_2 = "AKROUSDT"
    with open(r"C:\Users\Tapan\Documents\testnet_bybit bot\1_price_list.json", "r") as json_file:
        price_data = json.load(json_file)
        if len(price_data) > 0:
            plot_trends(symbol_1, symbol_2, price_data)
