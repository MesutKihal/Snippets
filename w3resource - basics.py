
#W3RESOURCE Exercices

#Exercice1

import datetime
name = str(input())
age = int(input())
year = int(str(datetime.date.today())[0:4]) - age + 100
print(f"{name} will get 100 years old in the year {year}.")

#Exercice2

num = int(input())
if num%2 == 0:
    print("\nThis number is even.")
else:
    print("This number is odd.")

#Exercice3

print(list(num for num in list(map(int,input().split())) if num<5))

#Exercice4

num = int(input())
print(list(div for div in range(1,num) if num%div==0))

#Exercice5

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print([num for num in a if num in b])

#Exercice6

s = str(input())
if s == s[::-1]:
    print(True)
else:
    print(False)

#Exercice7

def even_odd(x):
    if x%2 == 0:
        return True
    else:
        return False
print(list(filter(lambda x:even_odd(x),list(map(int,input().split())))))

#Exercice8

player1 = str(input())
player2 = str(input())
if player1 == "rock" and player2 == "scissors": print("Player1 is the winner.")
elif player1 == "scissors" and player2 == "paper": print("Player1 is the winner.")    
elif player1 == "paper" and player2 == "rock": print("Player1 is the winner.")
elif player2 == "rock" and player1 == "scissors": print("Player2 is the winner.")
elif player2 == "scissors" and player1 == "paper": print("Player2 is the winner.")    
elif player2 == "paper" and player1 == "rock": print("Player2 is the winner.")

#Exercice9

import random
num = int(input())
rnd = random.randint(1,9)
if num < rnd:
    print("too low.")
elif num > rnd:
    print("too high.")
else:
    print("exactly.")

#Exercice10

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(set(a).intersection(set(b)))

#Exercice11

num = int(input())
if len(list(div for div in range(2,num) if num%div==0)) == 0:
    print("This is prime number.")
else:
    print("This is not a prime number.")

#Exercice12

def first_and_last(arr):
    return [arr[0],arr[-1]]
print(first_and_last(list(map(int, input().split()))))

#Exercice13

def fibonacci(rng):
    arr = []
    num = 0
    while len(arr) <= rng:
        if len(arr) >= 2:
            arr.append(arr[num-2]+arr[num-1])
        else:
            arr.append(num)
        num += 1
    return arr[1:]
print(fibonacci(int(input())))

#Exercice14

def duplicate_free(arr):
    new_arr = []
    for elm in arr:
        if elm in new_arr:
            pass
        else:
            new_arr.append(elm)
    return new_arr
print(duplicate_free(list(map(int, input().split()))))

#Exercice15

def reversed_order(string):
    new_string = " ".join(list(string.split())[::-1])
    return new_string
print(reversed_order(str(input())))

#Exercice16

import string
import random
def password_generator(size):
    return "".join(random.choices(str(string.ascii_letters)+str(string.digits)+str(string.punctuation),k=size))
print(password_generator(int(input())))

#Exercice17

import requests
from bs4 import BeautifulSoup
source = requests.get("https://www.nytimes.com/").text
soup = BeautifulSoup(source,'lxml')

for article in  soup.find_all('p'):
	print(article.text+"\n\n")

#Exercice18

import random
def cows_bulls(guess):
    generated = random.choices("0123456789",k=4)
    cow = 0
    bull = 0
    index = 0
    for char in guess:
        if char in generated and guess[index] == generated[index]:
            cow += 1
        if char in generated and guess[index] != generated[index]:
            bull += 1
        else:
            pass
        index += 1
    return f"{cow} cows, {bull} bulls.",guess,generated
print(cows_bulls([char for char in input()]))

#Exercice19

import requests
from bs4 import BeautifulSoup
source = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture").text
soup = BeautifulSoup(source,'lxml')

for article in  soup.find_all('p'):
	print(article.text)

#Exercice20

def elem_search(arr, elem):
    isFound = False
    def search(arr,elem):
        global isFound
        mid = len(arr)//2
        if elem > arr[mid]:
            search(arr[mid:],elem)
        elif arr[mid] == elem:
            isFound = True
        elif arr[0] <= elem < arr[mid]:
            search(arr[:mid+1],elem)
        else:
            isFound = False
        return isFound
    return search(arr,elem)
