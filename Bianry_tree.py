class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def detailtree(root):
    if root is None:
        return
    print(root.data, end=": ")
    if root.left is not None:
        print("L", root.left.data, end=", ")
    if root.right is not None:
        print("R", root.right.data, end="")
    print()
    detailtree(root.left)
    detailtree(root.right)
    
    
def print_post_order(root):
    if root is None:
        return 
    print_post_order(root.left)
    print_post_order(root.right)
    print(root.data,end="")

def inputdata():
    input_data = int(input("Enter the data: "))
    if input_data == -1:
        return None
    root = BinaryTree(input_data)
    left_tree = inputdata()
    right_tree = inputdata()
    root.left = left_tree
    root.right = right_tree
    return root

def getsum_node(root):
    if root is None:
        return 0
    left_count = getsum_node(root.left)
    right_count = getsum_node(root.right)
    return left_count + right_count + root.data

def num_node(root):
    if root is None:
        return 0
    left_count = num_node(root.left)
    right_count = num_node(root.right)
    return left_count + right_count +1

def printgreater(root,x):
    count=0
    if root is None:
        return 0
    if root.data>=x:
        count=1
    count+=printgreater(root.left,x)
    count+=printgreater(root.right,x)
    return count

def height(root):
    if root is None:
        return 0
    root_left=height(root.right)
    root_right=height(root.left)
    return max(root_left,root_right)+1

def changeToDepthTree(root,depth=0) :
    if root is None:
        return
    # Change the current node's data to its depth
    root.data=depth
    # Recursively change the left and right subtrees
    changeToDepthTree(root.left, depth +1)
    changeToDepthTree(root.right, depth + 1)
    




##Make the tree roots
##
##
##
##btn1=BinaryTree(1)
##btn2=BinaryTree(2)
##btn3=BinaryTree(3)
##btn4=BinaryTree(4)
##btn5=BinaryTree(5)
##btn6=BinaryTree(6)
##
##
##
##Make a joint
##
##
##btn1.left=btn2
##btn1.right=btn3
##btn2.right=btn4
##btn2.left=btn5
##btn3.right=btn6


root=inputdata()
print(detailtree(root)) 
##detailtree(root)
##print(num_node(root))
##print(getsum_node(root))
##print(print_post_order(root))
##print(printgreater(root,1))
##print(height(root))
changeToDepthTree(root)
print("After the cahnge")
print(detailtree(root))          

    
