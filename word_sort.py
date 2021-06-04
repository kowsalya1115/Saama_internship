my_str="hello letter in the word"
words=[word.lower()for word in my_str.split()]
words.sort()
print("the sorted words are:")
for word in words:
	print(word)
