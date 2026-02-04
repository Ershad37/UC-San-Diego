def main():
    values = [40, 44, 49, 32]  
    weights = [5, 4, 7, 8]
    bag = 9
    print(maximizing_loot_fast(values, weights, bag))


def maximizing_loot_fast(values, weights, bag_capacity):
    paired_array = making_pairs(values, weights)
    sorted_paired_array = merge_sort(paired_array)
    amounts = [0] * len(values)
    total_value = 0

    for i in range(len(sorted_paired_array)):
        if bag_capacity == 0:
            return amounts, total_value
        
        a = min(sorted_paired_array[i][1], bag_capacity)
        total_value += sorted_paired_array[i][0]
        amounts[i] = a
        bag_capacity -= a

    return amounts, total_value
        


def making_pairs(arr1, arr2):
    paired_array = []
    for i in range(len(arr1)):
        paired_array.append((arr1[i], arr2[i]))

    return paired_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    return merge(sorted_left_half, sorted_right_half)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] // left[i][1] > right[j][0] // right[j][1]:
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