def get_fact(x):
    factorial = 1
    while(x>1):
        factorial *= x
        x-=1
    return factorial

def possible_paths(dest_x, dest_y):
    num = get_fact(dest_x+dest_y)
    denom1 = get_fact(dest_x)
    denom2 = get_fact(dest_y)
    return num/(denom1*denom2)

if __name__ == '__main__':
    x = 1
    y = 1
    print possible_paths(x, y)
