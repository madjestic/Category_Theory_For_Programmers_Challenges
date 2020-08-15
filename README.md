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
