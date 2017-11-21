def mergesort(numbers):
    if not numbers or len(numbers) == 1:
        return numbers
    else:
        mid = len(numbers)//2
        left = mergesort(numbers[:mid])
        right = mergesort(numbers[mid:])
        return merge(left, right)


def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged += [left.pop(0)]
        else:
            merged += [right.pop(0)]
    merged += left
    merged += right
    return merged

L = [9,2,5,4,7,3,6,8]
print(mergesort(L))
