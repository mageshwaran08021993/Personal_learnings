class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
    # __str__ or __repr__ to print the object, its similar to to_string in java
    def __str__(self):
      return self.data
    def __repr__(self) -> str:
        return self.data+"repr"

root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"
print(root)
print(root.left)
print(root.right)
print([root]) # to invoke __repr__ method
