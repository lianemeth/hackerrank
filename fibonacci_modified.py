a, b, n = [int(i) for i in raw_input().split(" ")]
for i in range(n-2):
    a,b = b, b*b+a
print b
