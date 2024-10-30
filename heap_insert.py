class Heap():
    def __init__(self,max_size):
        self.heap= [0] * (max_size+1)
        self.size =0
    
    def compare(self,a,b) ->bool:
        return b  >  a
    
    def swap(self,idx1,idx2):
        self.heap[idx1],self.heap[idx2] = self.heap[idx2],self.heap[idx1]
    
    def insert(self,data:int)-> None:
        # Increase the size of the heap
        self.size+=1

        # Insert the data at the last of the heap at the given self.size
        self.heap[self.size] = data

        idx = self.size
        while idx>1:
            parent = idx //2
            if self.compare(self.heap[parent],self.heap[idx]):
                self.swap(parent,idx)
                idx=parent
            else:
                break
    
    def heapify(self,val)-> None:
        idx=val
        while 2*idx <=self.size:
            largest=idx
            left = 2*idx
            right = 2*idx+1
            if self.compare(self.heap[idx],self.heap[left]):
                largest=idx

            if right <= self.size and self.compare(self.heap[largest],self.heap[right]):
                largest=right

            if largest ==idx:
                break
            self.swap(largest,idx)
            idx=largest

    def remove(self):
        if self.size == 0:
            return None
        self.swap(1,self.size)
        max_value = self.heap[self.size]
        self.size-=1
        self.heapify(1)
        return max_value 
    

    def print_heap(self):
        for x in range(1, self.size + 1):
            parent = self.heap[x // 2] if x > 1 else "None"
            left_child = self.heap[2 * x] if 2 * x <= self.size else "None"
            right_child = self.heap[2 * x + 1] if 2 * x + 1 <= self.size else "None"
            print(f"Index: {x}, Value: {self.heap[x]}, Parent: {parent} --> Left Child: {left_child}, Right Child: {right_child}")
        print()


if __name__ == "__main__":

    heap1 = Heap(10)

    heap1.insert(10)
    heap1.insert(20)
    heap1.insert(30)
    heap1.insert(40)
    heap1.insert(50)
    heap1.insert(60)
    print("Greates form the heap"+str(heap1.remove()))
    heap1.print_heap()

