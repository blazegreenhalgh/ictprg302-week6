
#            0     1    2
tic_tac = [['-',  'X', 'O'],  # 0
           ['X',  '-', 'X'],  # 1
           ['O',  '-', 'O']]  # 2

# given the list above, that represents
# a tic-tac-toe board's state
# do the following:
# (1) print the middle row
print(tic_tac[1])
# (2) print the dash on the middle row
print(tic_tac[1][1])
# (3) replace one dash such that X wins
tic_tac[1][1] = "X"
print(tic_tac)
# (4) replace one dash such that O wins
tic_tac[2][1] = 'O'
print(tic_tac)
# (5) restore the board to its original state
tic_tac[1][1] = "-"
tic_tac[2][1] = '-'
print(tic_tac)

# (6) create a function that accepts a board and a tuple (x, y)
# and checks if a particular spot is unoccupied.
# for example:

def is_space_free(board, coordinates):
    x, y = coordinates
    return board[x][y] == "-"

# such that:
print(is_space_free(tic_tac, (0, 0))) # True
print(is_space_free(tic_tac, (0, 1))) # False
print(is_space_free(tic_tac, (2, 1))) # True

# (7) create a function that checks if there are
# **any** unoccupied spaces on the board.
# Return True if there are empty spaces
#  Otherwise return false.

# This surely is not the best way to do this....?
def has_free_spaces(board):
    for row in board:
        for space in row:
            if space == '-':
                return True
            else:
                continue
    return False

# for example:
print("HAS FREE SPACES?")
print(has_free_spaces(tic_tac)) # returns True

# check that the function worked by modifying the board
# to a tied state (no winner
tic_tac[0][0] = "X"
tic_tac[1][1] = "O"
tic_tac[2][1] = "X"
# now check that:
print("HAS FREE SPACES?")
print(has_free_spaces(tic_tac)) # returns False

# Challenge!

# write code to convert this string
# into the list we started with:
tic_tac = ("- X O\n" +
           "X - X\n" +
           "O - O\n"   )


tic_tac_split = tic_tac.split('\n')
tic_tac_split.pop() # Without this, there was somehow an empty space in it's own array: [['-', 'X', 'O'], ['X', '-', 'X'], ['O', '-', 'O'], [""]]
tic_tac_board = []

for string in tic_tac_split:
    tic_tac_board.append(string.split(' '))

print(tic_tac_split)
print(tic_tac_board)

# scroll down for clues:









# you can split the string by each newline like so
tic_tac.splitlines()



# need more? keep scrolling!




# you can split each line into a list like so:
tic_tac.split()


# need more? keep scrolling!



# create an empty list first:
tic_tac_list = []



# now iterate over each line in the string




# for each line append the result of the split!