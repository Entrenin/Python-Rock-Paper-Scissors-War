
r = "rock"
p = "paper"
s = "scissors"
    
#Checks if inputed values (player choice) is valid
def validRPS(playerChoice):
    if playerChoice.lower() == r or playerChoice.lower() == p or playerChoice.lower() == s:
        return True;
    else:
        return False;

#The actual choosing of the "winner" of the game
def whoWinsRPS(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()

    if p1 == p2:
        return "Players Draw!"

    if p1 == r and p2 == s:
        return "Player 1 Wins!"

    if p1 == p and p2 == r:
        return "Player 1 Wins!"
      
    if p1 == s and p2 == p:
        return "Player 1 Wins!"
        
    return "Player 2 Wins!"
    
#Main class should be fairly obvious what it does, sets up and executes other classes
def main():
    print "*******************************"
    print "Hello! This is a simple game of Rock Paper Scissors!"
    print "Simply enter what you want to do (Rock, Paper, Scissors) and let the game play!"
    print "*******************************"
    player1 = raw_input('Player 1 please input your choice: ')

    while( not validRPS(player1)):
        print "Choice is not valid"
        player1 = raw_input('Player 1 please input a valid choice: ')

    player2 = raw_input('Player 2 please input your choice: ')

    while( not validRPS(player2)):
        print "Choice is not valid"
        player1 = raw_input('Player 2 please input a valid choice: ')

    print whoWinsRPS(player1, player2)


main()
