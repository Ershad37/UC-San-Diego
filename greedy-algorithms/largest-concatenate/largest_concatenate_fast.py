def main():
    print(largest_concatenate(nums=[0, 4, 9, 8, 1, 6, 9, 0]))


def largest_concatenate(nums: list[int]):
    nums_sorted = merge_sort(nums)
    largest = ""
    for num in nums_sorted:
        largest += str(num)
    
    return largest


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    m = len(nums) // 2
    left_half = nums[:m]
    right_half = nums[m:]

    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)

    return merge(left_half_sorted, right_half_sorted)


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