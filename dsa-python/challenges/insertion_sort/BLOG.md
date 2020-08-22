# Insertion Sort


An insertion sort takes an array and sorts it similar to the way you would sort cards in your hand. Consider the code below:

```py
def insertion_sort(arr: list) -> list:

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

```

## Now lets break this down

1. We take in an Array of integers-

```py
insertion_sort([8,4,23,42,16,15])

```

2. Now our for loop takes the length of the array and starts to iterate over it

```txt
for loop >
[8, 4, 23, 42, 16, 15]
 ^                  ^
 i                  j

while 6 >= 0 and 8 < 15]
 [8, 4, 23, 42, 16, 15]
  ^              ^
  i              j
```

3. This will remain true until we get to the 4. When we get to the 4 the array will change.

```txt
[4, 8, 23, 42, 16, 15]
    ^   ^   ^   ^   ^
    i < j < j < j < j

[4, 8, 23, 42, 16, 15]
```

4. This iteration of the while loop will not change cause the remaining numbers are not less than 8. But below we have another change cause 15 is lower than 23. Notice how j + 1 just moves 23 up to be the next i.

```txt
[4, 8, 23, 42, 16, 15]
        ^   ^   ^   ^
        i           j

[4, 8, 15, 23, 42, 16]
        ^   ^
        i   j+1

```

5. This goes on until i equals the last index in the list. The list should now an sorted array like below.

```txt
[4, 8, 15, 16, 23, 42]
```
