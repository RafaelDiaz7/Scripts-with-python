def checkPalindrome(inputString):
	palindrome = inputString[::-1]
	if palindrome == inputString:
		print 'Your string Its palindrome'
		return True
	else:
		print "The string its not palindrome"
		return False
checkPalindrome("caabaac")