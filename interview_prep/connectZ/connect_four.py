import sys

# Remove 1st argument from the
# list of command line arguments
# FYI - the first arg is the file name
connect_z_file_name = sys.argv[1:][0]

width, height, win_line_length = 0 , 0, 0
moves =[]

#corner case
#make sure the file is ASCII format
if connect_z_file_name.split(".")[1] != "ASCII":
    raise Exception("9")

try:
    with open(connect_z_file_name) as f:
        '''
        Our aim is to create the following variables
        #width, height, win_line_row = 7, 6, 4
        #moves = [1,2,1,2,1,2,1]

        We will validate the data as we go
        '''
        #create a list --> ['7 6 4', '1', '2', '1', '2', '1', '2', '1']
        content = f.read().splitlines()

        #Grab the first index. We are expecting '7 6 4' format:
        #Lets try and raise an exception is 
        try:
            board_config = content.pop(0).split(" ")
            width += int(board_config[0])
            height += int(board_config[1])
            win_line_length += int(board_config[2])
        except (IndexError, ValueError):
            raise Exception("8")

        try:
            for line in content:
                moves.append(int(line))
        except ValueError:
            raise Exception("8")

except (FileNotFoundError, OSError, Exception):
    raise Exception("9")



#We need to know what a win looks like
winning_combos = [
    "".join([ '1' for w in range(win_line_length)]), # '1111'
    "".join([ '2' for w in range(win_line_length)]) #'2222'
]



def create_board(width:int, height:int):
    '''
    We need to create a 'board'.
    This is a list of lists containing empty strings. So 3 x 3 will be:

    --> first list  ["", "", ""]
    --> second list ["", "", ""]
    --> third list  ["", "", ""]

    '''
    board = [['' for x in range(width)] for i in range(height)]
    return board

def get_column(board, index):
    '''
    Returns a column at the specified index
    '''
    return [i[index] for i in board]

def get_row(board, index):
    '''
    Returns a row at the specified index
    '''
    return board[index]

def get_diagonals():
    '''
    Returns all the diagonals in the game
    '''

    diagonals = []

    #We loop through twice to catch the positive diagonals and negative
    for i in range(height + width - 1):
        diagonals.append([])
        for j in range(max(i - height + 1, 0), min(i + 1, height)):
            diagonals[i].append(board[height - i + j - 1][j])

    for i in range(height + width - 1):
        diagonals.append([])
        for j in range(max(i - height + 1, 0), min(i + 1, height)):
            diagonals[i].append(board[i - j][j])

    return diagonals

def drop_chip(board, col, chip):
    '''
    drop a chip in the first 'row' we find
    '''
    found = 0
    for board_row in board:
        if not found and board_row[col-1] == "":
            found += 1
            board_row[col-1] += str(chip)
    
    #now print the new board
    #I've used reverse to display as a typical board
    print(f'**New board layout**')
    for row in reversed(board):
        print(row)


def before_chip_drop(board,**kwargs):
    '''
    Carry out validation before we drop a chip
    '''
    column = kwargs.get("column")
    row = kwargs.get("row")

    #corner case
    #The game can not be won if the win_line_length > width and height
    if win_line_length > width and win_line_length > height:
        raise Exception("7")

    if column:
        #Illegal column
        #Raise exception if col is < than minimum width or > than maximum width
        if (column-1) < 0 or column > width:
            raise Exception("6")

    if row:
        #Illegal row
        #1) Call set against row and raise exception if "" does not appear
        if not "" in set(board[row]):
            raise Exception("5")
    return True


def check_for_win(chips_in_row):
    '''
    We're passing through a list that 'should' have == win_line_length
    if chips_in_row < win_line_length == No win
    '''
    if len(chips_in_row) == win_line_length:
        chips_in_row = set(chips_in_row)
        #We could have a winner if chips_in_row == 1 as we have created a set
        if len(chips_in_row) == 1:
            if list(chips_in_row)[0] == "1":
                raise Exception("1")
            if list(chips_in_row)[0] == "2":
                raise Exception("2")


#Track moves taken
moves_taken = 0

def after_chip_drop(board):
    '''
    We check the board for an outcome after ach chip drop
    i.e. win/draw/incomplete

    ["A", "B", ""]
    ["B", "A", ""]
    ["A", "B", "A"]

    1) We now grad the chip names from each index and create a list
    2) Changing the list to a set and checking its length will signify a win
        --> len(chips_in_row) == 1 means that all chip are the same, therefore the last chip drop wins the game

    '''

    # Check for draw
    draw = 1
    for board_row in board:
        if "" in board_row:
            draw -= 1
    if draw > 0:
        raise Exception("0")

    # Check for incomplete
    incomplete = 1
    for board_row in board:
        if "" in board_row:
            incomplete -= 1
    if incomplete > 0:
        raise Exception("0")


    #Check rows
    for i in range(height):
        for j in range(width - 3):
            row = get_row(board, i)[j:j + 4]
            check_for_win(row)

    #Check columns
    for i in range(width):
        for j in range(height - 3):
            column = get_column(board,i)[j:j + 4]
            check_for_win(column)

    #Check diagonals
    for i in get_diagonals():
        for j, _ in enumerate(i):
            diagonal = i[j:j + 4]
            check_for_win(diagonal)

    #This catches the incomplete game code
    if moves_taken == len(moves):
        raise Exception("3")


#Create a fresh board
board = create_board(width, height)

#Calculate the chip being used
#Odd number == 1
#Even number == 2
chip_int = 1

#loop through the moves list
for column in moves:
    
    #Calculate the chip
    if (chip_int % 2) == 0:
        chip = 2
    else:
        chip = 1

    #Increase the moves taken variable each loop
    #This is used for validation purposes
    moves_taken += 1
    chip_int += 1

    if before_chip_drop(board, column = column):
        # row = get_next_open_row(board, column)
        drop_chip(board, column, chip)

        after_chip_drop(board)
