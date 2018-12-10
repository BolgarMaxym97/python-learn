def diffArr(number):
    allDiffs = []
    diffNumber = 1
    while diffNumber <= number:
        if number % diffNumber == 0:
            allDiffs.append(diffNumber)
        diffNumber += 1
    return allDiffs

f = int(open('input.txt', 'r').read())
allDiffs = diffArr(f)
diffNumbersSum = {}
for item in allDiffs:
    itemSumm = 0
    for strItem in str(item):
        itemSumm += int(strItem)
    diffNumbersSum[int(item)] = itemSumm

maxWithoutCheck = max(diffNumbersSum.values())
minValue = 10**5
for key, value in diffNumbersSum.items():
    if value == maxWithoutCheck and key < minValue:
        minValue = key

w = open('output.txt', 'w').write(str(minValue))
