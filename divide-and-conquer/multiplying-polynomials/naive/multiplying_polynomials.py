def main():
    print(*multiplying_polynomials(n=2, a=[0,6], b=[3, 7]))


def multiplying_polynomials(n, a, b):
    result = [0] * (2 * n - 1)

    for i in range(n):
        for j in range(n):
            result[i+j] += a[i] * b[j]

    return result

if __name__ == "__main__":
    main()