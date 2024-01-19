# Recursive solution, sort the elevators according to the major versions,
# then for all matching major versions sort according to minor versions and
# finally then for all minor versions of the matching major elevators sort
# according to revisions. If at any "version level" there isn't a number for
# that level, put that elevator to the front.

def solution(l, version_type=0):
    # If the elevator doesn't have a version number for this lever, push it
    # to the front
    answer = [elevator for elevator in l
              if len(elevator.split(".")) == version_type]
    # Sort the remaining
    sorted_elevators = [elevator for elevator in l
                        if len(elevator.split(".")) != version_type]
    sorted_elevators.sort(key=lambda x: int(get_vr(x, version_type)))

    # Either if this is the revision (or final) layer, or it is a single item,
    # we know there is nothing further to sort
    if version_type == 2 or len(sorted_elevators) == 1:
        answer.extend(sorted_elevators)
        return answer

    # Since we aren't at the revision layer, find all the matching numbers of
    # this layer and sort them according to the lower layer. We do this by
    # enumerating over the elevators, and check if the next one is a
    # different version. If so, all the previous elevators are all the
    # matching version and will then be sorted, then reset the starting point.
    # (This holds since the elevators are sorted at this version level)
    # Exempt the last element since there is no element after to check against.
    # See line after the loop for how this is handled.
    start_index = 0
    for idx, elevator in enumerate(sorted_elevators[:-1]):

        if get_vr(elevator, version_type) \
        != get_vr(sorted_elevators[idx+1], version_type):

            answer.extend(solution(sorted_elevators[start_index:idx+1],
                          version_type+1))
            start_index = idx + 1

    # When we have reached the last element, all the elements before it,
    # starting from our current start index will be all the matching
    # versions, so just sort from the start index to the end of the list
    # (just like with before, this holds since all the elevators are
    # sorted at this version level)
    answer.extend(solution(sorted_elevators[start_index:], version_type+1))

    # All the elevators at this version layer and lower are sorted.
    return answer


# Simple helper function, for reading sake and to shorten lines.
def get_vr(elevator, version_type):
    return elevator.split(".")[version_type]


if __name__ == "__main__":
    print solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0", "0.10", "0.5"])
    print solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
