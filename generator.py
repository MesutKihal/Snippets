import math


def generator(nums):
    for i in nums:
        yield math.sqrt(i)

my_nums = generator([45,9,2,12,67,8,24])

for num in my_nums:
    print(num)

#Or use next()

#print(next(my_nums))    #4.898979485566356
