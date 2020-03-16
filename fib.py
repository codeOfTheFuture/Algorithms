# [0, 1, 1, 2, 3, 5, 8, 13, 21]

# Two things that we need for a recursive function
  # 1. Base case
  # 2. 

cache = {}

def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  
  else:
    value = fib(n-1) + fib(n-2)
    return 

print(fib(35))