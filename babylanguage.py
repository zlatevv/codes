n = int(input())
words = []
for i in range(n):
    a = input().split()
    words.extend(a)
unique = set(words)
for word in unique:
    print(word)