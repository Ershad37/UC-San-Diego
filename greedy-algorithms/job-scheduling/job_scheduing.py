def main():
    jobs = [
        ("A",35,3),
    ]
    print(job_scheduling(jobs))


def job_scheduling(jobs):
    jobs_sorted = merge_sort(jobs)
    maximum_profits = 0
    #jobs_done = []

    profit = 0
    deadline = 0
    i = 0
    while i < len(jobs_sorted):
        profit = jobs_sorted[i][1]
        deadline = jobs_sorted[i][2]
        i += 1
        while i < len(jobs_sorted) and jobs_sorted[i][2] == deadline:
            if jobs_sorted[i][1] > profit:
                profit = jobs_sorted[i][1]
            i += 1
        maximum_profits += profit

    return maximum_profits


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
        if left[i][2] < right[j][2]:
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