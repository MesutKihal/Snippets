
def Anagram(str_1, str_2):
    l1 = []
    for char in str_1:
        l1.append(char)
    l1 = sorted(l1)
    l2 = []
    for char in str_2:
        l2.append(char)
    l2 = sorted(l2)
    if l1 == l2:
        return f'"{str_1}" and "{str_2}" are anagrams.'
    else:
        return f'"{str_1}" and "{str_2}" are not anagrams.'
    


print('Enter two strings and I\'ll tell you if they are anagrams:')

result = Anagram(str(input('Enter the first string: ')),
                 str(input('Enter the second string: ')))

print(result)
