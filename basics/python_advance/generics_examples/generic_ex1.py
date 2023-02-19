"""
Python has implemented Type Hints from version 3.5
"""

# from typing import Any, List

# def first(container: List[int]) -> int:
#     return container[0]
  
# if __name__ == "__main__":
#     list_one: List[str] = [1, "a", "b", "c", 1]
#     print(first(list_one))
    
#     list_two: List[int] = ["1", 2, 3, "a"]
#     print(first(list_two))


# from typing import List, TypeVar

# T = TypeVar("T")

# def first(container: List[T]) -> T:
#     return container[0]
  
# if __name__ == "__main__":
#     list_one: List[str] = [1, "a", "b", "c"]
#     print(first(list_one))
    
#     list_two: List[int] = [1, 2, 3]
#     print(first(list_two))

# from typing import List, TypeVar

# T = TypeVar("T")

# def first(container: List[T]) -> T:
#     print(container)
#     return "a" # mypy raises: Incompatible return value type (got "str", expected "T")
  
# if __name__ == "__main__":
#     list_one: List[str] = ["a", "b", "c"]
#     print(first(list_one))


def sub_this(x:int,y:int) -> int:
    return 1
print(sub_this(8,4))

print(f" {'check'.title() }".center(50, " "))


# I got a take home assignment to build SPARK application on recipes dataset. The problem was easy but the expectations on the solution was very high. The code should be object-oriented, with config files, unit test cases, logging and alerting, exception handling. Extra points for CI/CD , etc
