sentence="i love india,its very beautyful.".split()
N=3
grams=[sentence[i:i+N]for i in range(len(sentence)-N+1)]
for gram in grams:
	print(gram)
	
