# A mouse is smart enough to figure out that moving merely horizontal n vertically will lead to the food in a 2D space.
def mazeWD(processed,row, col):
    if row == 0 and col == 0:
        print(processed)
        return
    if row > 0:
        mazeWD(processed + "V", row-1,col)
    if col > 0:

        mazeWD(processed + "H", row,col-1)
    if row > 0 and col > 0:
        mazeWD(processed + "D", row-1,col-1)
mazeWD("",2,2)