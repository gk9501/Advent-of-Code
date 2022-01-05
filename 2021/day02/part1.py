with open("input.txt", "r") as input_file:
    directions = input_file.read().splitlines()


def solve(input_text):
    x = 0
    y = 0

    for instruction in input_text:
        d, n = instruction.split()
        n = int(n)

        if d == "forward":
            x += n
        elif d == "down":
            y += n
        elif d == "up":
            y -= n
        else:
            raise Exception("Direction not valid: {}".format(d))

    return x * y


print(solve(directions))
