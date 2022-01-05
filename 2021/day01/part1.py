with open("input.txt", "r") as input_file:
    numbers = input_file.read().splitlines()
    numbers = [int(i) for i in numbers]


def solve(input_list):
    count = 0
    prev = None

    for num in input_list:
        if prev is not None and num > prev:
            count += 1
        prev = num

    return count


print(solve(numbers))
