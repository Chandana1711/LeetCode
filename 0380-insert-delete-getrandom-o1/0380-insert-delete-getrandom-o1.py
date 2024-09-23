
import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index_map = {}
    
    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.values)
        self.values.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        # Get the index of the element to remove
        index = self.index_map[val]
        # Swap the element with the last element
        last_element = self.values[-1]
        self.values[index] = last_element
        self.index_map[last_element] = index
        # Remove the last element
        self.values.pop()
        del self.index_map[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.values)



        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()