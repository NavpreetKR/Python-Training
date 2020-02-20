#returns the lcs of 2 strings
def lcs(first,second):
    l = []
    if len(first) == 0 or len(second) == 0:
        return 0

    if first[0] == second[0]:
        return 1 + lcs(first[1:],second[1:])

    else:
        left = lcs(first[1:],second)
        right = lcs(first,second[1:])
        return max(left,right)


res= lcs("aman","manan")
#print(res)

def ret_lcs(first,second):
    l = []
    if len(first) == 0 or len(second) == 0:
        return 0,""

    if first[0] == second[0]:
        count, max_yet = ret_lcs(first[1:],second[1:])
        return count+1, first[0] + max_yet   # function is returning an int & a string

    else:
        left_c, left_yet = ret_lcs(first[1:],second)
        right_c, right_yet = ret_lcs(first,second[1:])
        if left_c > right_c:
            return left_c, left_yet
        else:
            return right_c,right_yet
res= ret_lcs("aman","manan")
#print(res)

def list_lcs(first,second):
    if len(first) == 0 or len(second) == 0:
        return 0,[""]

    if first[0] == second[0]:
        total_c, yet = list_lcs(first[1:],second[1:])
        return total_c+1, [first[0]+item for item in yet]   # function is returning an int & a string

    else:
        left_c, left_yet = list_lcs(first[1:],second)
        right_c, right_yet = list_lcs(first,second[1:])
        if left_c > right_c:
            return left_c, left_yet
        elif left_c < right_c:
            return right_c,right_yet
        else:
            return left_c,left_yet + right_yet

max_len, items = list_lcs("aman","manan")
print(max_len,set(items))