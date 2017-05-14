prime_set = set([2,3,5])

def is_prime(n):
    if n in prime_set:
        return True
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    prime_set.add(n)
    return True


print 5, is_prime(5)
print 10, is_prime(10)
print 311, is_prime(311)
print 17, is_prime(17)
print 4, is_prime(4)
