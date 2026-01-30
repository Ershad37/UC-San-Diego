def main():
    print(min_waiting_time(t=[2, 10, 40, 3, 7, 16, 17], n=7))


def min_waiting_time(t: list[int], n):
    waiting_time = 0
    treated = [0] * n
    for i in range(n):
        t_min = 1000000000000
        index = i
        for j in range(n):
            if treated[j] == 0 and t[j] <= t_min:
                t_min = t[j]
                index = j
        waiting_time += (n - i - 1)*t_min
        treated[index] = 1

    return waiting_time


if __name__ == "__main__":
    main()