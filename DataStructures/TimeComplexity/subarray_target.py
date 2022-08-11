
# sliding window technique

nums = [1, 2, 3, 4, 5]
target = 9


def sub_array_sum(array, target):
    left = 0
    right = 1
    total = array[left] + array[right]

    while right < len(nums):
        if total == target:
            return True

        elif total < target:
            right += 1
            if right < len(array):
                total += array[right]

        elif total > target:
            total -= array[left]
            left += 1

    return False
            

print(sub_array_sum(nums, target))





