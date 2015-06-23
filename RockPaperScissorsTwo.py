
r = "rock"
p = "paper"
s = "scissors"
    
print "*******************************"
print "Hello! This is a simple game of Rock Paper Scissors!"
print "Simply enter what you want to do (Rock, Paper, Scissors) and let the game play!"
print "*******************************"
player1 = raw_input('Player 1 please input your choice: ')

while(True):
    if player1.lower() == r or player1.lower() == p or player1.lower() == s:
        break
    print "Choice is not valid"
    player1 = raw_input('Player 1 please input a valid choice: ')

player2 = raw_input('Player 2 please input your choice: ')

while(True):
    if player2.lower() == r or player2.lower() == p or player2.lower() == s:
        break
    print "Choice is not valid"
    player1 = raw_input('Player 2 please input a valid choice: ')

p1 = player1.lower()
p2 = player2.lower()

if p1 == p2:
    print "Players Draw!"

elif p1 == r and p2 == s:
    print "Player 1 Wins!"

elif p1 == p and p2 == r:
    print "Player 1 Wins!"
  
elif p1 == s and p2 == p:
    print "Player 1 Wins!"
    
else:
    print "Player 2 Wins!"
