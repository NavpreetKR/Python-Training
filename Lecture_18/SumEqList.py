# given a list of items. return two sub lists whose individual sum is equal
def eq_sum_list(unprocessed, first=(), second=()):
    if len(unprocessed) == 0:
        if sum(first) == sum(second):
            print(first, second)

        return
    item = unprocessed[0]         # indexing can be used here too to minimize the cost
    eq_sum_list(unprocessed[1:], first + (item,), second)
    eq_sum_list(unprocessed[1:], first, second + (item,))


def eq_sum_list_eff(unprocessed, first=[], second=[]):    # cost efficient for the sub lists
    if len(unprocessed) == 0:
        if sum(first) == sum(second):
            print(first, second)

        return
    item = unprocessed[0]
    first.append(item)
    eq_sum_list_eff(unprocessed[1:], first, second)
    first.pop()

    second.append(item)
    eq_sum_list_eff(unprocessed[1:], first, second)
    second.pop()

def eq_sum_list_effUn(unprocessed, index =0, first=[], second=[]):     # cost efficient for unprocessed as well as f&s
    if len(unprocessed) == index:
        if sum(first) == sum(second):
            print(first, second)

        return
    item = unprocessed[index]
    first.append(item)
    eq_sum_list_effUn(unprocessed,index +1, first, second)
    first.pop()

    second.append(item)
    eq_sum_list_effUn(unprocessed,index + 1, first, second)
    second.pop()
eq_sum_list_effUn((1,2,3))