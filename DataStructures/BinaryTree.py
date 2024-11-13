class TreeNode :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def pre_order_traversal(node):
    if node is None:
        return    
    
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


def in_order_traversal(node):
    if node is None:
        return
    
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)

def post_order_traversal(node):
    if node is None:
        return
    
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)

def binary_serch(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return binary_serch(node.left, target)
    else:
        return binary_serch(node.right, target)

def insert(node, data):
    if node is None:
        insert(node)
    elif data > node.data:
        node.right = insert(node.right, data)
    elif data < node.data:
        node.left = insert(node.left, data)

#set up nodes
R_TreeNode = TreeNode("R")
A_TreeNode = TreeNode("A")
B_TreeNode = TreeNode("B")
C_TreeNode = TreeNode("C")
D_TreeNode = TreeNode("D")
E_TreeNode = TreeNode("E")
F_TreeNode = TreeNode("F")
G_TreeNode = TreeNode("G")



#link nodes
R_TreeNode.left = A_TreeNode
R_TreeNode.right = B_TreeNode

A_TreeNode.left = C_TreeNode
A_TreeNode.right = D_TreeNode

B_TreeNode.left = E_TreeNode
B_TreeNode.right = F_TreeNode

F_TreeNode.left = G_TreeNode

pre_order_traversal(R_TreeNode)


