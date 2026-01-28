def main():
    print(josephus(11, 3))


def josephus(n, k):
    if k == 2:
        m = 1
        while (2 ** m) <= n:
            m += 1
        m -= 1
        if n == 2 ** m:
            return 0
        else:
            remain = n - (2 ** m)
            return ((2*remain) + 1) + 1
    else:
        res = 0
        for i in range(1, n+1):
            res = (res + k) % i
        return res 
    

if __name__ == "__main__":
    main()