from numpy import inner


def fun1(p1, p2):
  print(f"Fun1 and parm - {p1} and p2 - {p2}")
  def trigger(fun):
    def inner_func():
      print("inner func")
      fun(p1, p2)
    return inner_func
  return trigger

@fun1(10, 20)
def actual_func(x, y):
  print("Inside actual func")
  print(f"params x - {x} and y - {y}")


actual_func()