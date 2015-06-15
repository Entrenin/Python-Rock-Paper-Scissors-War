print "*******************************"
print "Hello! This is a simple game of Rock Paper Scissors!"
print "Simply enter what you want to do (Rock, Paper, Scissors) and let the game play!"
print "*******************************"
r = "rock"
p = "paper"
s = "scissors"
player1 = raw_input('Player 1 please input your choice: ')
player2 = raw_input('Player 2 please input your choice: ')
class Checkinput:
    x = False
    def __init__(test):
        if test.lower() == r | test.lower() == p | test.lower() == s:
            return True
        #if x == False:
        #    print "Exception: Invalid input string", test 
Checkinput(player1)
