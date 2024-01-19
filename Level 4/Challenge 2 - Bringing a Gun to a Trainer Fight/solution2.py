import math

def solution(dimensions, your_position, trainer_position, distance):
    width, height = dimensions
    your_x, your_y = your_position
    trainer_x, trainer_y = trainer_position

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(dx, dy):
        common_divisor = gcd(dx, dy)
        return (dx // common_divisor, dy // common_divisor)

    def visible_points(x, y):
        dx = trainer_x - x
        dy = trainer_y - y

        if dx == 0 and dy == 0:
            return set()

        dx, dy = simplify_fraction(dx, dy)

        points = set()
        while True:
            x += dx
            y += dy
            if x < 0 or x > width or y < 0 or y > height:
                break
            points.add((x, y))

        return points

    seen_points = set()
    for x in range(width + 1):
        for y in range(height + 1):
            if (x - your_x) ** 2 + (y - your_y) ** 2 <= distance ** 2:
                seen_points |= visible_points(x, y)

    return len(seen_points)



if __name__ == "__main__":
    print "Input: [300,275], [150,150], [185,100], 500"
    print "Desired Output: 9"
    print "Actual Output: " + str(solution([300,275], [150,150], [185,100], 500))

    print "\n"

    print "Input: [3,2], [1,1], [2,1], 4"
    print "Desired Output: 9"
    print "Actual Output: " + str(solution([3,2], [1,1], [2,1], 4))
