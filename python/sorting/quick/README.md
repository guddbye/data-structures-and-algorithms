# Blog Notes: Quick Sort
## Pseudocode

ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // Set a pivot value as a point of reference

    DEFINE pivot <-- arr[right]

    // Create a variable to track the largest index of numbers lower than the defined pivot

    DEFINE low <-- left - 1

    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // Place the value of the pivot location in the middle.
     // All numbers smaller than the pivot are on the left, larger on the right.

     Swap(arr, right, low + 1)
    // Return the pivot index point

     Return low + 1

ALGORITHM Swap(arr, i, low)

    DEFINE temp;

    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

Start with [8,4,23,42,16,15]

The pivot point is set to be 15 on the first pass, which is the final value in the list. After analyzing the list, it will move everything below the pivot to the left and everything above it to the right. Each value that is lower than the pivot is placed in the left side by swapping it with the first value of the list. The pivot is shifted to the position after the values that were lower than it if there are still values on the right.

## Time Complexity:
Time: O(n/log/n): the recursive function is logarithmic by the constant splitting of the list.
Space: O(1): The space requirement is constant because the list is sorted in place.
