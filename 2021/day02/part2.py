with open("input.txt", "r") as input_file:
    directions = input_file.read().splitlines()


def solve(input_text):
    x = 0
    y = 0
    aim = 0

    for instruction in input_text:
        d, n = instruction.split()
        n = int(n)

        if d == "forward":
            x += n
            y += aim * n
        elif d == "down":
            aim += n
        elif d == "up":
            aim -= n
        else:
            raise Exception("Direction not valid: {}".format(d))

    return x * y


print(solve(directions))
