from random import *
from sys import exit

wlist = open("words.txt").readlines()
wstr = open("words.txt").read()
dict = open("dict.txt").read()
word = choice(wlist)
result = []

def check(word, guess):
    for n in range(0,5):
        if word[n] == guess[n]:
            result.append('O')
            n = n+1
        elif word.find(guess[n]) != -1:
            if word.count(guess[n]) >= guess[0:n + 1].count(guess[n]):
                result.append('I')
                n = n+1
            else:
                result.append('X')
                n = n+1
        else:
            result.append('X')
            n = n+1
    return(result)

print('Welcome to Walmart Wordle, type your first guess to start \n')

i = 0
while i < 6:
    guess = str(input())
    
    if len(guess) != 5 or dict.find(guess) == -1:
        print("please enter a valid 5 letter word")
    else:
        print(check(word , guess))
        result = []
        i = i + 1

        if str(guess) == word[0:5]:
            if i == 1:
                print('You won in 1 attempt')
                exit(0)
            else:
                print('You won in ' + str(i) + ' attempts')
                exit(0)
print('You lost, the word was ' + str(word))