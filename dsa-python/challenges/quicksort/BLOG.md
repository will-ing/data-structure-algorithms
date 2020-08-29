# Quick Sort

Quick sort is employed in many programming languages as the sorting algorithm under the hood. Quick sort is very fast that is particularly efficient for average scenarios. In worst case scenarios it performs like Insertion Sort and Selection Sort. It relies on the concept of partitioning.

Consider the following pseudo code:

```txt
LOGARITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

```

We assign a pivot and a pointers on the array. The pointers should be on the left most side of the array and the right most side. *excluding the pivot*

```py
[0, 5, 2, 1, 6, 3]
#^           ^  ^
#LP         RP pvt
```

1. The `left` pointer moves continuously to the `right` until it reaches a value that is `greater` than or equal to the pivot
2. The `right` pointer moves continuously to the `left` until it reaches a value that is `less` than or equal to the pivot

```py
[0, 5, 2, 1, 6, 3]
#^           ^  ^
#LP-->   <--RP pvt
```

When the left pointer stops , we start the right pointer until is reaches the value less than the pivot. When both have stopped we swap them.

```py
[0, 5, 2, 1, 6, 3]
#^           ^  ^
#LP-->   <--RP pvt

[0, 1, 2, 5, 6, 3]
#   ^     ^     ^
#  LP swap RP   pvt

[0, 1, 2, 5, 6, 3]
#      ^  ^     ^
#      LP RP    pvt

[0, 1, 2, 3, 6, 5]
#         ^     ^
#       LP swap pvt

```

Now that the pivot is in the right place, we partition everything to the left and right of the pivot. Using recursion.

```py
# left
[0, 1, 2]
# ^  ^  ^
# RP LP pvt

# left
   [0, 1]
#   ^  ^
# RP LP pvt

# left side is sorted
  [0, 1, 2, 3]

# Right of pivot
    [6, 5]
#    ^  ^
# RP LP pvt

# Right of pivot
    [5, 6]
#    ^  ^
# RP LP pvt (swap values)
```

Now we have the a sorted array!

```py
[0, 1, 2, 3, 5, 6]
```
