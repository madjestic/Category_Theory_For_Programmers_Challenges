#Write a program that tries to test that your composition function respects identity.

def foo(x):
    return x+1

def bar (x):
    return x**2

def baz (x):
    return x*x

def compose (f, g):
    return lambda x: f(g(x))

def test():
    return 0
    
