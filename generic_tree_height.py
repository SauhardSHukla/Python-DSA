import sys
class treeNode:
    def __init__(self,data):
        self.data = data
        self.children=[]


def height(root):
    if root is None:
        return 0
    if  not root.children:
        return 1    
    height_of_tree=0
    for child in root.children:
       child_height= height(child)
       height_of_tree=max(height_of_tree,child_height)
    return height_of_tree+1


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(height(tree))
