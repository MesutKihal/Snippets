def fibonacci(n):
    temp = []
    for num in range(n):
        if len(temp) <= 1: 
            temp.append(num)
        else:
            temp.append(temp[-1]+temp[-2])

    print(temp)

fibonacci(int(input('>>>>>>>> ')))
