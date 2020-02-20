def countPermute(processed, unprocessed):
    if len(unprocessed) == 0:
        return 1
    acc = 0
    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        rec = unprocessed[:i] + unprocessed[i+1:]
        acc += countPermute(processed + ch, rec)
    return acc
res = countPermute("","abc")
print(res)

def countPermute(processed, unprocessed):
    if len(unprocessed) == 0:
        return [processed]
    acc = []
    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        rec = unprocessed[:i] + unprocessed[i+1:]
        acc.extend(countPermute(processed + ch, rec))
    return acc
res = countPermute("","abc")
print(res)