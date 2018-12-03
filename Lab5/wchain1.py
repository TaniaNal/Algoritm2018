def read_input():
    with open("wchain.in", "r") as input_file:
        number = int(input_file.readline())
        words = []
        for line in input_file:
            words.append(line.split()[0])
        return words, number


def construct_dict(A):
    global order_d
    dictionary = {}
    for x in A:
        key, val = len(x), x
        if key in dictionary.keys():
            dictionary[key].append(val)
        else:
            dictionary[key] = [val]
        order_d = sorted(dictionary.keys())
    return dictionary, order_d


def check_str(string1, string2):
    it1 = iter(string1)
    it2 = iter(string2)
    count_diffs = 0
    c1 = next(it1, None)
    c2 = next(it2, None)
    while True:
        if c1 != c2:
            if count_diffs: return False
            count_diffs = 1
            c1 = next(it1)
        else:
            try:
                c1 = next(it1)
                c2 = next(it2)
            except StopIteration:
                return True


def solve(A):
    words, order_words = construct_dict(A)
    solution = {order_words[0]: [1] * len(words[order_words[0]])}

    g_max = 1

    for l in order_words[1:]:

        solution[l] = []
        for w in words[l]:
            tmp = []
            if l - 1 in words.keys():
                for i in range(0, len(words[l - 1])):
                    if check_str(w, words[l - 1][i]):
                        tmp.append(solution[l - 1][i] + 1)
                    else:
                        tmp.append(solution[l - 1][i])
                solution[l].append(max(tmp))
            else:
                solution[l] = [1] * len(words[l])
        if max(solution[l]) >= g_max:
            g_max = max(solution[l])
    return g_max


if __name__ == "__main__":
    words, number = read_input()
    result = solve(words)
    print(result)
