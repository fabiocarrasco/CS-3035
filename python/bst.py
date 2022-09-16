'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

public static <T extends Comparable<T>> int iterativeBinarySearch(List<T> list, T key) {
        if(list.size() < 1) return -1;
        int low = 0;
        int high = list.size() - 1;
        System.out.println("Searching " + list + " for " + key);
        while (low <= high) {
            System.out.println("Comparing " + key + " and " +list.get(high));
            int mid = (low + high) / 2;
            if (list.get(mid).equals(key))
                return mid;
            if (list.get(mid).compareTo(key) < 0) // key is later in the sort order than the value at mid
                low = mid + 1;
            else
                high = mid - 1;
        }

        return -1;
    }

'''
import sys
def iterativeBinarySearch(searchedList, key):
	if len(searchedList) < 1: 
		return -1
	low = 0
	high = len(searchedList) -1
	print("Searching " + str(searchedList)+" for "+str(key))
	while low <= high:
		mid = (low+high)/2
		print("Comparing "+ str(key)+" and "+str(searchedList[int(mid)]))
		if searchedList[int(mid)] == key:
			return mid
		if searchedList[int(mid)] < key:
			low = mid + 1
		else:
			high = mid - 1
	return -1

def main():
    fruits = [1,2,3,4,5,6]
    key = 5
    print(iterativeBinarySearch(fruits,key))
    
if __name__ == "__main__":
    sys.exit(main())

