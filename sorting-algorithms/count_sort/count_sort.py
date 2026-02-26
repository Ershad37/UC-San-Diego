def main():
    print(count_sort([2,3,1,3,4,2,2,5,6,2,1,2,3,4,3,2,1]))


def count_sort(arr):
    count = [0] * len(arr)
    result = []
    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(arr)):
        if i != 0:
            temp = [i] * count[i]
            result.extend(temp)
        
    return result


if __name__ == "__main__":
    main()