def diff_arr(number):
    allDiffs = []
    diffNumber = 1
    while diffNumber <= number:
        if number % diffNumber == 0:
            allDiffs.append(diffNumber)
        diffNumber += 1
    return allDiffs


def min_diff(allDiffs):
    diffNumbersSum = {}
    for item in allDiffs:
        itemSumm = 0
        for strItem in str(item):
            itemSumm += int(strItem)
        diffNumbersSum[int(item)] = itemSumm

    maxWithoutCheck = max(diffNumbersSum.values())
    minValue = 10 ** 5
    for key, value in diffNumbersSum.items():
        if value == maxWithoutCheck and key < minValue:
            minValue = key
    return minValue
