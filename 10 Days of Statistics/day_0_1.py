# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mode
from statistics import median
from statistics import mean

n = int(input())
arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])
    
arr.sort()

#mean
print(mean(arr))

#median
print(median(arr))

#mode
print(mode(arr))