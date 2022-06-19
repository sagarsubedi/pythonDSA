# given sorted non empty array of integers, return a sorted array of the square of each element

# soln 1
def sortedSquaredArray(array):
    left = 0
    right = len(array) - 1
    result = [0 for _ in array]

    for indexToInsert in reversed(range(len(array))):
        absValueLeft = abs(array[left])
        absValueRight = abs(array[right])

        if absValueRight > absValueLeft:
            result[indexToInsert] = pow(absValueRight, 2)
            right -= 1
        else:
            result[indexToInsert] = pow(absValueLeft, 2)
            left += 1

    return result
# O(N) time | O(N) space

# another simple solution can be to just square all the numbers and then sort using python's sort()
