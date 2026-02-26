def main():
    print(selection_sort([8,1,2,3,23,87,34,62,19,27]))


def selection_sort(arr: list[int]):
    for i in range(len(arr)):
        min_num = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_num:
                min_num = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
                
    return arr


if __name__ == "__main__":
    main()