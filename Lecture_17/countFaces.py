def countdDice(processed, target, faces):
    if target == 0:
        if len(processed) >= 3:   #limiting sol to path which finishes in 3 steps (can be used to print path in prev code as well)
            return 1
        else:
            return 0
    acc= 0
    for face in range(1,faces+1):
        if face > target:
            continue

        acc += countdDice(processed  + str(face), target - face, faces)
    return acc
print(countdDice("",5,3))

def ret_countdDice(processed, target, faces):
    if target == 0:
        if len(processed) >= 3:
            return [processed]
        else:
            return []
    acc= []
    for face in range(1,faces+1):
        if face > target:
            continue

        acc.extend(ret_countdDice(processed  + str(face), target - face, faces))
    return acc
print(ret_countdDice("",5,3))