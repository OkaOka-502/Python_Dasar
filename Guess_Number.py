import random

class Guess_Number :
    def __init__ (self): 
        self.system = random.randint(1,10)
        self.answer = " "

    def check (self):
        if int (self.answer) == self.system :
            return True
        else :
            return False

gn = Guess_Number()

print("Let's play guessing the numbers with a system from 1 - 10!")
gn.answer = input('Your Answer: ')

    
reset = True
while reset :
    if gn.check():
        print("Congrats u're right!XD")
        break
    else :
        print("Sorry u're wrong!;(")
        gn.answer = input ("Let's answer again: ")
