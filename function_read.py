def
skips=[".",",",":","'",'"']
for i in skips:
	text=text.replace(i,"")
print(text)
new_text=text.split(" ")
print(new_text)
word_count={}
for i in new_text:
	if i in word_count:
		word_count[i]=word_count[i]+1
	else:
		word_count[i]=1
print(word_count)