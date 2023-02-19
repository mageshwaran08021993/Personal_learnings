class Node:
    def __init__(self, info, level = None): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = level 

    def __str__(self):
        return str(self.info)
    
    

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val, level=0)
            print("root - ", self.root.info)
        else:
            current = self.root
            level = self.root.level+1
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                        level +=1
                    else:
                        current.left = Node(val, level=level)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                        level +=1
                    else:
                        current.right = Node(val, level=level)
                        break
                else:
                    break

    def printTree(self):
      current = self.root
      res, stack = [], []
      data_left = []
        # current = root
      while True:
        while current:
            stack.append(current)
            current = current.left
        if len(stack) == 0:
            return res
        # print(stack)
        node = stack[-1]
        #  print("stack - ", stack)
        stack.pop(len(stack)-1)
        #  print("after pop - ", stack)
        # print(node)
        if node.info != None:
            # data_left_val += current.data
            res.append((node.info, node.level))
        current = node.right
      return res

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
# DC0 - n
# 1C0 - l - n
# 220 - r

def height(node):
    if node is None:
        return 0
    else:
  
        # Compute the depth of each subtree
        lDepth = height(node.left)
        rDepth = height(node.right)
  
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

def getHeight(node):
    if node.left and node.right:
        return 1+ max(getHeight(node.left), getHeight(node.right))
    elif node.left:
        return 1 + getHeight(node.left)
    elif node.right:
        return 1 + getHeight(node.right)
    else:
        return 1

def getHeight_for_value(node, value):
    if node is not None:
        print("Value in getheght - ", node.info)
    if node is None:
        return 1
    elif int(node.info) == value:
        return getHeight(node)
    elif int(node.info) > value:
        if node.left:
            return getHeight_for_value(node.left, value)
        return 0
    elif int(node.info) < value:
        if node.right:
            return getHeight_for_value(node.right, value)
        return 0
    else:
        return 1

def print_tree_out(node):
    if node.left:
        print_tree_out(node.left)
    print(node.info)
    if node.right:
        print_tree_out(node.right)

def print_subtree_by_value(node, value):
    # if node is not None:
    #     print("Value in node - ", node.info)
    if node is None:
        print("Node Not Found")
    elif int(node.info) == value:
        print_tree_out(node)
    elif int(node.info) > value:
        if node.left:
            print_subtree_by_value(node.left, value)
        # print("Node not found in left")
    elif int(node.info) < value:
        if node.right:
            print_subtree_by_value(node.right, value)
        # print("Node not found in right")
    else:
        print("Node not found in else")

tree = BinarySearchTree()
# t = "4 2 6 1 3 5 7"
# t = "3 5 2 1 4 6 7"
t = "40 30 50 25 35 45 60 42"
# 
arr = t.split(" ")

for i in range(0, len(arr)):
    tree.create(arr[i])


# n=Node()
print(tree.printTree())
print("hieght by comparison - ", height(tree.root))
# print(getHeight(tree.root.left.left))
# print("getheight by value - ", getHeight_for_value(tree.root, 345))
print("Values in Subtree by value in inorder")
print_subtree_by_value(tree.root, 30)

# print_tree_out(tree.root)