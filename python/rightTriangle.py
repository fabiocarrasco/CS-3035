import sys
import math

class RightTriangle:
	def __init__(self, sideA,sideB,hypotenuse = None):
		if hypotenuse == None:
			try:  
				self.sideA = float(sideA)
				self.sideB = float(sideB)
				self.hypotenuse = math.sqrt(math.pow(self.sideA,2) + math.pow(self.sideB,2))
			except: 
				raise Exception ("Error: sides are not numbers")
			if self.sideA <= 0 or self.sideB <= 0: 
				raise Exception ("Error: both sides must be nonnegative")
		else:
			try:  
				self.sideA = float(sideA)
				self.sideB = float(sideB)
				self.hypotenuse = float(hypotenuse)
			except: 
				raise Exception ("Error: sides are not numbers")
			if self.sideA <= 0 or self.sideB <= 0 or self.hypotenuse<=0: 
				raise Exception ("Error: both sides and the hypotenuse must be nonnegative")
			if abs(self.hypotenuse - math.sqrt(math.pow(self.sideA,2) + math.pow(self.sideB,2))) > .00001:
				raise Exception ("Error: not a valid pythagorean triple")
	def __eq__(self, other):
		if abs(other.hypotenuse - self.hypotenuse) < .00001:
			return True
		else:
			return False
	def __str__ (self):
		return "Right Triangle with side a = "+ str(self.sideA)+", side b = "+str(self.sideB)+", and hypotenuse = "+str(self.hypotenuse)

result1 = None
result2 = None
while result1 == None and result2 == None:
	a1 = input("Enter a nonegative numeric value for side A for rectangle 1: ")
	b1 = input("Enter a nonegative numeric value for side B for rectangle 1: ")
	try:
		r1 = RightTriangle(a1,b1)
		print(r1)
	except Exception as e:
		print(e)
	a2 = input("Enter a nonegative numeric value for side A on rectangle 2: ")
	b2 = input("Enter a nonegative numeric value for side B on rectangle 2: ")
	hyp = input("Enter a nonegative numeric value for hyptoneuse on rectangle 2: ")
	try:
		r2 = RightTriangle(a2,b2,hyp)
		print(r2)
	except Exception as e:
		print(e)
	try:
		result1 = (str(r1 == r2))
	except Exception as e:
		print(e)
	try:
		result2 = (str(r2 == r1))
	except Exception as e:
		print(e)

print(result1)
print(result2)
