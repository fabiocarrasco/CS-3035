firstHalf :: [a] -> [a]
firstHalf xs = take (ceiling (fromIntegral (length xs) / 2)) xs

secondHalf :: [a] -> [a]
secondHalf ys = drop (ceiling (fromIntegral (length ys) / 2)) ys

merge :: Ord a => [a] -> [a] -> [a]
merge xs ys
   | length xs == 0 = xs ++ ys
   | length ys == 0 = xs ++ ys
   | otherwise = if head xs <= head ys then head xs : merge (tail xs) ys else head ys : merge xs (tail ys)

mergeSort :: Ord a => [a] -> [a]
mergeSort xs
   | length xs < 2 = xs
   | otherwise = merge (mergeSort (firstHalf xs)) (mergeSort (secondHalf xs))

