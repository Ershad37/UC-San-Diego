def main():
    print(max_dot_product(arr1=[2, 3, 9], arr2=[7, 4, 2]))


def max_dot_product(arr1, arr2):
    if len(arr1) == 1 and len(arr2) == 1:
        return arr1[0] * arr2[0]
    
    arr1_sorted = merge_sort(arr1)
    arr2_sorted = merge_sort(arr2)
    maximum_product = 0

    for i in range(len(arr1)):
        maximum_product += arr1_sorted[i] * arr2_sorted[i]

    return maximum_product


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    first_half = arr[:mid]
    second_half = arr[mid:]

    first_half_sorted = merge_sort(first_half)
    second_half_sorted = merge_sort(second_half)

    return merge(first_half_sorted, second_half_sorted)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    main()