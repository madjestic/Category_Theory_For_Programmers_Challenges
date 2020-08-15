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

