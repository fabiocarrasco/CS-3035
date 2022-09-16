import sys

def ammntLetters(data):
	counter = 0
	if(len(data)==0):
		return counter
	counter+=1
	return counter + ammntLetters(data[1:])
	
def reverseString(data):
	if(len(data) ==0):
		return ""
	return reverseString(data[1:])+data[0]
	
def isPalindrome(data):
	if(len(data) <1):
		return True
	if(data[0].isalpha() and data[-1].isalpha()):
		return data[0].lower() == data[-1].lower() and isPalindrome(data[1:-1])
	else:
		if(not data[0].isalpha()):
			return True and isPalindrome(data[1:])
		elif(not data[-1].isalpha()):
			return True and isPalindrome(data[:-1])
		else:
			return True and isPalindrome(data[1:-1])

def main():
	data = input('Enter a string: ')
	numOfLetters = ammntLetters(data)
	print(numOfLetters)
	print(reverseString(data))
	print(isPalindrome(data))

if __name__ == "__main__":
	sys.exit(main())
