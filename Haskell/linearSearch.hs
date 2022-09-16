linearSearch :: Eq a => [a] -> a -> Bool
linearSearch = \myList -> \elem ->
  case myList of
    [] -> False 
    x:xs | x == elem -> True 
    _:xs -> linearSearch xs elem 
