def main():
    print(fibonacci_numbers(n=10))

def fibonacci_numbers(n: int):
    prev = 0
    current = 1
    for i in range(n - 1):
        nxt = prev + current
        prev = current
        current = nxt
    
    return current


if __name__ == "__main__":
    main()