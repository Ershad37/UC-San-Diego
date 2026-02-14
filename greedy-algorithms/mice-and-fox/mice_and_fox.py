def main():
    mice = [1, 2, 3, 4, 5]
    holes = [50, 40, 30, 20, 10]
    result = mice_fox(mice, holes)
    print(" ".join(map(str, result[1])))
    print(result[0])


def mice_fox(mice, holes):
    mice_sorted = merge_sort(mice)
    holes_sorted = merge_sort(holes)

    distances = []
    longest_dis = 0
    for m, h in zip(mice_sorted, holes_sorted):
        distance = abs(m - h)
        distances.append(distance)
        if distance > longest_dis:
            longest_dis = distance

    return longest_dis, distances




def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)

    return merge(left_half_sorted, right_half_sorted)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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