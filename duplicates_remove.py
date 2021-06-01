a=[3,7,8,3,11,9,7]
for i in range(0,len(a)):
	for j in range(i+1,len(a)-1):
		if a[i]==a[j]:
			a.remove(a[j])
print(a)
