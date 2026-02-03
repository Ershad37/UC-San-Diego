def main():
    result = maximize_loot(price=[40, 44, 49, 32], weight=[5, 4, 7, 8], bag=9)
    print(f"best price: {result[0]}")
    print(f"the weight: {result[1]}")


def maximize_loot(price: list[int], weight: list[int], bag: int):
    total_price = 0
    loots = [0] * len(price)
    
    while bag != 0:
        most_valuable = None
        for i in range(len(price)):
            if most_valuable == None:
                most_valuable = i
            elif price[most_valuable] // weight[most_valuable] < price[i] // weight[i] and loots[i] == 0:
                most_valuable = i

        if bag >= weight[most_valuable]:
            loots[most_valuable] = weight[most_valuable]
            total_price += price[most_valuable]
            bag -= weight[most_valuable]
        elif bag < weight[most_valuable]:
            loots[most_valuable] = bag
            total_price += (price[most_valuable] // weight[most_valuable]) * bag
            bag -= bag
    
    return total_price, loots

        

                

if __name__ == "__main__":
    main()