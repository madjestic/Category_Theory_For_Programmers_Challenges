import math
import random

def memoize(f):
    memo = {}
    def memoized(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return memoized

# Use example:
# $ python
# > import math
# > import _271
# > fact = _271.memoize(math.factorial)
# > fact(1000000)

# define a random number generator with seed:
def rand(seed):
    fseed = math.factorial(1000000) # make it slow to compute i.o.t. test memorization
    random.seed(fseed)
    return random.random()

# > mrand = _271.memoize(_271.rand)
# > mrand(10)

# Partial Function Application in python
def f(x):
    def g(y):
        return x + y
    return g

# > foo = f(1) # returns a function that takes 1 argument
# > foo(2) # returns a value of 3
