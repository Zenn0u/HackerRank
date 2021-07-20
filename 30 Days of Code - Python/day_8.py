n = int(input())

nns = [input().split() for _ in range(n)]
phoneBook = {name: num for name,num in nns}

while True:
    try:
        name = input()
        if name in phoneBook:
            print(f"{name}={phoneBook.get(name)}")
        else:
            print("Not found")
    except:
        break