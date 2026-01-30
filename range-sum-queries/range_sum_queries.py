def main():
    results = range_sum_queries([5, 10, 20], [(0, 1), (1, 3)])
    print("\n".join(map(str, results)))


def range_sum_queries(arr, queries):
    result = []
    for query in queries:
        sum_nums = 0
        for i in range(query[0], query[1]):
            sum_nums += arr[i]
        result.append(sum_nums)
        sum_nums = 0
    
    return result


if __name__ == "__main__":
    main()