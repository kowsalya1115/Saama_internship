class sample:
	def __init__(self,a,b): #constructor
		self.a=a
		self.b=b
		print(self.a+self.b)
	def stringop(self,s):
		self.s=s
		c=""
		for i in self.s:
			c=i+c
		return c		

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
x=sample(num1,num2)
print(x.stringop("python"))
print(x.a+x.b)
