import test

f = int(open('INPUT.txt', 'r').read())
string = ''
sumAllNumbers = 0
if 0 < f <= 10**4:
    for x in range(1, f + 1):
        sumAllNumbers += x

if sumAllNumbers > 0:
    string = str(sumAllNumbers)

the_file = open('OUTPUT.txt', 'w')
the_file.write(string)
test.TEST.echo()