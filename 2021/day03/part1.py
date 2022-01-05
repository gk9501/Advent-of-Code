with open("input.txt", "r") as input_file:
    report = input_file.read().splitlines()


def solve(input_list):
    input_str = "".join(input_list)
    num_bits = len(input_list[0])
    gamma = ""
    epilson = ""

    for i in range(num_bits):
        bit = input_str[i::num_bits]
        max_count = str(max(bit, key=bit.count))
        min_count = str(min(bit, key=bit.count))
        gamma += max_count
        epilson += min_count

    return int(gamma, 2) * int(epilson, 2)


print(solve(report))
