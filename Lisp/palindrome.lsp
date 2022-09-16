(defun test-palindrome(s)
	(COND
		((<= (length s) 1) 
			t
		)
		((not (char= (char-downcase (char s 0)) (char-downcase(char s (- (length s) 1)))))
			nil
		)
		((char= (char-downcase (char s 0)) (char-downcase(char s (- (length s) 1))))
			(if(test-palindrome(subseq s 1 (-(length s) 1))) t)
		)
		(t
			(test-palindrome(subseq s 1 (-(length s) 1)))
		)
	)
)
(test-palindrome "")
(test-palindrome "a")
(test-palindrome "aa")
(test-palindrome "ab")    
(test-palindrome "abc")
(test-palindrome "aba")
