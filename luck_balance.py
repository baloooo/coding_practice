n, k = [int(x) for x in raw_input().strip().split(' ')]
total_luck = 0
imp_contests = []
for x in xrange(n):
    luck, imp = [int(x) for x in raw_input().strip().split(' ')]
    if imp == 0:
        total_luck+=luck
    else:
        imp_contests.append(luck)

imp_contests.sort(reverse=True)
for i in xrange(k):
    total_luck+=imp_contests[i]

for i in xrange(k, len(imp_contests)):
    total_luck-=imp_contests[i]

print total_luck
