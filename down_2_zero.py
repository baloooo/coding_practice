# n = raw_input().strip()
from math import sqrt
n = 1
count = 0

def fac(x):
    global count
    if x<4:
        count=count+x
        return
    # if x == 2:
    #     count+=2
    #     return
    # if x == 3:
    #     count+=3
    #     return
    y = int(sqrt(x)) + 1
    while(y>1):
       if x%y == 0:
           print "found divisor %d divides %d" % (x,y)
           x = x/y
           print "new x", x
           count+=1
           print "new count= ", count
           fac(x)
           return
       else:
           y-=1
    if y == 1:
        print "prime therefore decrementing", x
        x-=1
        count+=1
        print "new count= ", count
        fac(x)


inp = '966514 812849 808707 360422 691410 691343 551065 432560 192658 554548 27978 951717 663795 315528 522506 300432 412509 109052 614346 589115 301840 7273 193764 702818 639354 584658 208828 255463 506460 471454 554516 739987 303876 813024 118681 708473 616288 962466 55094 599778 385504 428443 646717 572077 463452 750219 725457 672957 750371 542716 87017 743756 293742 301031 939025 503398 334595 209039 191818 158563 617470 118260 176581 966721 48924 235330 200174 992221 411098 559560 117381 814728 795418 309832 943111 775314 875208 168234 933574 444474 995856 687362 543687 761831 952514 970724 611269 237583 88891 708888 387629 407891 393991 577592' 

#fac(812849)
# fac(214567)
fac(34)
print "final count", count
# for x in inp.split(' '):
#     # x = int(raw_input().strip())
#     fac(int(x))
#     print count
#     count = 0
