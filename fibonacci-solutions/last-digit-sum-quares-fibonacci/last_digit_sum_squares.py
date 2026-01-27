def main():
    print(last_digit_sum_squares(34786238495274148))


def last_digit_sum_squares(n):
    if n <= 1:
        return n

    def last_digit(n):
        a = 0
        b = 1
        for i in range(1, n):
            c = (a + b) % 60
            a = b
            b = c

        return b

    k = n % 60
    fib_n = last_digit(k)
    fib_n_next = last_digit(k + 1) % 60

    return (fib_n * fib_n_next) % 10


if __name__ == "__main__":
    main()
