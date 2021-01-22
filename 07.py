#Flatten Lists
result = [[el for el in list_as_string.split()] for list_as_string in input().split('|')[::-1]]

print(*[' '.join(el) for el in result])