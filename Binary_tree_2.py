
import queue

class Binary_tree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

import queue
def takeinput():
    
    inputdata=int(input("enter the value")).split()
    q=queue.Queue()
    if inputdata ==-1:
        return None
    root=Binary_tree(inputdata)
    q.put(root)
    while(not (q.empty())):
        curr_node=q.get()
        print("left node for left chiild of ",curr_node.data)
        if leftchild!=-1:
            leftroot=Binary_tree(inputdata)
            curr_node.left=leftroot
            q.put(leftroot)
        
        print("right node for left chiild of ",curr_node.data)
        if rightchild!=-1:
            rightchild=Binary_tree(inputdata)
            curr_node.right=leftroot
            q.put(rightchild)
    return root
            

    
    
    

root = takeinput()
print("Level-wise traversal of the constructed tree:")
##printLevelWise(root)
