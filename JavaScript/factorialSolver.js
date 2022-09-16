function factorialSolver(n){
	if(n==0) return 1;
	return n*factorialSolver(n-1);
}
console.log(factorialSolver(5));
console.log(factorialSolver(0));
console.log(factorialSolver(1));
console.log(factorialSolver(3));

function reverseString(n){
	if(n.length == 0) return "";
	return reverseString(n.substring(1,n.length))+n.charAt(0);
}
console.log(reverseString("abc"));
console.log(reverseString("apple"));
console.log(reverseString("race car"));

function inAlphabet(n){
	var alphabet = "abcdefghijklmnopqrstuvwxyz";
	if(alphabet.charAt(0).includes(n)){
		
	}
}
console.log(inAlphabet("abc"));
console.log(inAlphabet("apple"));
console.log(inAlphabet("race car"));
