import sys
def conv_cel_to_fahr(tempC):
	tempF = (tempC * 9.0/5.0) + 32
	return tempF
	
def main():
	min_temp = int(input('Enter the minimum temperature: '))
	max_temp = int(input('Enter the maximum temperature: '))
	print("Celsius	Fahrenheit")
	for tempC in range(min_temp,max_temp+1):
		tempF = conv_cel_to_fahr(tempC)
		print(str(tempC)+"	"+str(tempF))

if __name__ == "__main__":
    sys.exit(main())
