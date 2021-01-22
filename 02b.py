#2. Words Lengths
d={word:len(word) for word in input().split(', ')}
print(', '.join([str(f'{key} -> {value}')for key, value in d.items()]))