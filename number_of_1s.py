def number_of_1s(num):
    count = 0
    while(num):
        if num % 2 !=0:
            count+=1
        num = num/2
    print count
if __name__ == '__main__':
    number_of_1s(16)
