# example of a dynamic array implementation in Python
class DynamicArray:
    
    def __init__(self, capacity: int):
        # Initialize the dynamic array with a given capacity
        self.capacity = capacity     # total number of slots allocated in the underlying fixed-size array
        self.size = 0                # number of valid elements curreltly stored in the dynamic array
        self.array = [0] * capacity  # allocated fixed space

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # Add an element n to the end of the dynamic array
        # this resizes the array if the current size is equal to the capacity
        # and then adds the element n to the end of the array and increments the size
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Remove and return the last element of the dynamic array
        self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity