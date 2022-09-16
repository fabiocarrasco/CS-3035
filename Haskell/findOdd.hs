findOdd :: [Int] -> Int
findOdd xs 
   | length xs == 0 = 0
   | otherwise = if mod (head xs) 2 /= 0 then 1 + findOdd (tail xs) else findOdd (tail xs)
