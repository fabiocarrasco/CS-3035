stoogesInfinity = cycle["Moe","Larry","Shemp"]
slap a b = take b ["slap " ++ x | x <- a]
main = print(slap stoogesInfinity 20)
