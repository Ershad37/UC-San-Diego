def main():
    print(huge_fibonacci_number(2816213588, 239))


def get_pisano_period(m):
    prev = 0
    curr = 1
    for i in range(m * m):
        nxt = (prev + curr) % m
        prev = curr
        curr = nxt

        if prev == 0 and curr == 1:
            return i + 1


def huge_fibonacci_number(n, m):
    period = get_pisano_period(m)

    n = n % period
    if n == 0: return n
    if n == 1: return n % m

    prev, curr = 0, 1
    for _ in range(n - 1):
        nxt = (prev + curr) % m
        prev = curr
        curr = nxt
    
    return curr


if __name__ == "__main__":
    main()