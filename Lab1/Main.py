import time

from Car import Car


def quick_sort(list):
    exchanges = 0
    comparisons = 0

    def partition(begin, end):
        exchanges = 0
        comparisons = 0
        if end - begin < 1:
            return
        left = begin + 1
        right = end
        pivot = list[begin].power
        while True:
            while list[left].power > pivot and left < end:
                left += 1
                comparisons += 1

            while not list[right].power > pivot and right > begin:
                right -= 1
                comparisons += 1

            if left >= right:
                break

            list[left], list[right] = list[right], list[left]
            exchanges += 1
        list[begin], list[right] = list[right], list[begin]
        exchanges += 1
        partition(begin, right - 1)
        partition(right + 1, end)

    partition(0, len(list) - 1)
    print("Comparisons: " + str(comparisons))
    print("Swaps: " + str(exchanges))
    return list


def selection_sort(list):
    comparisons = 0
    swaps = 0
    n = len(list)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if list[j].max_speed < list[min_index].max_speed:
                comparisons += 1
                min_index = j
        list = swap(list, i, min_index)
        swaps += 1
    print("Comparisons: " + str(comparisons))
    print("Swaps: " + str(swaps))
    return list


def swap(list, i, min_index):
    tmp = list[i]
    list[i] = list[min_index]
    list[min_index] = tmp
    return list


if __name__ == "__main__":
    car_list = []
    car_power = 0
    car_brand = 1
    car_speed = 2
    file = open('car.txt')
    for line in file:
        values = line.split(',')
        car = Car(int(values[car_power]), values[car_brand], int(values[car_speed][:-1]))
        car_list.append(car)

    print("Selection sort")
    start_time = time.perf_counter()
    selection_sort(car_list)
    print("Time: " + str(time.perf_counter() - start_time))
    for car in car_list:
        print(car)

    print("\nQuick sort")
    quick_sort(car_list)
    start_time = time.perf_counter()

    print("Time: " + str(time.perf_counter() - start_time))
    for car in car_list:
        print(car)
