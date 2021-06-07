file_value=open("sample.txt",'r')
a=file_value.read()
print(a)
my_str="அகர முதல எழுத்தெல்லாம் ஆதி "
words=[word.lower()for word in my_str.split()]
words.sort()
print("the sorted words are:")
for word in words:
	print(word)
sentence="அகர முதல எழுத்தெல்லாம் ஆதி .".split()
N=2
grams=[sentence[i:i+N] for i in range(len(sentence)-N+1)]
for gram in grams:
	print(gram)
sentence="அகர முதல எழுத்தெல்லாம் ஆதி.".split()
N=3
grams=[sentence[i:i+N]for i in range(len(sentence)-N+1)]
for gram in grams:
	print(gram)
	
