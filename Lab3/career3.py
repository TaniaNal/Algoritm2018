def read_data():
    with open('career.in', 'r') as input_file:
        levels_number = int(input_file.readline())
        arr = []
        for line in input_file:
            arr.append([int(x) for x in line.rstrip('\n').split()])
        return levels_number, arr


if __name__ == '__main__':
    levels_number, experiences = read_data()

    for y in range((len(experiences) - 2), -1, -1):
        for x in range(len(experiences[y])):
            left = experiences[y + 1][x]
            right = experiences[y + 1][x + 1]
            best = max(left, right)
            experiences[y][x] += best

    solution = experiences[0][0]

    print(solution)
