import tictactoe
from tictactoe import *

init = initial_state()

state = [["", "s", "O"], ["D", "O", "X"], ["O", "X", "O"]]

print(winner(state))