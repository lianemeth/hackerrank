def twins(lower_limit, upper_limit):
    array = [True] * (upper_limit + 1)
    array[0] = array[1] = False
    
    for (i, isprime) in enumerate(array):
        if isprime:
            for n in xrange(i*i, len(array), i):
                array[n] = False
    count = 0
    for i in range(lower_limit, len(array) - 2):
        if i + 2 < upper_limit and array[i] and array[i + 2]:
            count += 1
    return count

if __name__ == "__main__":
    n, m = raw_input().split(' ')
    n, m = int(n), int(m)
    primes = twins(n, m+1)
    print primes
