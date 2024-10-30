class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.skt1=[]
        self.skt2=[]

    def enqueue(self,x):
        self.skt1.append(x)
        return True
    
    def dequeue(self):
        if not self.skt2:
            while self.skt1:
                self.skt2.append(self.skt1.pop())
                
        if self.skt2:
            return self.skt2.pop()
        else:
            return -1

def process_queries(queries):
    q = Queue()
    result = []
    
    for query in queries:
        # Split the query to identify type
        query = query.split()
        q_type = int(query[0])

        # If query is of type 1 (Enqueue)
        if q_type == 1:
            x = int(query[1])
            q.enqueue(x)
            result.append(True)  # Add True after enqueueing
        
        # If query is of type 2 (Dequeue)
        elif q_type == 2:
            result.append(q.dequeue())  # Add dequeued element or -1 if queue is empty
    
    return result

# Sample driver code
if __name__ == "__main__":
    # Input number of queries
    Q = int(input("Enter number of queries: "))
    
    queries = []
    for _ in range(Q):
        queries.append(input())  # Input each query

    # Process queries and get results
    results = process_queries(queries)
    
    # Print results for dequeue operations
    for res in results:
        if isinstance(res, bool):
            continue  # Skip True values for enqueue, print only dequeue results
        print(res)
