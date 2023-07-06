symbols = [ch for ch in input() if ch != " "]
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for ch, occ in letters.items():
    print(f"{ch} -> {occ}")