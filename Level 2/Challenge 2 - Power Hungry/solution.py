def solution(xs):
    # This separates the positive and negative integers into
    # separate lists since they will be handled in slightly
    # different ways when calculating the product
    positive_integers = filter((lambda x: x >= 1), xs)
    negative_integers = filter((lambda x: x <= -1), xs)

    # Quick check for a certain trivial case that would cause 
    # an error with the way I am handling things. If there is
    # no positive integers and only one negative integer, then
    # the trivial answer (just the max number of the list) would
    # not be caught.
    if len(positive_integers) == 0 \
            and len(negative_integers) <= 1:
        return str(max(xs))

    # Given the previous case isn't true, the answer then would
    # be the product of all the positive integers (if any) times
    # the product of all the negative integers except of the
    # absolute smallest one if there are an odd amount of negative
    # integers (if there are any). 
    answer = 1

    if len(positive_integers) > 0:
        answer *= reduce((lambda x, y: x * y), positive_integers)

    if len(negative_integers) > 1:
        answer *= reduce((lambda x, y: x * y), negative_integers)
        if len(negative_integers) % 2 != 0:
            answer /= max(negative_integers)
    
    # Return the string version of the answer
    return str(answer)

if __name__ == "__main__":
    print solution([2, 0, 2, 2, 0])
    print solution([-2, -3, 4, -5])
