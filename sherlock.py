def sherlock(l):
    if len(l) == 1:
        return "YES"
    total = sum(l)
    item = l[0]
    left = 0
    right = total - item
    for i in l[1:]:
        left = left + item
        item = i
        right = right - item
        if left == right:
            return "YES"
    return "NO"    

T = int(raw_input())
for i in xrange(T):
    _ = raw_input()
    l = map(int, raw_input().split(" "))
    print sherlock(l)
