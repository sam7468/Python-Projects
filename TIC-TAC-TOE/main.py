#board materials
board =['.','.','.','.','.','.','.','.','.']

#board structure as function
def show_board():
  print(board[0] +  '|' + board[1] +  '|'  + board[2])
  print(board[3] +  '|' + board[4] +  '|'  + board[5])
  print(board[6] +  '|' + board[7] +  '|'  + board[8])       

#to define the while loop we use global variable and set it to false if somebody wins
ifgamenotover = True

#another global variable for result
winner = None

#another global variable
current_player = "X" 

#...........................................................................

def startgame(): 
  show_board()

  while ifgamenotover:
    player_turn(current_player)
    checkforwin()
    tie()
    flipturn()

#result

  if winner == "X" or winner == "O":
   print (winner + "  jeichtaann") 
  elif winner == None:
   print ("tie ra niggaahhh")

#.........................................................................


 #actual mechanism for the above function calls

#player turn function

def player_turn(player):

 print(player + "'s turn")
 position = input("enter your position : ")

#while is here to check whether the input is valid

 while position not in ["1","2","3","4","5","6","7","8","9"]:
    print ("invalid inputra bunda :[")
    print()
    position = input("type valid input: ")

 position = int(position) -1

 board[position]= player
 show_board()

#check for win function

#creating a subfunction for win and Tie

def checkforwin():

 global winner

#check the rows colums diagonals
#giving them certain names to call from if function you cannot directly check a function whether its true or false
 
 rowwinner = rowscheck()
 columnwinner = columncheck()
 diagonalwinner = diagonalcheck()

 if rowwinner:
   winner = rowwinner
 elif columnwinner:
   winner = columnwinner
 elif diagonalwinner:
   winner = diagonalwinner      
 return

def tie():
  global ifgamenotover
  if "." not in board:
    ifgamenotover = False
    winner = None
  return


#subsub function for win and tie
def rowscheck():

 global ifgamenotover

 if board[0] == board[1] == board[2] != "." :
   ifgamenotover = False
   return board[0]
 elif board[3] == board[4] == board[5] != ".":
   ifgamenotover = False
   return board[3]
 elif board[6] == board[7] == board[8] != ".":
   ifgamenotover = False
   return board[6]
   return


def columncheck():
   
 global ifgamenotover

 if board[0] == board[3] == board[6] != ".":
   ifgamenotover = False
   return[0]
 elif board[1] == board[4] == board[7] != ".":
   ifgamenotover = False
   return[3]
 elif board[2] == board[5] == board[8] != ".":
   ifgamenotover = False
   return
   return

def diagonalcheck():
 global ifgamenotover

 if board[0] == board[4] == board[8] != ".":
   ifgamenotover = False
   return[0]
 elif board[6] == board[4] == board[2] != ".":
   ifgamenotover = False
   return[6]
   return

#flip turn function

def flipturn():
 global current_player
 if current_player == "X":
   current_player = "O"
 elif current_player == "O":
   current_player = "X"
 return

startgame()

#______________________________________algorithm___________________________________________
#creating the board using some symbols [list]
#to start a game we call start function to  call all the game functions
#start function ie.start_game(): is to start the game by calling the game functions which are
  #these call functions runs on a while loop till the game gets win or tie  
    #player_turn()
    #checkforwin()
    #checkfortie()
    #flipturn()
    #result

#working of playerturn function
 #give name to players turn (player x or o)
 #get an input from the player from 1 to 9 position
 #check whether the input is valid.
 #cast the input to int
 #make the input to cast as X OR O in the given position
 #call showboard()

#working of checkforwin function
 #check for the equal rows or columns or diagonals
  #creating seperate functions for each
   #if elif rule for checking rows colums and diagonals
 #after checking and find the winner through the sub functions 
 #the main function of checkforwin will get the winner and process it to result area.

#tie function
 #use if function to check (if "." is not vailable in board:) it declares winner = None
 #the result are makes the game tie

#working of flipturn function
 #as the start game goin' on a while loop. every time it starts we should flip the player names  as X to O  ---   O to X.

# global variable concept
 #if you want to access a variable inside a function use Global "variable" in the first line of the function 
 #Global variable (here used for  true or false rule)
#Local variable can only be accessed inside the function

#and this game has overwrite inplut problem though it says a warning.
#play fair!

 #_______________________________ END OF TIC TAC TOE  _____________________________________lop=0o999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999LO