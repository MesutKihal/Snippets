

def string_reversal(string):
    i = len(string)-1
    if string == "":
        return ""
    else:
        return string[i] + string_reversal(string[:i])

print(string_reversal('HELLO'))

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


def binary(num):
    result = num % 2
    if num == 0:
        return "0"
    else:
        return  binary(num // 2) + str(result)
print(binary(233))
