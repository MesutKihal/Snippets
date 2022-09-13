def palindrome(string):
    i = len(string)-1
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        if string[0] == string[i]:
            return palindrome(string[1:i])
        else:
            return False
        
print(palindrome('racecar'))
