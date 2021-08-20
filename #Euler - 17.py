import inflect

p = inflect.engine()

chars = ''
for i in range(1,1001):
    chars += p.number_to_words(i)

print(len(chars.replace('-', '').replace(' ', '')))

