findEven :: [Int] -> Int
findEven xs 
   | length xs == 0 = 0
   | otherwise = if mod (head xs) 2 == 0 then 1 + findEven (tail xs) else findEven (tail xs)
