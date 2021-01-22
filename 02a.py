#2. Words Lengths
words = input().split(", ")
print(*[f"{word} -> {len(word)}" for word in words], sep=", ")