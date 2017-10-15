#!/bin/python

def calculate_sums(h):
    h = h[::-1]
    sum_h = [h[0]]
    aux = h[0]
    for el in h[1:]:
        aux = el + aux
        sum_h.append(aux)
    return sum_h[::-1]


def calculate_max_equal_stack(h1, h2, h3):
    sum_h1 = calculate_sums(h1)
    sum_h2 = calculate_sums(h2)
    sum_h3 = calculate_sums(h3)
    height_count = {}
    possible_answer = []
    for elem in sum_h1 + sum_h2 + sum_h3:
        if elem in height_count:
            height_count[elem] += 1
            if height_count[elem] == 3:
                possible_answer.append(elem)
        else:
            height_count[elem] = 1
    if possible_answer:
        return max(possible_answer)
    else:
        return 0
    

if __name__ == "__main__":
    n1,n2,n3 = raw_input().strip().split(' ')
    n1,n2,n3 = [int(n1),int(n2),int(n3)]
    h1 = map(int,raw_input().strip().split(' '))
    h2 = map(int,raw_input().strip().split(' '))
    h3 = map(int,raw_input().strip().split(' '))
    print calculate_max_equal_stack(h1, h2, h3)
