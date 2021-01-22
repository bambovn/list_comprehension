data = input().split("|")[::-1]
#data.reverse()
 
result = [value.strip() for i in range(len(data)) for value in data[i].split()]
print(*result)