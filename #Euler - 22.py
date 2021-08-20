def name_score(name, i):
    score = 0
    for char in name:
        score += ord(char)-64
    score *= i
    return score


with open("names.txt", "r") as f:
    names = sorted(f.readlines()[0].replace('"', '').strip().split(","))
    i = 0
    all_score = 0
    while i < len(names):
        all_score += name_score(names[i], i+1)
        i += 1

print(all_score)
