firstHalf :: [a] -> [a]
firstHalf xs = take (ceiling (fromIntegral (length xs) / 2)) xs

secondHalf :: [a] -> [a]
secondHalf ys = drop (ceiling (fromIntegral (length ys) / 2)) ys

l1 :: Ord a => a -> a -> Bool
l1 = (\x  y -> if x <= y then True else False)

l2 :: Ord a => a -> a -> Bool
l2 = (\x  y -> if y <= x then True else False)

merge :: (Ord a) => [a] -> [a] -> (a -> a -> Bool) -> [a]
merge xs ys l
  | length xs == 0 = xs ++ ys
  | length ys == 0 = xs ++ ys
  | otherwise = if l (head xs) (head ys) then head xs : merge (tail xs) ys l else head ys : merge xs (tail ys) l

mergeSort :: Ord a => [a] -> (a -> a -> Bool) -> [a]
mergeSort xs l
  | length xs < 2 = xs
  | otherwise = merge (mergeSort (firstHalf xs) l)(mergeSort (secondHalf xs) l) l
