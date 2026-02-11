def main():
    print(money_change_denominations(money=8, denominations=[1, 4, 6]))


def money_change_denominations(money: int, denominations: list[int]):
    min_coins = 0
    for i in range(len(denominations) - 1, -1, -1):
        if denominations[i] != 1 and money % denominations[i] == 0:
            min_coins = money // denominations[i]
            if min_coins <= len(denominations) - 1:
                return min_coins
    
    n = len(denominations)
    return (money // denominations[n - 1]) + ((money % denominations[n - 1])//denominations[n -2]) + (money % denominations[n - 2])


if __name__ == "__main__":
    main()