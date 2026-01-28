def main():
    print(lcm(35673623, 1374658))


def lcm(a, b):
    if a > b:
        big_num = a
        small_num = b
    elif b > a:
        big_num = b
        small_num = a
    else:
        return a
    
    lcm = 1
    for i in range(2, small_num+1):
        while True:
            if big_num % i == 0 and small_num % i == 0:
                big_num //= i
                small_num //= i
                lcm *= i
            else:
                break
        if big_num == 1 or small_num == 1:
            break
    
    return lcm * big_num * small_num

if __name__ == "__main__":
    main()