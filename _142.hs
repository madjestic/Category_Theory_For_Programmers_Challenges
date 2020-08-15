module Main where

foo x = x+1

bar x = x^2

h :: (b -> c) -> (a -> b) -> a -> c
h f g = f . g

main = undefined
