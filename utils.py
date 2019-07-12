def chunker(target_str, size):
    '''
    break a given string/list to chunks of asked size
    returns a list of these breaks
    '''
    return [target_str[pos: pos+size] for pos in range(0, len(target_str), size)]