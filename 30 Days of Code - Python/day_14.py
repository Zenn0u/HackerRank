class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        max = None
        for i in self.__elements:
            for j in self.__elements:
                abv = abs(i - j)
                if max == None:
                    max = abv
                elif max < abv:
                    max = abv
        self.maximumDifference = max
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)