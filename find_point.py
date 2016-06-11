n = int(raw_input())
for i in range(n):
    px,py,qx,qy = [int(i) for i in raw_input().split(" ")]
    sx, sy = 2* qx - px, 2* qy - py
    print sx, sy
