from collections import deque 
class treenode():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

import queue

def takeinput():
    q=queue.Queue()
    inputdata = int(input())
    if (inputdata ==-1):
        return None
    root=treenode(inputdata)
    q.put(root)
    while (not(q.empty())):
           curr_node=q.get()
           print("Enter the new left Node for ",curr_node.data)
           left_child=int(input())
           if left_child !=-1:
               leftdata = treenode(left_child)
               curr_node.left=leftdata
               q.put(leftdata)

           print("Enter the new right Node for ",curr_node.data)
           right_child=int(input())
           if right_child !=-1:
               rightdata = treenode(right_child)
               curr_node.right=rightdata
               q.put(rightdata)
    return root
           
def printLevelWise(root):
    if root is None:
        return
    
    q = deque([root])
    
    while q:
        current_node = q.popleft()
        
        # Get the left and right child data, or 'None' if no child exists
        left_data = current_node.left.data if current_node.left else "None"
        right_data = current_node.right.data if current_node.right else "None"
        
        # Print the current node's data along with its left and right children
        print(f"Node: {current_node.data}, Left Child: {left_data}, Right Child: {right_data}")
        
        if current_node.left:
            q.append(current_node.left)

        if current_node.right:
            q.append(current_node.right)

root = takeinput()
print("Level-wise traversal of the constructed tree:")
printLevelWise(root)

    
