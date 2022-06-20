# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import erf

mn, sd = map(float, input().split())
one = float(input())
lower, upper = map(int, input().split())

norm_one = 0.5 + 0.5 * erf((one-mn)/(sd* 2**0.5))
norm_upper = 0.5 + 0.5 * erf((upper-mn)/(sd* 2**0.5))
norm_lower = 0.5 + 0.5 * erf((lower-mn)/(sd* 2**0.5))

print( '{:.3f}'.format(norm_one))
print( '{:.3f}'.format(norm_upper - norm_lower))