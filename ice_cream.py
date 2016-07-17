def ice_cream(l, m):
    l = [(j,k) for j,k in enumerate(l, 1)]
    l.sort(key = lambda i: i[1])
    lo = 0
    hi = len(l) - 1
    while lo <= hi:
        summ = l[lo][1] + l[hi][1]
        if summ == m:
            result = [l[lo][0], l[hi][0]]
            result.sort()
            return result
        if summ > m:
            hi = hi - 1
        else:
            lo = lo + 1
    return -1, -1

T = int(raw_input().strip())
for a0 in xrange(T):
    m = int(raw_input().strip())
    _ = raw_input()
    l = map(int,raw_input().strip().split(' '))
    print " ".join(map(str, ice_cream(l, m)))
