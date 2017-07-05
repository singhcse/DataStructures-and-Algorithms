def Fib(n):
	a,b=0,1
	result=[0,]
	while(b<n):
		result.append(b)
		a,b=b,b+a
	
	print(result)
	
	return	


Fib(4)
print('\n')
Fib(7)
