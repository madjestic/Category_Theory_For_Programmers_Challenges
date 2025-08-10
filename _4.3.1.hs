module Main where

import Control.Category (Category (..))
import Control.Monad ((>=>))

  -- | 4.3.1. Construct the Kleisli category for partial functions (define composition and identity).

data Partial a b = Partial { runPartial :: a -> Maybe b}

instance Category Partial where
  id :: Partial a a
  id = Partial Just

  (.) :: Partial b c -> Partial a b -> Partial a c
  --(Partial g) . (Partial f) = Partial (\x -> f x >>= g)
  (Partial g) . (Partial f) = Partial (f >=> g)

main :: IO ()
main = undefined
