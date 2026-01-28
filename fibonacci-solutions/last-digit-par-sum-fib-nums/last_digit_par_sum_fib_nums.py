def main():
    print(last_digit_par_sum_fib_nums(7, 12))


def last_digit_par_sum_fib_nums(m, n):
    m, n = m % 60, n % 60
    if n <= 1:
        return n
    prev = 0
    curr = 1
    sum_nums = 0
    for i in range(1, n+1):
        if i >= m:
            sum_nums += curr
        nxt = (prev + curr) % 10
        prev = curr
        curr = nxt
        
        
    return sum_nums % 10


if __name__ == "__main__":
    main()