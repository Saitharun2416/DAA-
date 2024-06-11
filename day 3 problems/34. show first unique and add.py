from collections import deque, defaultdict

class FirstUnique:
    def __init__(self, nums):
        self.queue = deque()
        self.counts = defaultdict(int)
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        while self.queue and self.counts[self.queue[0]] > 1:
            self.queue.popleft()

            return self.queue[0] if self.queue else -1

    def add(self, value):
        self.counts[value] += 1
        if self.counts[value] == 1:
            self.queue.append(value)
firstUnique = FirstUnique([2, 3, 5])
print(firstUnique.showFirstUnique())  
firstUnique.add(5)
print(firstUnique.showFirstUnique())  
firstUnique.add(2)
print(firstUnique.showFirstUnique())  
firstUnique.add(3)
print(firstUnique.showFirstUnique())  

firstUnique = FirstUnique([7, 7, 7, 7, 7, 7])
print(firstUnique.showFirstUnique())  
firstUnique.add(7)
firstUnique.add(3)
firstUnique.add(3)
firstUnique.add(7)
firstUnique.add(17)
print(firstUnique.showFirstUnique())  

firstUnique = FirstUnique([809])
print(firstUnique.showFirstUnique())  
firstUnique.add(809)
print(firstUnique.showFirstUnique()) 

