INF = 1000000001


def read_input():
    raw_data = open('game.in', 'r').read().split('\n')

    n = int(raw_data[0].split()[0])
    m = int(raw_data[0].split()[1])

    client = list(map(int, raw_data[1].split()))
    edges = [[int(i) for i in edge.split()] for edge in raw_data[2:]]

    return n, m, edges, client


def init_matrix(n, m, edges):
    matrix = []

    for i in range(n):
        initial_values = [INF] * n
        matrix.append(initial_values)
        matrix[i][i] = 0

    for i in range(m):
        matrix[edges[i][0] - 1][edges[i][1] - 1] = edges[i][2]
        matrix[edges[i][1] - 1][edges[i][0] - 1] = edges[i][2]

    return matrix


def calculate_all_summary_latency(n, matrix):
    new_matrix = matrix[:][:]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if new_matrix[i][k] < INF and new_matrix[k][j] < INF:
                    new_matrix[i][j] = min(new_matrix[i][j], new_matrix[i][k] + new_matrix[k][j])

    return new_matrix


def main():
    n, m, edges, client = read_input()
    matrix = init_matrix(n, m, edges)
    routers = list(set(range(1, n + 1)) - set(client))

    all_routes_with_latencies = calculate_all_summary_latency(n, matrix)
    result = INF

    for i in routers:
        result = min([result, max([all_routes_with_latencies[i - 1][j - 1] for j in client])])

    print(result)


if __name__ == '__main__':
    main()
