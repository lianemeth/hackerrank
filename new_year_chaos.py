#!/bin/python

import sys

def new_year_chaos(l):
    for i in range(len(l)-1, -1, -1):
        if l[i] - i -1 > 2:
            return "Too chaotic"
    changed = True
    total = 0
    while changed:
        changed = False
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                total += 1
                changed = True
    return total

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    print new_year_chaos(q)
