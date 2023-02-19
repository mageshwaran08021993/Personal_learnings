# from readline import insert_text


from copy import copy


class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # __str__ or __repr__ to print the object, its similar to to_string in java
    def __str__(self):
      return self.data
    def __repr__(self) -> str:
        return self.data+"repr"

    def insert_data(self, data):
      if data < self.data:
        if self.left:
          self.left.insert_data(data)
        else:
          self.left = Tree(data)
      else:
        if self.right:
          self.right.insert_data(data)
        else:
          self.right = Tree(data)

    # print the data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
        
    def add_left_child_data(self):
      globals()['su'] += self.data
      if self.left:
        self.left.add_left_child_data()
      if self.right:
        self.right.add_left_child_data()


    def left_sum_for_root(self):
      # print("evaludating for node data - ", self.data)
      current = self
      globals()['su'] = 0
      if current.left or current.right:
        globals()['su'] = current.data
        current.right.add_left_child_data()
        current.data = globals()['su']
        current.left.left_sum_for_root()
        current.right.left_sum_for_root()

    def minValueNode(node):
      current = node
      # loop down to find the leftmost leaf
      while(current.left is not None):
          current = current.left
  
      return current

    def delete_val(root, key):
      # Base Case
      if root is None:
          return root
  
      # If the key to be deleted
      # is smaller than the root's
      # key then it lies in  left subtree
      if key < root.data:
          root.left = root.left.delete_val(key)
  
      # If the kye to be delete
      # is greater than the root's key
      # then it lies in right subtree
      elif(key > root.data):
          root.right = root.right.delete_val(key)
  
      # If key is same as root's key, then this is the node
      # to be deleted
      else:
  
          # Node with only one child or no child
          if root.left is None:
              temp = root.right
              root = None
              return temp
  
          elif root.right is None:
              temp = root.left
              root = None
              return temp
  
          # Node with two children:
          # Get the inorder successor
          # (smallest in the right subtree)
          temp = root.right.minValueNode()
  
          # Copy the inorder successor's
          # content to this node
          root.data = temp.data
  
          # Delete the inorder successor
          root.right = root.right.delete_val(temp.data)
  
      return root


        

# Creating root node
ele = [40, 30, 50, 25, 35, 45, 60]
root = Tree(ele[0])
su = 0
lt = []
# Inserting values in BST
for i in ele[1:len(ele)]:
  root.insert_data(i)

# root.left_sum_for_root()
# check = copy(root)
root = root.delete_val(40)
root.PrintTree()
