intTester :: [Int] -> (Int -> Bool) -> [Int]
intTester xs l 
   | length xs == 0 = []
   | otherwise = if l (head xs) then (head xs) : intTester (tail xs) l else intTester (tail xs) l
l1 :: Int -> Bool
l1 = (\x -> if mod x 2 == 0 then True else False)
l2 :: Int -> Bool
l2 = (\x -> if x > 5 then True else False)
