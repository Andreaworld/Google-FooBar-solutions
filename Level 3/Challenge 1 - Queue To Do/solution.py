"""from operator import xor


def solution(start, length):
    remaining_workers = length - 1
    checksum = start
    current_worker = start + 1
    while remaining_workers > 0:
        checksum = checksum ^ current_worker
        current_worker += 1
        remaining_workers -= 1
    workers_to_include = length - 1

    while workers_to_include > 0:
        remaining_workers = workers_to_include
        current_worker = start + (length * (length - workers_to_include))
        while remaining_workers > 0:
            checksum = checksum ^ current_worker
            remaining_workers -= 1
            current_worker += 1
        workers_to_include -= 1

    return checksum"""
from operator import xor


def solution(start, length):
    workers = xrange(start, start + length)
    print workers
    workers_to_exclude = 1
    checksum = reduce(xor, workers)
    starting_num = start + length

    while workers_to_exclude < length:
        workers = xrange(starting_num, (starting_num + length) - workers_to_exclude)
        print workers
        checksum = checksum ^ reduce(xor, workers)
        starting_num += length
        workers_to_exclude += 1

    return checksum



if __name__ == "__main__":
    print solution(0, 3)
    print solution(17, 4)
    print solution(5, 3)