print(elem_search(list(map(int, input().split())),int(input())))

#Exercice21

import requests
from bs4 import BeautifulSoup
source = requests.get("https://www.nytimes.com/").text
soup = BeautifulSoup(source,'lxml')

with open("file.txt", "a") as f:
    for article in  soup.find_all('p'):
        f.write(article.text+"\n\n")

#Exercice22

import re
names = dict()
with open("file.txt", "r") as f:
    for line in f.readlines():
        print(re.findall(re.compile(r"[a-z]+"),line)[0])

#Exercice23

happy = []
prime = []
with open("happy.txt", "r") as f:
    for line in f.readlines():
        happy.append(int(line))
with open("prime.txt", "r") as f:
    for line in f.readlines():
        prime.append(int(line))
print(set(happy).intersection(set(prime)))

#Exercice24

print(" --- --- --- ")
for _ in range(3):
    print("|   |   |   | \n")
    print(" --- --- --- ")

#Exercice25

import random
guesses = 0
x = 1
y = 100
while True:
    r = random.randint(x,y)
    print(r)
    ans = input()
    if ans == "exactly":
        print(f"\tnumber of guesses: {guesses}")
        break
    else:
        if ans == "too low":
            x = r
        if ans == "too high":
            y = r
        guesses += 1
        continue

#Exercice26

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
if game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1:
    print("Player 1 wins")
if game[0][0] == 2 and game[1][1] == 2 and game[2][2] == 2:
    print("Player 2 wins")
if game[0][2] == 1 and game[1][1] == 1 and game[2][0] == 1:
    print("Player 1 wins")
if game[0][2] == 2 and game[1][1] == 2 and game[2][0] == 2:
    print("Player 2 wins")
if game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1:
    print("Player 1 wins")
if game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 2:
    print("Player 2 wins")
if game[0][1] == 1 and game[1][1] == 1 and game[2][1] == 1:
    print("Player 1 wins")
if game[0][1] == 2 and game[1][1] == 2 and game[2][1] == 2:
    print("Player 2 wins")
if game[0][2] == 1 and game[1][2] == 1 and game[2][2] == 1:
    print("Player 1 wins")
if game[0][2] == 2 and game[1][2] == 2 and game[2][2] == 2:
    print("Player 2 wins")

#Exercice27

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
isOver = False
player1 = True
player2 = False
while isOver == False:
    index = 1
    print("   1  2  3")
    for row in game:
        print(f"{index} "+str(row))
        index += 1

    if player1 == True:
        turn = list(map(int,input("player1's turn\nEnter coordinates (row, column): ").split()))
        game[turn[0]-1][turn[1]-1] = 1
        player1 = False
        player2 = True
    index = 1
    print("   1  2  3")
    for row in game:
        print(f"{index} "+str(row))
        index += 1
    if player2 == True:
        turn = list(map(int,input("player2's turn\nEnter coordinates (row, column): ").split()))
        game[turn[0]-1][turn[1]-1] = 2
        player2 = False
        player1 = True

#Exercice28

def max_of_three(num1, num2, num3):
    arr = [num1, num2, num3]
    return max(arr)
result = max_of_three(int(input()), int(input()), int(input()))
print(result)

#Exercice29

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

player1 = True
player2 = False
def player1_check():
    isOver = False
    if game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1:
        print("\nPlayer 1 wins")
        isOver = True
    elif game[0][2] == 1 and game[1][1] == 1 and game[2][0] == 1:
        print("\nPlayer 1 wins")
        isOver = True
    elif game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1:
        print("\nPlayer 1 wins")
        isOver = True
    elif game[0][1] == 1 and game[1][1] == 1 and game[2][1] == 1:
        print("\nPlayer 1 wins")
        isOver = True
    elif game[0][2] == 1 and game[1][2] == 1 and game[2][2] == 1:
        print("\nPlayer 1 wins")
        isOver = True
    elif all(char==1 for char in game[0]):
        print("\nPlayer 1 wins")
        isOver = True
    elif all(char==1 for char in game[1]):
        print("\nPlayer 1 wins")
        isOver = True
    elif all(char==1 for char in game[2]):
        print("\nPlayer 1 wins")
        isOver = True
    return isOver

