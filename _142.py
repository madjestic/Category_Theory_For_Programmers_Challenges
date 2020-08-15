# 2. Implement the composition function in your favorite language. It takes two functions as arguments and returns a function that is their composition.

def foo(x):
    return x+1

def bar (x):
    return x**2

def compose (f, g):
    return lambda x: f(g(x))

def main():
    f = compose(foo, bar)
    result = f(2)
    print (result)

if __name__ == "__main__":
    # execute only if run as a script
    main()
