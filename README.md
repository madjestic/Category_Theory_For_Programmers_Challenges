# Category Theory For Programmers Challenges
My solutions to Bartosz Milewski "Category Theory for Programmers" challenges.

## 1.4

### 1. Implement, as best as you can, the identity function in your favorite language (or the second favorite, if your favorite language happens to be Haskell).

```python
# the identity arrow is implemented as the identity function that just returns back its argument.

def identity(x):
    return x
```	

### 2. Implement the composition function in your favorite language. It takes two functions as arguments and returns a function that is their composition.

```python
def compose (f, g):
    return lambda x: f(g(x))


```
(see full example at 1.4.2.py)

```haskell
h :: (b -> c) -> (a -> b) -> a -> c
h f g = f . g
```

### 3. Write a program that tries to test that your composition function respects identity.

Function comparison for partial functions is undefined for Turing Machin in general case, because of the Halting Problem.
Functions might be compared:
- lexically (possibly via reduction)
- by comparing samples of function return values for a number of samples, or for all samples in case of total functions.
- in case of composition with identity, we could cheat by defining the following (in haskell):
```haskell 
id . f == f . id
```

### 4. Is the world-wide web a category in any sense? Are links morphisms?

If links are composable, then they are morphisms, in which case WWW is a category.

### 5. Is Facebook a category, with people as objects and friendships as morphisms?

Friendships do not compose in general, hence they are not morphisms.

### 6. When is a directed graph a category?

When a directed graph's edges are associative, compose and every node has an identity morphism, then such directed graph is a category.

## 2.7

### 1. Define a higher-order function (or a function object) memoize in your favorite language. This function takes a pure function f as an argument and returns a function that behaves almost exactly like f , except that it only calls the original function once for every argument, stores the result internally, and subsequently returns this stored result every time it’s called with the same argument. You can tell the memoized function from the original by watching its performance. For instance, try to memoize a function that takes a long time to evaluate. You’ll have to wait for the result the first time you call it, but on subsequent calls, with the same argument, you should get the result immediately.

```python
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

```

### 2. Try to memoize a function from your standard library that you normally use to produce random numbers. Does it work?

It works, provided the random number generator can be fixed, e.g.:

```python
import random

# define a random number generator with seed:
def rand(seed):
    fseed = math.factorial(1000000) # make it slow to compute i.o.t. test memorization
    random.seed(fseed)
    return random.random()

# > mrand = _271.memoize(_271.rand)
# > mrand(10)
# 0.27256627902952435
```
