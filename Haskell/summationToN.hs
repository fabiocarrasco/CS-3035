summationToN :: Int -> Int
summationToN n = if n < 0 then 0 else summationToN (n-1) + n
