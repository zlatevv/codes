n = input()
characters = {}
for text in n:
    if text in characters:
        characters[text] += 1
    else:
        characters[text] = 1
sorted = sorted(characters.keys())
for text in sorted:
    print(f"'{text}': {characters[text]}")