# Enter your code here. Read input from STDIN. Print output to STDOUT


d1, m1, y1 = [int(x) for x in input().split(' ')]
d2, m2, y2 = [int(x) for x in input().split(' ')]

if y1 > y2:
    print(10000)
elif y1 < y2:
    print(0)
else:
    if m1 > m2:
        print(500 * (m1 - m2))
    elif m1 < m2:
        print(0)
    else:
        if d1 > d2:
            print(15 * (d1 - d2))
        else:
            print(0)