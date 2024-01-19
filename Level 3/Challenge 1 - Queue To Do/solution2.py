from operator import xor



def solution(start, length):
    # Initialise variables
    checksum = 0
    workers_to_exclude = 0
    starting_num = start

    # Loop until entire queue is skipped
    while workers_to_exclude < length:
        L = cumXOR(starting_num - 1)
        R = cumXOR(starting_num + (length - 1) - workers_to_exclude)
        checksum ^= xor(L, R)
        starting_num += length
        workers_to_exclude += 1

    return checksum


def cumXOR(n):
    mod = n % 4
 
    # If n is a multiple of 4
    if mod == 0:
        return n
 
    # If n % 4 gives remainder 1
    elif mod == 1:
        return 1
 
    # If n % 4 gives remainder 2
    elif mod == 2:
        return n + 1
 
    # If n % 4 gives remainder 3
    elif mod == 3:
        return 0



if __name__ == "__main__":
    print solution(0, 3)
    print solution(17, 4)
    print solution(5, 3)
