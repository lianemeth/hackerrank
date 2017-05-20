
def max_hourglass(a):
    i,j = 0,0
    max_hourglass = None
    while j+2 <= 5:
        hourglass = a[j][i] + a[j][i+1] + a[j][i+2]
        hourglass = hourglass + a[j+1][i+1]
        hourglass = hourglass + a[j+2][i] + a[j+2][i+1] + a[j+2][i+2]
        if hourglass > max_hourglass or max_hourglass is None:
            max_hourglass = hourglass
        i += 1
        if i + 2 > 5:
            i = 0
            j += 1
    return max_hourglass

if __name__ == "__main__":
    arr = []
    for arr_i in xrange(6):
        arr_temp = map(int, raw_input().strip().split(' '))
        arr.append(arr_temp)
    print max_hourglass(arr)
