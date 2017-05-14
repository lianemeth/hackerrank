
def counting_sort(max_value, numbers):
    count_list = [0 for i in xrange(max_value)]
    for number in numbers:
        count_list[number] += 1
    sorted_list = []
    for item, n_of_times in enumerate(count_list):
        sorted_list += [item for i in xrange(n_of_times)]
    return sorted_list


if __name__ == "__main__":
    _ = raw_input()
    numbers = [int(i) for i in raw_input().split(' ')]
    count_list = counting_sort(100, numbers)
    print ' '.join([str(i) for i in count_list])
