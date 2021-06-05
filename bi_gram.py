sentence="iam geetha,from villupuram city.".split()
N=2
grams=[sentence[i:i+N] for i in range(len(sentence)-N+1)]
for gram in grams:
	print(gram)
