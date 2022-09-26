print('Welcome to the game!')
user1=input('User 1: ')
user2=input('User 2: ')

print(f"{user1} is assigned X")
print(f"{user2} is assigned O")

def checkWin(sol):

    # Method 1: 3 X or O in the same row
    for el in sol:
        if el[0]==el[1]==el[2]:
            return el[0]

    # Method 2: 3 X or O in the same column
    for i in range(3):
        if sol[0][i]==sol[1][i]==sol[2][i]:
            return sol[0][i]

    # Method 3: 3 X or O in the same diagnal
    if sol[0][2] == sol[1][1] == sol[2][0] or sol[0][0] == sol[1][1] == sol[2][2]:
        return sol[1][1]

    return False;

def displayGame(twod):
    for el in twod:
        for i in el:
          print(i, end=' | ');
        print('\n----------')
    
def playGame():

    board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

    displayGame(board) #Display botr before starting the game

    for i in range(9):

        if(not(i%2)):
            enteredEl=int(input(f"{user1}'s turn:\n Enter a number from the board: ")) 
        else:
            enteredEl=int(input(f"{user2}'s turn:\n Enter a number from the board: "))

        num=enteredEl-1         
        presentEl=board[num//3][num%3]
        if presentEl==enteredEl and (presentEl!='X' or presentEl!='O'):
            board[num//3][num%3] ='O' if i%2 else 'X'

        displayGame(board)

        if checkWin(board)=='X':
            print(f"{user1.upper()} IS THE WINNER!!")
            break
        elif checkWin(board)=='O':
            print(f"{user2.upper()} IS THE WINNER!!")
            break

playGame()