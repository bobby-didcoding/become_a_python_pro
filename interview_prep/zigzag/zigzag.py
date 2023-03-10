def zigzag(str, rows: int):

    if not str.isascii():
        raise Exception("Only English A to Z and '.' and ','")
    if not isinstance(rows, int):
        raise Exception("Only integers please")
    elif rows < 1 or rows >1000:
        raise Exception("Please use an integer min 1 and max 1000")

    # Find length of string
    sting_length = len(str)
 
    # Create list of empty strings. One for each row
    row_list=["" for x in range(rows)]
 
    # Initialize index for row_list
    row = 0
   
    # Loop through string
    #1) add char to row_list by row index
    #2) change row index
    for i in range(sting_length):
         
        # append current character
        # to current row
        try:
            row_list[row] += str[i]
        #Corner case (1 row only)
        except IndexError: 
            row_list[0] += str[i]

        #create variable in memory and only change on first or last index
        #increment if first index 
        if row == 0:
            down = True
        #decrement if last index
        if row == rows - 1:
            down = False

        #Change row int accordingly
        if down:
            row += 1
        else:
            row -= 1

    #construct new string
    result = ""
    for i in row_list:
        result += i
    return print(result)

 
# Driver Code
str = "DIDCODING"
rows = 5
zigzag(str, rows)