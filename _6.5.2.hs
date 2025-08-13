module Main where

data Shape = Circle Float
           | Rect Float Float

area :: Shape -> Float
area (Circle r) = pi * r * r
area (Rect d h) = d * h

main = undefined  
