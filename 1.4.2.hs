module Main where

h :: (b -> c) -> (a -> b) -> a -> c
h f g = f . g

main = undefined
