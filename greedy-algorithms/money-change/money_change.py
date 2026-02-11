def main():
    print(money_change(105))


def money_change(money: int):
    min_changes = 0
    while money > 0:
        if money // 10 > 0:
            min_changes += money // 10
            money = money % 10
        elif money // 5 > 0:
            min_changes += money // 5
            money = money % 5
        else:
            min_changes += money
            money = 0

    return min_changes

    # return (money // 10) + ((money % 10)//5) + (money % 5)


if __name__ == "__main__":
    main()