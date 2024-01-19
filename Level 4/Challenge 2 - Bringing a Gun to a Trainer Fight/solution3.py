from math import ceil, atan2



def solution(dimensions, your_position, trainer_position, distance):
    if (trainer_position[0] - your_position[0])**2 + (trainer_position[1] - your_position[1])**2 > distance**2:
        return 0
    elif (trainer_position[0] - your_position[0])**2 + (trainer_position[1] - your_position[1])**2 == distance**2:
        return 1

    mirror_enemies_locations = get_all_targets(dimensions, trainer_position, distance)
    mirror_selves_locations = get_all_targets(dimensions, your_position, distance)

    mirror_enemies_polars = within_distance(cart_to_polar(mirror_enemies_locations, your_position), distance)
    mirror_selves_polars = cart_to_polar(mirror_selves_locations[1:], your_position)

    results = set()
    for mirror_enemy in mirror_enemies_polars:
        is_blocked = False
        for mirror_self in mirror_selves_polars:
            if mirror_enemy[0] > mirror_self[0] and mirror_enemy[1] == mirror_self[1]:
                is_blocked = True
                break
        
        if not is_blocked:
            results.add(mirror_enemy[1])

    return len(results)


def get_all_targets(room_size, position, max_distance):
    up = []
    right = []
    left = []
    down = []
    
    max_order = max_order = int(ceil(float(max_distance) / float(min(room_size))))
    
    dx = room_size[0] - position[0]
    dy = room_size[1] - position[1]
    
    for i in range(1, max_order+1):
        right += [[room_size[0]*i + dx, position[1]]]
        left += [[-room_size[0]*i + dx, position[1]]]
        up += [[position[0], room_size[1]*i + dy]]
        down += [[position[0], -room_size[1]*i + dy]]
        
        dx = room_size[0] - dx
        dy = room_size[1] - dy
    
    all_mirror_entities = [position] + right + left + up + down
    
    for vertical in up+down:
        for horizontal in left+right:
            all_mirror_entities += [[horizontal[0], vertical[1]]]
    
    return all_mirror_entities


def within_distance(polars, distance):
    return filter(lambda m: m[0]<=distance**2, polars)


def cart_to_polar(positions, shooter):
    return map(lambda p: ((p[0] - shooter[0])**2 + (p[1] - shooter[1])**2, atan2(p[1] - shooter[1], p[0] - shooter[0])), positions)



if __name__ == "__main__":
    print "Input: [300,275], [150,150], [185,100], 500"
    print "Desired Output: 9"
    print "Actual Output: " + str(solution([300,275], [150,150], [185,100], 500))

    print "\n"

    print "Input: [300,275], [185,100], [150,150], 500"
    print "Desired Output: 9"
    print "Actual Output: " + str(solution([300,275], [185,100], [150,150], 500))

    print "\n"

    print "Input: [275,300], [100,185], [150,150], 500"
    print "Desired Output: 9"
    print "Actual Output: " + str(solution([275,300], [100,185], [150,150], 500))

    print "\n"

    print "Input: [275,300], [150,150], [100,185], 500"
    print "Desired Output: 9"
    print "Actual Output: " + str(solution([275,300], [150,150], [100,185], 500))

    print "\n"

    print "Input: [3,2], [1,1], [2,1], 4"
    print "Desired Output: 7"
    print "Actual Output: " + str(solution([3,2], [1,1], [2,1], 4))

    print "\n"

    print "Input: [3,2], [2,1], [1,1], 4"
    print "Desired Output: 7"
    print "Actual Output: " + str(solution([3,2], [2,1], [1,1], 4))

    print "\n"

    print "Input: [2,3], [1,1], [1,2], 4"
    print "Desired Output: 7"
    print "Actual Output: " + str(solution([2,3], [1,1], [1,2], 4))

    print "\n"

    print "Input: [2,3], [1,2], [1,1], 4"
    print "Desired Output: 7"
    print "Actual Output: " + str(solution([2,3], [1,2], [1,1], 4))
