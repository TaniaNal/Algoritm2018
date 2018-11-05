import math


class Bananas(object):
    def number(self, N, H):

        def possible(K):
            return sum(math.ceil(P / K) for P in N) <= H

        x, y = 1, max(N)
        while x < y:
            K = (x + y) / 2
            if not possible(K):
                x = K + 1
            else:
                y = K
        return x


if __name__ == '__main__':
    bananas = Bananas()
    N = [30, 11, 23, 4, 20]
    H = 6

    result = bananas.number(N, H)
    print(int(result))
