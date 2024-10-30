## Queue

class Node:
    def __init__(self,data):
        self.data=date
        self.nex=None

class queue:
    def __init__(self):
        self.__arr=[]
        self.__count=0
        self.__front=0

    def isempty(self):
        if self.__count==0:
            return True
        return False
##
    def issize(self):
        if self.__count==0:
            return 0
        return self.__count
    

    def enQueue(self,item):
        self.__arr.append(item)
        self.__count+=1

    def dequeue(self):
        if self.__count==0:
            return -1

        ele = self.__arr[self.__front]
        self.__front+=1
        self.__count-=1
        return ele
    def front(self):
        if self.__count==0:
            return -1
        return self.__arr[self.__front]

q=queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
while (q.isempty()is False):
    print(q.front())
##    q.dequeue()
print(q.dequeue())

        
 
