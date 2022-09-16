checkHyp a b c = c == sqrt(a ^ 2 + b ^ 2)
checkTriple a b c = checkHyp a b c || checkHyp a c b || checkHyp b a c || checkHyp b c a || checkHyp c a b || checkHyp c b a
listOfPythTrips x y = [[a,b,c]| a<-[x..y], b<-[x..y], c<-[x..y], a<=b && b <=c && checkTriple a b c]
main = print(listOfPythTrips 1 15)
