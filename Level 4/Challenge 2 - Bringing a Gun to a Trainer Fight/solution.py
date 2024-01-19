import math



def solution(start, end, room_size, max_distance):
    suitable_angles = 0

    for angle_of_incidence in range(0, 360, 5):
        angle_rad = math.radians(angle_of_incidence)
        
        # Calculate the initial vector components
        #print "Degrees: " + str(angle_of_incidence) + " | Radians:" + str(angle_rad / math.pi)
        vector_x = math.cos(angle_rad)
        vector_y = math.sin(angle_rad)
        #print (vector_x, vector_y)

        current_point = start
        distance_travelled = 0
        
        while distance_travelled < max_distance:
            if round(vector_x, 10) == 0:
                if abs(end[1] - start[1]) < max_distance and math.copysign(1, end[1] - start[1]) == math.copysign(1, vector_y) and end[0] == start[0]:
                    suitable_angles += 1
                continue
            elif round(vector_y, 10) == 0:
                if abs(end[0] - start[0]) < max_distance and math.copysign(1, end[0] - start[0]) == math.copysign(1, vector_x) and end[1] == start[1]:
                    suitable_angles += 1
                continue
            
            distance_to_wall_x = ((end[0] / 2) + math.copysign(end[0] / 2, vector_x)) - current_point[0]
            distance_to_wall_y = ((end[1] / 2) + math.copysign(end[1] / 2, vector_y)) - current_point[1]
            # Find the next wall hit and update the current point
            min_distance = min(x_distance / abs(vector_x) if vector_x != 0 else float('inf'),
                                y_distance / abs(vector_y) if vector_y != 0 else float('inf'))
            current_point = (current_point[0] + min_distance * vector_x, current_point[1] + min_distance * vector_y)
            
            vector_x = -vector_x if x_distance < y_distance else vector_x
            vector_y = -vector_y if y_distance < x_distance else vector_y
            
            # Break if the path has exceeded max distance or goes out of bounds
            if min_distance * max_distance >= max_distance or not (0 <= current_point[0] <= room_size[0] and 0 <= current_point[1] <= room_size[1]):
                break
            
            # Append the angle if the path reaches close to the end point
            if end[0] - current_point[0] == 0 and end[1] - current_point[1] == 0:
                suitable_angles += 1
                
    return suitable_angles



if __name__ == "__main__":
    print "Input: [300,275], [150,150], [185,100], 500"
    print "Desired Output: 9"
    print "Actual Output: " + str(solution([300,275], [150,150], [185,100], 500))

    print "\n"

    print "Input: [3,2], [1,1], [2,1], 4"
    print "Desired Output: 9"
    print "Actual Output: " + str(solution([3,2], [1,1], [2,1], 4))
