
def permute(string, start, end):
    if end=start+1:
        string[start], string[end] = string[end], string[start]
        return
    permute(string, start+1, end)

