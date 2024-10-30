####LINKED LIST
##
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

##def printll(head):
##    c=0
##    while head is  not None:
##        print(str(head.data)+"->",end=" ")
##        head=head.next
##        c+=1
##    print("heyne")
##    print(c)
##def inputlist():
##
##    list_linked=[int(ele) for ele in input().split()]
##    head=None
##    for currdata in list_linked:
##        if currdata==-1:
##            break
##
##        newnode=Node(currdata)
##        if head is None:
##            head = newnode
##        else:
##            curr=head
##            while curr.next is not None:
##                curr=curr.next
##            curr.next=newnode
##    return head
##head=inputlist()
##printll(head)


def printIthNode(head, i):
    #Your code goes here
   
    index = 0
    
    # Traverse the linked list to find the ith node
    while head is not None:
        if index == i:
            print(head.data)  # Print the data at the ith position
            return
        head = head.next
        index += 1
    
list=[1,2,3,6,7,8]
i=0
printIthNode(list,i)
