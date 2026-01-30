def main():
    print(min_waiting_time_fast(t=[2, 10, 40, 3, 7, 16, 17], n=7))


def min_waiting_time_fast(t: list[int], n):
    t_sorted = merge_sort(t)
    waiting_time = 0

    for i in range(n):
        waiting_time += (n - i - 1) * t_sorted[i]
    
    return waiting_time


def merge_sort(arr: list[int]):
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
        if left[i] <= right[j]:
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