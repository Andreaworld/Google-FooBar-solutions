def solution(n):
    answer = 0
    current_number = int(n)

    while current_number > 1:
        if current_number % 2 == 0:
            current_number /= 2
        elif current_number == 3 or current_number % 4 == 1:
            current_number -= 1
        else:
            current_number += 1
        answer += 1
    
    return answer



if __name__ == "__main__":
    print solution('15')
    print solution('4')
    print solution('13')
