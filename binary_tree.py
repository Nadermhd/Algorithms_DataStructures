'''
Binary tree: each node has a maximum of 2 leafs
Balanced binary tree: left leaf/node is always smaller than right leaf/node
Elements are always unique
Every iteration we reduce the SEARCH by 1/2 --> serach complexity Big O(log n)
   - Breadth first search: we visit all nodes (Left -> Right) in the SAME level before going deeper 
   - Depth first search : - in order traveral:     Left -> Node  -> Right (Ascending order)
                          - pre order traversal    Node -> Left  -> Right
                          - post order traversal:  Left -> Right -> Node

Delete node from tree:
    - node with no child: just delete
    - node with one child: we copy he value of a child to the node and delete child
    - node with 2 children:
        - find Min value of Right subtree -> copy to the node -> delete duplicate
        - find Max value of left subtree -> copy to the node -> delete duplicate
'''
class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):

        if data == self.data:
            # this node already exists
            return
        
        if data < self.data:
            # add to left subtree
            if self.left:
                # node exists and we add as a child
                self.left.add_child(data)
            else:
                # node does not exist
                self.left = BinarySearchTreeNode(data)

        else: 
            # add to right subtree
            if self.right:
                # node exists and we add as a child
                self.right.add_child(data)
            else:
                # node does not exist
                self.right = BinarySearchTreeNode(data)
    
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            self.right.find_max()
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        #else:
        #    self.left.find_max()
        return self.left.find_min()

    def in_order_traversal(self):
        elements = []
        # Left -> node -> right
        # visit left
        if self.left:
            elements += self.left.in_order_traversal()
        # visit node
        elements.append(self.data)
        # visit right
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:    
            # might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def delete(self, val):

        if val < self.data:
            # check the left subtree
            if self.left:
                self.left= self.left.delete(val)
        elif val > self.data:
            # check te right subtree
            if self.right:
                self.right = self.right.delete(val)
        else:
            
            # we found the value: we delete and rearrange
            if self.left is None and self.right is None:
                # there is no subtree for the node
                return None
            if self.left is None: 
                # there is no left subtree
                return self.right
            if self.right is None:
                # there is no right subtree
                return self.right
            # we have both right and left subtree for this node (find min or max)
            # find min val in right subtree
            min_val = self.right.find_min()
            
            # assign to the current node
            self.data = min_val
            # delete the value (duplicate) and create the new right subtree
            self.right = self.right.delete(min_val)
        return self

def build_tree(elm):
    root = BinarySearchTreeNode(elm[0])

    for i in range(1, len(elm)):
        root.add_child(elm[i])
    return root

numbers = [17, 15, 8, 84, 3, 2, 99, 2]
num_tree = build_tree(numbers)
print(num_tree.search(84))
print(num_tree.find_max())
num_tree.delete(8)
print(num_tree.in_order_traversal())

######
countries = ["Germany", "France", "India", "USA", "India"]
#countries = [1, 2, 5, 6, 6, 4, 3]
country_tree = build_tree(countries)

print('Germany is in the list?', country_tree.search("Germany"))
print('Sweden is in the list?', country_tree.search("Sweden"))
print('Sorted Alphabatically: ', country_tree.in_order_traversal())

