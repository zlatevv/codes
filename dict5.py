input_symbols = input().split(", ")
symbol_dict = {}
for symbol in input_symbols:
    if symbol:
        symbol_dict[symbol] = ord(symbol)
print(symbol_dict)
