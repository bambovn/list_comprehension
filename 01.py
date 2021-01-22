#1. Word Filter
words = input().split()

even_words_lenght = [word for word in words if len(word) %2 ==0]

print(*even_words_lenght, sep='\n')
