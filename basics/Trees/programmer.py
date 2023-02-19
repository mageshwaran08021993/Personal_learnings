class TreeNode:
  def __init__(self, data, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return self.data

def insert(temp,data):
  que = []
  que.append(temp)

  while (len(que)):
    temp = que[0]
    que.pop(0)
    if (not temp.left):
      temp.left = TreeNode(data)
      break
    else:
      que.append(temp.left)
    if (not temp.right):
      temp.right = TreeNode(data)
      break
    else:
      que.append(temp.right)

def make_tree(elements):
  Tree = TreeNode(elements[0])
  for element in elements[1:]:
    insert(Tree, element)
  return Tree

class Solution(object):
  def inorderTraversal(self, root):
    res, stack = [], []
    data_left = []
    current = root
    while True:
      data_left_val = 0
      while current:
        stack.append(current)
        # data_left_val += current.data
        current = current.left
      if len(stack) == 0:
        return res
      node = stack[-1]
      #  print("stack - ", stack)
      stack.pop(len(stack)-1)
      #  print("after pop - ", stack)
      if node.data != None:
        # data_left_val += current.data
        res.append(node.data)
      current = node.right
    return res

# Use the insert method to add nodes


if __name__ == "__main__":
  a="40 30 50 25 35 45 60".split(" ")
  ob1 = Solution()
root = make_tree(a)
print(ob1.inorderTraversal(root))