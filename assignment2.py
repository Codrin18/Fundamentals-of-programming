def Suma(n):
	s = 0
	for i in range(n):
		if i % 2==0 :
			s=s+i
	return s



n = int(input("Enter an integer :"))
print("The sum of even numbers up to " + str(n) + "is" + str(Suma(n)))