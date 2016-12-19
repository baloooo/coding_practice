orig_k1, offset_k1, orig_k2, offset_k2 = [int(x) for x in raw_input().strip().split(' ')]
def jump(k1, k2):
    if k1 == k2:
        print "YES"
        return
    if offset_k1 == offset_k2:
        print "NO"
        return
    if (k1<k2 and offset_k1<offset_k2) or (k1>k2 and offset_k1>offset_k2):
        print "NO"
        return
    if (orig_k1<orig_k2 and k1>k2) or (orig_k1>orig_k2 and k1<k2):
        print "NO"
        return
    jump(k1+offset_k1, k2+offset_k2)

jump(orig_k1, orig_k2)
