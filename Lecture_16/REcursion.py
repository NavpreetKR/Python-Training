# power of a number
def pow(n,p):
    if p == 0:
        return 1
    else:
        proc = pow(n,p-1)
        return n * proc

print(pow(2,10))