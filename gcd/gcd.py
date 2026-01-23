def main():
    print(gcd(2789345, 1376480))


def gcd(n: int, m: int):
    if m == 0:
        return n
    remain = n % m
    return gcd(m, remain)


if __name__ == "__main__":
    main()