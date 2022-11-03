#API Imports
from pybit import HTTP
from pybit import WebSocket
#CONFIG
mode = "test" #test or production
timeframe = 60
kline_limit = 200
z_score_window = 40

#LIVE API
api_key_mainnet = ""
api_secret_mainnet = ""

#TEST API
api_key_testnet = "iLvhQNx9AWxJ8cs1zP"
api_secret_testnet = "ECIMfwx4TT8CoenkkbTGxsxU2BHQ48ZuyUig"


#SELECT API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

#SELECTED URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"

#SESSION ACTIVATION
session = HTTP(api_url)

#WEB SOCKET CONNECTION
# subs = [
#     "candle.1.BTCUSDT"
# ]
#
# ws = WebSocket(
#     "wss://stream-testnet.bybit.com/realtime_public",
#     subscriptions = subs
# )
#
# while True:
#     data = ws.fetch(subs[0])
#
#     if data:
#         print(data)
#     else :
#         print("No Data")