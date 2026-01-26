def main():
    print(last_digit_fibonacci(3))


def last_digit_fibonacci(n: int):
    prev = 0
    current = 1
    for i in range(n - 1):
        nxt = prev + current
        prev = current
        current = nxt

    return current % 10


if __name__ == "__main__":
    main()