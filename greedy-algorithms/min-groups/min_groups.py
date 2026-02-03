def main():
    children = [2,2,3,4,4,5,6,6,6,7,8,9]
    print(min_num_of_groups(children))


def min_num_of_groups(ages: list[int]):
    groups = []
    i = 0
    while i < len(ages):
        l, r = ages[i], ages[i] + 2
        groups.append((l, r))
        while i < len(ages) and r >= ages[i]:
            i += 1

    return groups


if __name__ == "__main__":
    main()