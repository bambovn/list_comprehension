result = [' '.join(list_as_string.split()) for list_as_string in input().split('|')[::-1]]

print(*result)