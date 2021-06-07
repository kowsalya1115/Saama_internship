def letter_frequency(value):
	b={}
	for i in value:
		k=b.keys()
		if i in k:
			b[i]=b[i]+1
		else:
			b[i]=1
	for k,v in b.items():
		print(k,v)

def word_frequency(value):
	text=value.lower()
	skips=[".",",",":","'",'"']
	for i in skips:
		text=text.replace(i,"")
	new_text=text.split(" ")
	word_count={}
	for i in new_text:
		if i in word_count:
			word_count[i]=word_count[i]+1
		else:
			word_count[i]=1
	print(word_count)

def sort_word(value):
	words=[word.lower()for word in value.split()]
	words.sort()
	for word in words:
		print(word)
def find_grams(value):
	n=int(input("Enter the number of grams:"))
	sentence=value.split()
	grams=[sentence[i:i+n] for i in range(len(sentence)-n+1)]
	for gram in grams:
		print(gram)

file_value=open("tamil_word.txt",'r')
a=file_value.read()
letter_frequency(a)
word_frequency(a)
sort_word(a)
find_grams(a)

