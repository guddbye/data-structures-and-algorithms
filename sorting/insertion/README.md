# Blog Notes: Insertion Sort

# Insertion Sort

Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration. Insertion sort works similarly as we sort cards in our hand in a card game. We assume that the first card is already sorted then, we select an unsorted card.

Space Complexity: O(1)

![psuedo](sorting/insertion/SHOT.png)


```

# Implementation of Insertion Sort
####### WALKS THROUGH STEP BY STEP OF THE INSERTION SORT METHOD #######

# Uses insertion sort to sort a list of integers.
def insertionSort(arr): # Insertion sort function.

    for i in range(1, len(arr)):  # Loop through the array.

        key = arr[i]  # The key to be inserted.

        j = i - 1 # j is the index of the first element in the sorted portion of the array.

        while j >= 0 and key < arr[j]:

            arr[j + 1] = arr[j] # shift elements to the right

            j -= 1  # decrement j

        arr[j + 1] = key # Insert the key at the correct position.

    return arr  # Return the sorted array.

def main(): # Main function.

    arr = [12, 11, 13, 5, 6]  # Create an unsorted array.

    print(insertionSort(arr)) # Print the sorted array.

```
