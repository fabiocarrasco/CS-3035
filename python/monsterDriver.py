import sys
from monster import Monster

def main():
	monA = Monster("Godzilla",100)
	monA.attack("Italy")
	str(monA)
	print(str(monA.get_name()))
	print(str(monA.get_size()))
	monB = Monster("Godzilla",100)
	print("Comparing MonsterA with MonsterB: "+str(monA == monB))
	monC = Monster("Cthulu",100)
	print("Comparing MonsterA with MonsterC: "+str(monA == monC))
	monD = monA + monC
	print(str(monD))
	
if __name__ == "__main__":
    sys.exit(main())
