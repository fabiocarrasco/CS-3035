mBros = ["Groucho", "Harpo", "Zeppo", "Beppo"]
stooges = ["Moe", "Curly", "Shemp"]
shorter [x,y] = if length x == length y then 
 "length of " ++ x ++ " is the same as length of " ++ y
 else if length x < length y then
 "length of " ++ x ++ " is shorter than length of " ++ y
 else "length of " ++ y ++ " is shorter than length of " ++ x
short as bs = [shorter[a,b]|a<-as,b<-bs]
main = print(short mBros stooges)
