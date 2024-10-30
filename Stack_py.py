class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.__count=0
        self.__head=None
        self.__tail=None

    def isempty(self):
        if  self.__count==0:
            return True
        return False
    
    def ISsize(self):
        if  self.__count==0:
            return("Hey it's empty")
        return self.__count

    def push(self,item):
        newnode=Node(item)
        if self.__count==0:
           self.__head=newnode
           self.__tail=newnode
        else:
            self.__tail.next=newnode
            self.__tail=newnode
        self.__count+=1

    def pop(self):
        if self.__count==0:
            return None
        if self.__count==1:
            data_pop=self.__head.data
            self.__head=None
            self.__tail=None
        else:
            temp=self.__head
            while temp.next!=self.__tail:
                temp=temp.next
            popped_data=self.__tail.data
            self.__tail=temp
            self.__tail=None
        self.__count+=1
        return poopped_data
        
            
    def top(self):
        if self.__count==0:
            return None
        return self.__tail.data
            

stack=Stack()

stack.push(19)
stack.push(20)
stack.push(21)
print("Current size of stack:", stack.ISsize())
print("ISempoty",stack.isempty())

      
