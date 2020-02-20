def countSbsq(processed,unprocessed,count=0):
    if len(unprocessed) == 0:
        if len(processed) == 0:    # since at last base case both processed as well a unprocessed'll be 0
            return 0
        else:
            return 1

    ch = unprocessed[0]

    left  = countSbsq(processed + ch, unprocessed[1:])
    right = countSbsq(processed, unprocessed[1:])
    return left + right
res = countSbsq("","abc")
#print(res)

def ret_subsq(processed, unprocessed):
    if len(unprocessed) == 0:
        if len(processed) == 0:
            return []
        return [processed]

    ch = unprocessed[0]
    acc = []
    acc.extend(ret_subsq(processed + ch,unprocessed[1:]))
    acc.extend(ret_subsq(processed, unprocessed[1:]))

    return acc

print(ret_subsq("","abc"))