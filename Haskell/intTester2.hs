intTester l xs = [x | x <- l, (xs x)]
l1 :: Int -> Bool
l1 = (\x -> if mod x 2 == 0 then True else False)
l2 :: Int -> Bool
l2 = (\x -> if x > 5 then True else False)
