#need to be updatedd to get to play with user

import random 
s=["O","[]","%"]
choose1 = input("type the weapon : ")

choose2 = random.choice(s)
print(choose1)
print(choose2)

def play():
  
  global choose1
  global choose2

  if choose1==choose2:
   return ("its a tie")


  if ch1():
   return("ch1 won")
  return ("ch2 won")   

 # O >> % >> [] >> O  rule:RSP


def ch1():
  global ch1
  if choose1 == "O" and choose2=="%" or choose1 == "%" and  choose2=="[]" or choose1 == "[]" and choose2=="O":
   return True

print(play())