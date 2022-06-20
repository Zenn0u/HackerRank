# Enter your code here. Read input from STDIN. Print output to STDOUT
# Couldn't solve it my own ways for some reason despite doing it pretty similarly
# solution taken from https://www.hackerrank.com/challenges/s10-normal-distribution-2/forum/comments/355249
# because I didnt want to bother

from math import erf

mn, sd = map(float, input().split())
pass_lim = float(input())
fail_lim = float(input())

cdf = lambda x: 0.5 * (1 + erf((x - mn) / (sd * (2 ** 0.5))))

print(round((1-cdf(pass_lim))*100,2))
print(round((1-cdf(fail_lim))*100,2))
print(round((cdf(fail_lim))*100,2))