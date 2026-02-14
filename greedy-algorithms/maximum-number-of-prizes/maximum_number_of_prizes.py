def main():
    print(*maximum_number_of_prizes(39))


def maximum_number_of_prizes(n: int):
    sum_prizes = 0
    prizes = []
    if n == 0:
        return 0

    prize = 1
    while sum_prizes < n:
        if n - (sum_prizes + prize) == 0:
            prizes.append(prize)
            return prizes
        elif n - (sum_prizes + prize) > prize:
            sum_prizes += prize
            prizes.append(prize)
        prize += 1

    return prizes


if __name__ == "__main__":
    main()