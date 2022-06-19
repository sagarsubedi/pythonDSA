# given two non-empty arrays of ints, write a func that determines whether the second array is a subsequence of the first array.

# soln 1
# O(N) time | O(1) space
def isValidSubsequence(array, sequence):
    arrayIdx = 0
    sequenceIdx = 0
    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)


# soln 2
# O(N) time | O(1) space
def isValidSubsequenceForLoop(array, sequence):
    sequenceIdx = 0
    for value in array:
        if sequenceIdx == len(sequence):
            return True
        if sequence[sequenceIdx] == value:
            sequenceIdx += 1
    return sequenceIdx == len(sequence)
