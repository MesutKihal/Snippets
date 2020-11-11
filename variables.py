import random
for i in range(1,82):
	choice = random.choice([0,0,random.randint(1,9)])
	exec("var"+str(i)+" ="+str(choice))
