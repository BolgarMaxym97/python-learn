f = open('INPUT.txt', 'r')
arr = [x.strip() for x in f.readlines()]
threeCount = 0
fourCount = 0
three = [item for item in arr[1].split() if int(item) % 2 != 0]
four = [item for item in arr[1].split() if int(item) % 2 == 0]

file = open('OUTPUT.txt', 'w')
file.write(' '.join(three) + '\n')
file.write(' '.join(four) + '\n')
file.write('YES' if len(four) > len(three) else 'NO')