def prim(n):
	if n==1:
		return False
	elif n==2 :
		return True
	elif  n==3 :
		return True
	elif n%2==0 :
		return False
	else :
		for i in range(3,n//2):
			if n%i==0 :
				return False
		return True

n=int(input("Enter an integer : "))
if prim(n)==True :
	print("Prim")
else :
	print("Nu e prim")

#problema 11 tema 