
#Comment:  W02 Prove: Developer - Solo Code Submission
# Author CSE210, Jason McLaughlin
def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(36):
        board.append(square + 1)
    return board
    # def display_board presents a 6 x 6 grid, with | and -+ lines as separations.  Need to format 0-9 in two digits
    # for better spacing of grid.
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}|{board[ 3]}|{board[ 4]}|{board[ 5]}")
    print('-+-+-+-+-+-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}|{board[9]}|{board[10]}|{board[11]}")
    print('-+-+-+-+-+-+-+-')
    print(f"{board[12]}|{board[13]}|{board[14]}|{board[15]}|{board[16]}|{board[17]}")
    print('-+-+-+-+-+-+-+-')
    print(f"{board[18]}|{board[19]}|{board[20]}|{board[21]}|{board[22]}|{board[23]}")
    print('-+-+-+-+-+-+-+-')
    print(f"{board[24]}|{board[25]}|{board[26]}|{board[27]}|{board[28]}|{board[29]}")
    print('-+-+-+-+-+-+-+-')
    print(f"{board[30]}|{board[31]}|{board[32]}|{board[33]}|{board[34]}|{board[35]}")
    print()
    
def is_a_draw(board):
    for square in range(36):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    # def has-winner is used to determine 6 in a row first horizonal, then vertical, then 2 possible diagonal.
def has_winner(board):
    return (board[0] == board[1] == board[2] == board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] == board[9] == board[10] == board[11] or
            board[2] == board[13] == board[14] == board[15] == board[16] == board[17] or
            board[18] == board[19] == board[20] == board[21] == board[22] == board[23] or
            board[24] == board[25] == board[26] == board[27] == board[28] == board[29] or
            board[30] == board[31] == board[32] == board[33] == board[34] == board[35] or
            board[0] == board[6] == board[12] == board[18] == board[24] == board[30] or
            board[1] == board[7] == board[13] == board[19] == board[25] == board[31] or
            board[2] == board[8] == board[14] == board[20] == board[26] == board[32] or
            board[3] == board[9] == board[15] == board[21] == board[27] == board[33] or
            board[4] == board[10] == board[16] == board[22] == board[28] == board[43] or
            board[5] == board[11] == board[17] == board[23] == board[29] == board[35] or
            board[1] == board[8] == board[15] == board[22] == board[29] == board[36] or
            board[6] == board[11] == board[16] == board[21] == board[26] == board[31])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-36): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()