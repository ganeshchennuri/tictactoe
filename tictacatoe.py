board=[" " for i in range(9)]

player1 = input('Enter Player 1 Name : ')
player2 = input('Enter Player 2 Name : ')

def print_board():
    row1="| {} | {} | {} |".format(board[0],board[1],board[2])
    row2="| {} | {} | {} |".format(board[3],board[4],board[5])
    row3="| {} | {} | {} |".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3+'\n')

def board_game(icon):
    if icon=="X":
        name=player1
    elif icon=="O":
        name=player2
    print("Its Your Turn Player {}".format(name))
    choice=int(input("Enter your choice in 1-9 : ").strip())
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print("Entered Choice is already Allocated\n")
        board_game(icon)

def is_winner(icon):
    if board[0]==board[1]==board[2]==icon or\
       board[3]==board[4]==board[5]==icon or\
       board[6]==board[7]==board[8]==icon or\
       board[0]==board[3]==board[6]==icon or\
       board[1]==board[4]==board[7]==icon or\
       board[2]==board[5]==board[8]==icon or\
       board[0]==board[4]==board[8]==icon or\
       board[2]==board[4]==board[6]==icon:
        return True
    else:
        return False

def is_tie():
    if " " not in board:
        return True
    else:
        return False
        
while True:
    print_board()
    board_game("X")
    if is_winner("X"):
        print(f"Congratulations!! {player1} You are Winner")
        break
    if is_tie():
        print(f"{player1} X  DRAW  O {player2}")
        break
    print_board()
    board_game("O")
    if is_winner("O"):
        print(f"Congratulations!! {player2} You are Winner")
        break
    if is_tie():
        print("Game has Tied")
        break