def player2_check():
    isOver = False
    if game[0][0] == 2 and game[1][1] == 2 and game[2][2] == 2:
        print("\nPlayer 2 wins")
        isOver = True
    elif game[0][2] == 2 and game[1][1] == 2 and game[2][0] == 2:
        print("\nPlayer 2 wins")
        isOver = True
    elif game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 2:
        print("\nPlayer 2 wins")
        isOver = True
    elif game[0][1] == 2 and game[1][1] == 2 and game[2][1] == 2:
        print("\nPlayer 2 wins")
        isOver = True
    elif game[0][2] == 2 and game[1][2] == 2 and game[2][2] == 2:
        print("\nPlayer 2 wins")
        isOver = True
    elif all(char==2 for char in game[0]):
        print("\nPlayer 2 wins")
        isOver = True
    elif all(char==2 for char in game[1]):
        print("\nPlayer 2 wins")
        isOver = True
    elif all(char==2 for char in game[2]):
        print("\nPlayer 2 wins")
        isOver = True
    return isOver

def draw_gameboard():
    global index 
    index = 1
    print("   1  2  3")
    for row in game:
        print(f"{index} "+str(row))
        index += 1
draw_gameboard()
while True:
    if player1 == True:
        move = list(map(int,input("\nplayer1's turn\nEnter coordinates (row, column): ").split()))
        while True:
            if game[move[0]-1][move[1]-1] == 0:
                game[move[0]-1][move[1]-1] = 1
                break
            else:
                print("\nWrong Value!!")
                move = list(map(int,input("\nplayer1's turn\nEnter coordinates (row, column): ").split()))
        player1 = False
        player2 = True
        draw_gameboard()
        if player1_check() == True:
            break
        
    if player2 == True:
        move = list(map(int,input("\nplayer2's turn\nEnter coordinates (row, column): ").split()))
        while True:
            if game[move[0]-1][move[1]-1] == 0:
                game[move[0]-1][move[1]-1] = 2
                break
            else:
                print("\nWrong Value!!")
                move = list(map(int,input("\nplayer2's turn\nEnter coordinates (row, column): ").split()))

        player2 = False
        player1 = True
        draw_gameboard()
        if player2_check() == True:
            break

#Exercice30

import random
norvig = dict()
with open("SOWPODS.txt", "r") as f:
    for line in f.readlines():
        if norvig.get(f"{line[0]}") == None:
            temp = list()
            temp.append(line[:-2])
        else:
            temp = norvig.get(f"{line[0]}")
            temp.append(line[:-2])
        norvig[f"{line[0]}"] = temp

index = 0
for value in norvig.values():
    print(list(norvig.keys())[index],random.choice(value))
    index += 1

#Exercice31

print("Welcome to Hangman!")
guessed = set()
while True:
    letter = str(input("Guess your letter:   "))
    word = "evaporate"
    progress = ""
    for l in word:
        if l == letter:
            guessed.add(l)
        if l in guessed:
            progress += l
        else:
            progress += "_"
    if letter in word:
        print(progress)
    else:
        print("Incorrect!")
    if progress == word:
        break

#Exercice32

print("Welcome to Hangman!")
guessed = set()
guesses = 0
while guesses < 6:
    print(f"You have {abs(guesses-6)} incorrect guesses left.\n")
    letter = str(input("Guess your letter:   "))
    word = "evaporate"
    progress = ""
    for l in word:
        if l == letter:
            guessed.add(l)
        if l in guessed:
            progress += l
        else:
            progress += "_"
    if letter in word:
        print(progress)
    else:
        guesses += 1
        print("Incorrect!")
    if progress == word:
        break

#Exercice33

birthday = {
    "Dennis Ritchie":"September 9, 1941",
    "Guido van Rossum":"31 January 1956",
    "Larry Wall":"September 27, 1954",
    "Bjarne Stroustrup":"30 December 1950",
    }
print("Welcome to the birthday dictionary. We know the birthdays of:")
for key in birthday.keys():
    print(key)
answer = input("Who's birthday do you want to look up?\n")
date = birthday.get(answer)
if date != None:
    print(f"{answer}\'s birthday is {date}.")
else:
    print(f"{answer}\'s birthday is unknown.")

