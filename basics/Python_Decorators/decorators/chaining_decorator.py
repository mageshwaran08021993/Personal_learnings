"""
if multiple decorators are there, execution starts from lower from upper direction
"""


# code for testing decorator chaining
def decor1(func):
  print("Inside Decor1")
  def inner():
    x = func()
    return x * x
  return inner

def decor(func):
  print("Inside Decor var")
  def inner():
    x = func()
    return 2 * x
  return inner

print("Start Func")
@decor1
@decor
def num():
	return 10

print(num())
