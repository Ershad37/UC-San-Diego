def main():
    print(lcm(60, 100))


def gcd(a, b):
    if b == 0:
        return a
    remain = a % b
    return gcd(b, remain)


def lcm(a, b):
    gcd_a_b = gcd(a, b)

    return (a // gcd_a_b * b)


if __name__ == "__main__":
    main()