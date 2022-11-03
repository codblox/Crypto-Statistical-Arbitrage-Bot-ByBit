from config_strategy_api import session

#Get Symbols
def get_tradeable_symbols():
    sym_list = []
    symbols = session.query_symbol()
    if "ret_msg" in symbols.keys():
        if symbols["ret_msg"] == "OK":
            symbols=symbols["result"]

    for symbol in symbols:
        if symbol["quote_currency"] == "USDT" and symbol["status"] == "Trading":
            sym_list.append(symbol["name"])

    return sym_list