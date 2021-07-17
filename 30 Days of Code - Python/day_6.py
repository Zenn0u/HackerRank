# Title: Let's Review

# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

n = int(input().strip())
for i in range(0,n):
    word = str(input().strip())
    first = ""
    second = ""
    for i in range(0,len(word)):
        if i % 2 == 0:
            first += word[i]
        else:
            second += word[i]
    print(f"{first} {second}")