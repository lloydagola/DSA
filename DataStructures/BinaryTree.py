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


