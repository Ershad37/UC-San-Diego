def main():
    print(largest_concatenate(nums=[0, 6, 8, 9, 2, 9, 1, 0]))


def largest_concatenate(nums):
    result = ""
    while len(nums) != 0:
        largest = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[largest]:
                largest = i
        result += str(nums[largest])
        nums.remove(nums[largest])
    
    return result
            


if __name__ == "__main__":
    main()