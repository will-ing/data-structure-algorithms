# Merge Sort

> Merge sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

Consider the following sudo code:

```txt
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

First we have to find the left, middle and right of the arr.

```py
[8, 4, 23, 42, 16, 15]
 ^      ^           ^
 L     mid          R
```

Then we have to separate it in to two arrays

```py
# left
[8, 4, 23]

# right
[42, 16, 15]

```

Then we break them again and sort them.

```py
# left
[8, 4, 23]

[4, 8] + [23]

[4, 8, 23]


# right
[42, 16, 15]
[16, 42] + [15]

[15, 16, 42]
```

Now we bring the rest together.

```py

[4, 8, 23] + [15, 16, 42]

[4, 8, 15, 16, 23, 42]

```

The best way to do this is to use a helper function to merge everything back together. This sorting method has a time complexity of O(nlogn).

Merge Sort is useful for sorting linked lists in O(nLogn) time. It can also is good for the inversion count problem and external sorting.