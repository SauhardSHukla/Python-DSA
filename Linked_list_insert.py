
##To define the class 
class Node:
    def __init__(self,data):
        self.data= data
        self.next=None
        
##To print the linked list
def printll(head):
    curr= head
    while curr is not None:
        print(str(curr.data) + "->",end=" ")
        curr=curr.next
    print("None")

##To take the input
def inputlist():
    takelist=[int(ele)for ele in input().split()]
    head=None
    tail=None
    for curr_data in takelist:
        if curr_data==-1:
            break
        newnode=Node(curr_data)
        if head is None:
            head=newnode
            tail=newnode
        else:
            tail.next=newnode
            tail=newnode
    return head

##Funtion to insert at ith position in the list (iteratively)
##def insertithposition(head,i,data):
##    if i<0:
##        return head
##    curr=head
##    prev=None
##    count=0
##    while count <i:
##        prev=curr
##        curr=curr.next
##        count+=1
##    newnode=Node(data)
##    if count==i:
##        if prev is not None:
##            prev.next=newnode
##        else:
##            head=newnode
##        newnode.next=curr
##    return head
            

##Function to Do recursively
def insertAtIR(head,i,data):
    if i<0:
        return head
    if i==0:
        newnode = Node(data)
        newnode.next=head
        return newnode
    if head is None:
        return None
    smallhead=insertAtIR(head.next,i-1,data)
    head.next=smallhead
    return head
    



head=inputlist()
printll(head)
head=insertAtIR(head,3,0)
printll(head)





