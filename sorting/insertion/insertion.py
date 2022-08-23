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
