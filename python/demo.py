def divide(x, y):
	result = None
	try:  
		x = float(x)
		y = float(y)
	except: 
		raise Exception ("Divisor and dividend must be numbers!")
	if float(y) == 0: 
		raise Exception("Can't divide by zero!")
	else: 
		result = float(x) / float(y)
	return result 
result = None
while result == None:
	x = input("Please enter a dividend: ");
	y = input("Please enter a divisor: ");
	try: 
		result = (str(divide(x, y)))
	except Exception as e:
			print(e)
print(result)
