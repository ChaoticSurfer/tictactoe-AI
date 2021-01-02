"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_y = 0
    for line in board:
        for place in line:
            if place == X:
                x_y += 1
            elif place == O:
                x_y -= 1

    return X if bool(x_y) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    S = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                S.add((i, j))
    return S


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print(action)
    # ---delete

    board = board.copy()
    i = action[0]
    j = action[1]
    if not board[i][j] is None:
        raise Exception("is not None ! you can't move here.....")
    board[i][j] = player(board)  # play
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        check_x_line = 0
        check_y_line = 0
        for j in range(3):
            current = board[i][j]
            current_reverse = board[j][i]

            # X
            if current == X:
                check_x_line += 1
            if current_reverse == X:
                check_y_line += 1
            # O
            if current == O:
                check_x_line -= 1
            if current_reverse == O:
                check_y_line -= 1

        # check if won
        if check_x_line == 3 or check_y_line == 3:
            return X
        elif check_x_line == -3 or check_y_line == -3:
            return O

    # diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]

    # reverese diagonal
    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return bool(all([all(i) for i in board]) or bool(winner(board)))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    Winner = winner(board)
    if Winner == X:
        return 1
    elif Winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        action = max_value(board)
    else:
        action = min_value(board)

    return action


def max_value(state):
    if terminal(state):
        return utility(state)

    options = []

    for action in actions(state):
        v = min_value(result(board=state, action=action))
        options.append((action, v))

    return (max(options, key=lambda x: x[1]))[0]


def min_value(state):
    if terminal(state):
        return utility(state)

    options = []

    for action in actions(state):
        v = max_value(result(board=state, action=action))
        options.append((action, v))

    return (min(options, key=lambda x: x[1]))[0]
