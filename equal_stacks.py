s1_len, s2_len, s3_len = [int(x) for x in raw_input().strip().split(' ')]

s1 = [int(x) for x in raw_input().strip().split(' ')]
s2 = [int(x) for x in raw_input().strip().split(' ')]
s3 = [int(x) for x in raw_input().strip().split(' ')]
s1_sum = sum(s1)
s2_sum = sum(s2)
s3_sum = sum(s3)
while not(s1_sum==s2_sum == s3_sum):
    max_sum = max(s1_sum, s2_sum, s3_sum)
    if max_sum == s1_sum:
        s1_sum-=s1.pop(0)
    if max_sum == s2_sum:
        s2_sum-=s2.pop(0)
    if max_sum == s3_sum:
        s3_sum-=s3.pop(0)

print s1_sum

