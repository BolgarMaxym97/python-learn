from helper import diff_arr, min_diff

f = int(open('input.txt', 'r').read())
allDiffs = diff_arr(f)
minValue = min_diff(allDiffs)

w = open('output.txt', 'w').write(str(minValue))
