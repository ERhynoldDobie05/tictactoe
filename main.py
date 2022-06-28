board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player_turn = 1
winner = 0
game_active = True
coord = 0


def check_win(player):
    # row 1
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    # row 2
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    # row 3
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    # col 1
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    # col 2
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    # col 3
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    # dia 1
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    # dia 2
    elif board[2] == player and board[4] == player and board[6] == player:
        return True


def check_tie():
    for a in board:
        if a == 0:
            return False
    return True


def draw_board():
    player_board = []
    for p in board:
        if p == 1:
            player_board.append("X")
        elif p == 2:
            player_board.append("0")
        else:
            player_board.append("-")
    print("{}|{}|{}".format(player_board[0], player_board[1], player_board[2]))
    print("-----")
    print("{}|{}|{}".format(player_board[3], player_board[4], player_board[5]))
    print("-----")
    print("{}|{}|{}".format(player_board[6], player_board[7], player_board[8]))


def game_turn():
    row = 0
    col = 0
    global player_turn
    global board
    global coord
    global game_active
    global winner
    draw_board()
    if player_turn == 1:
        print("It is X's turn")
    else:
        print("It is O's turn")
    while row < 1 or row > 4 or col < 1 or col > 4 or board[coord] != 0:
        try:
            row = int(input("Which row? (1 - 3) "))
            col = int(input("Which column? (1 - 3) "))
        except ValueError:
            print("Please enter numbers only!")
            continue
        coord = 3 * (row - 1) + (col - 1)
        if row < 1 or row > 4 or col < 1 or col > 4:
            print("Inputs must be 1-3")
            continue
        if board[coord] != 0:
            print("Already played! Choose a different spot.")
            continue
    board[coord] = player_turn
    if check_win(player_turn) is True:
        game_active = False
        winner = player_turn
        return
    if check_tie() is True:
        game_active = False
        return
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1


while game_active is True:
    game_turn()

draw_board()
if winner == 0:
    print("The game was tied. No one wins.")
elif winner == 1:
    print("X's wins!")
elif winner == 2:
    print("O's wins!")
else:
    print("Something has gone horribly wrong! The world may be ending or your computer may be broken!")
