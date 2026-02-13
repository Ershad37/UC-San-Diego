def main():
    segments = [[1,3], [2,5], [3,6]]
    result = collecting_signatures(segments)
    coordinates = str(result[1])
    print(result[0])
    print(result[1])
    


def collecting_signatures(segments):
    segments_sorted = merge_sort(segments)
    matches = 0
    coordinates = []
    n = len(segments_sorted)
    i = 0
    
    while i < n:
        point = segments_sorted[i][1]
        matches += 1
        coordinates.append(point)
        i += 1
        while i < n and segments_sorted[i][0] <= point:
            i += 1

    return matches, " ".join(map(str, coordinates))


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
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
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