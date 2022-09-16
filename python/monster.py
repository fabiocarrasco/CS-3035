import sys

class Monster:
	def __init__(self, name, size):
		self._name = name
		self._size = size
	def attack(self, location):
		print(str(self._name)+" attacks "+str(location))
	def get_name(self):
		return self._name
	def get_size(self):
		return self._size
	def __str__(self):
		return 'The name of the monster is '+ str(self._name) + ' with a size of ' + str(self._size) + '.'
	def __eq__ (self, other):
		if((self._name == other._name) and (self._size == other._size)):
			return True
		else:
			return False
	def __add__(self, other):
		return Monster(self._name + other._name, self._size + other._size)
