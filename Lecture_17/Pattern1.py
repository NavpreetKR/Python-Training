def starDown(stars):
    if stars == 0:
        return
    for i in range(stars):
        print("*",end="")
    print()
    starDown(stars-1)

#starDown(5)

def starUp(stars):
    if stars == 0:
        return

    starUp(stars-1)
    for i in range(stars):
        print("*",end="")
    print()

#starUp(5)

def rec_starDown(row,col=0):
    if row == 0:
        return
    if col == row:
        print()
        rec_starDown(row-1,0)
        return
    print("*", end='')
    rec_starDown(row,col+1)

rec_starDown(5)

def numbers(row,col=0):
