with open("input.txt", "r") as input_file:
    numbers = input_file.read().splitlines()
    numbers = [int(i) for i in numbers]


def solve(input_list):
    count = 0
    prev = (None, None, None)

    for num in input_list:
        if prev[0] is not None and num > prev[0]:
            count += 1
        prev = (prev[1], prev[2], num)

    return count


print(solve(numbers))
