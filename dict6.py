names = input().split()
word = {}
for words in names:
    lowercase = words.lower()
    if lowercase in word:
        word[lowercase] += 1
    else:
        word[lowercase] = 1
repeat = []
for w, c in word.items():
    if c > 1:
        repeat.append(w)
print(*repeat, sep = " ")
