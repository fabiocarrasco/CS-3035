checkHyp a b c = c == sqrt(a ^ 2 + b ^ 2)
checkTriple a b c = checkHyp a b c || checkHyp a c b || checkHyp b a c || checkHyp b c a || checkHyp c a b || checkHyp c b a
listOfPythTrips = [[a,b,c]| a<-[1..15], b<-[1..15], c<-[1..15], a<=b && b <=c && checkTriple a b c]
main = print(listOfPythTrips)
