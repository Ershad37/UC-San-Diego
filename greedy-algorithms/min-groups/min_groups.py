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


def grouping_the_children(groups: list[int], arr: list[int]):
    for group in groups:
        return arr[group[0]: group[1]+ 1]
    




if __name__ == "__main__":
    main()