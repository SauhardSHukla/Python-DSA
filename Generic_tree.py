

class genertree:
    def __init__(self,data):
        self.data = data
        self.children =[]
    
    def print_lvl_wise(tree):
        q=[tree]
        while q:
            parent = q.pop(0)
            print(parent.data,':',",".join(str(num.data)for num in parent.children)
                ,sep='')
            for child in parent.children:
                q.append(child)

    def height(root):
        if root is None:
            return 0
        
        if not root.children:
            return 1
        
        max_nodes_height= 0
        for child in root.children:
            child_height = genertree.height(child)
            max_nodes_height=max(max_nodes_height, child_height)
        return max_nodes_height+1

    def createlvlwise(arr):
        root= genertree(int(arr[0]))
        q = [root]
        size = len(arr)
        i=1
        while i < size:
            curr_node = q.pop(0)
            child_node = int(arr[i])
            i+=1
            for j in range (0,child_node):
                child_nodes_data  = genertree(int(arr[i+j]))
                curr_node.children.append(child_nodes_data)
                q.append(child_nodes_data)
            i+=child_node
        return root



arr=[10 ,3, 20, 30, 40, 2, 40, 50, 0, 0, 0, 0 ]r
tree = genertree.createlvlwise(arr)
genertree.print_lvl_wise(tree)
print(genertree.height(tree))

