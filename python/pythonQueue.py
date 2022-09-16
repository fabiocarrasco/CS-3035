import sys

def main():
    pq = PQ()
    pq.add(2, "Eat")
    pq.add(0, "Study for CS 3035")
    pq.add(3, "Sleep")
    pq.add(1, "Maintain Personal Relationships")
    pq.add(4, "Practice Good Personal Hygiene")
    pq.set_priority("Practice Good Personal Hygiene", 2)
    pq.set_priority("Eat", 4)
    print(str(pq.size()))
    while pq.size() > 0:
        print(pq.remove_min())

class QueueEntry:
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value
    def set_priority(self,priority):
        self.priority = priority
    def get_priority(self):
        return self.priority
    def get_value(self):
        return self.value
    def __str__(self):
        return "Priority: " + str(self.priority) + " Value: " + str(self.value)
class PQ:
	def __init__(self):
		self.queue=[]
	def add(self,priority,value):
		self.queue.append(QueueEntry(priority, value))
	def remove_min(self):
		min = 0
		for i in range(len(self.queue)):
			if self.queue[i].get_priority() < self.queue[min].get_priority():
				min = i
		minQueue = self.queue[i]
		del self.queue[i]
		return minQueue
		
		return minimum
	def set_priority(self,value,new_priority):
		for i in self.queue:
			if i.get_value() == value:
				i.set_priority(new_priority)
	def size(self):
		return len(self.queue)
if __name__ == "__main__":
	sys.exit(main())
