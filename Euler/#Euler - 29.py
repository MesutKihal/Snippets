

i = 2
j = 2
terms = set()
while i <= 100:
    j = 2
    while j <= 100:
        terms.add(i**j)
        j += 1
    i += 1
    
print(len(terms))
