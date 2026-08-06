class DynamicArray:
    
    def __init__(self, capacity: int):
        self.num_elements = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]
        
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.num_elements == self.capacity:
            self.resize()

        self.arr[self.num_elements] = n
        self.num_elements += 1

    def popback(self) -> int:
        if self.num_elements > 0:
            self.num_elements -= 1
        
        return self.arr[self.num_elements]

 

    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity 
        
        # Copy elements to new_arr
        for i in range(self.num_elements):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.num_elements
        
    
    def getCapacity(self) -> int:
        return self.capacity
