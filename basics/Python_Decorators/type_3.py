# Python code to illustrate
# Decorators with parameters in Python

def decorator_func(x, y):
  print("inside decorator func")
  def Inner(func):
    print("Inside Inner Func")
    def wrapper(*args, **kwargs):
      print("I like Geeksforgeeks")
      print("Summation of values - {}".format(x+y) )

      func(*args, **kwargs)
			
    return wrapper
  return Inner


# Not using decorator
def my_fun(*args):
	for ele in args:
		print(ele)

# another way of using decorators
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')
