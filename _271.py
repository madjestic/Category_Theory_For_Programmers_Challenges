import math

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

# Partial Function Application in python
def f(x):
    def g(y):
        return x + y
    return g        
