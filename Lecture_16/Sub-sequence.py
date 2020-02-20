# SUBSEQUENCE ON STRINGS
def subsq(processed, unprocessed):
    if len(unprocessed) == 0:
        print(processed)
        return
    ch = unprocessed[0]
    subsq(processed + ch,unprocessed[1:])
    subsq(processed, unprocessed[1:])

# PERMUTAIONS ON STRINGS
def permute(processed, unprocessed):
    if len(unprocessed) == 0:
        print(processed)
        return
    for i in range(len(unprocessed)):
            char = unprocessed[i]
            rec_unprocessed = unprocessed[:i] + unprocessed[i+1:]
            permute(processed + char,rec_unprocessed)

permute("","abc")
