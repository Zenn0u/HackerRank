# Enter your code here. Read input from STDIN. Print output to STDOUT


A, B = map(float, input().split())

# Solved by using the algorithm provided here https://www.hackerrank.com/challenges/s10-poisson-distribution-2/forum/comments/293964
cA = 160 + 40*(A + A**2)
cB = 128 + 40*(B + B**2)

print(round(cA, 3))
print(round(cB, 3))