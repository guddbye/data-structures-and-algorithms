# Perform a quick method on a list of numbers
def quick_sort(nums, left, right):
    if left < right:
        pivot = partition(nums, left, right)
        quick_sort(nums, left, pivot - 1)
        quick_sort(nums, pivot + 1, right)
        return nums

# define a partition method
def partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left

# define a swap method
def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    nums = [2, 5, 1, 7, 3, 9, 4, 6, 8]
    print(quick_sort(nums, 0, len(nums) - 1))
