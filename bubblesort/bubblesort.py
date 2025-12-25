"""
So basically we start from the left and compare elements.
The heavy ones we push them to the right.
Once we pushed the heaviest to the far right
We start again from beginning.

Uncomment the print statements to see the movement.

https://www.youtube.com/watch?v=xli_FI7CuzA
"""


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # print(i)
        # After each pass, the last i elements are already sorted
        for j in range(0, n - i - 1):
            # print(j)
            if arr[j] > arr[j + 1]:
                # print(arr[j])
                # print(arr[j + 1])
                # print(numbers)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # print(numbers)

    return arr


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)
