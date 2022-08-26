def maximum(list1):
    largestNumber = list1[0]
    for number in list1:
        if number > largestNumber:
            largestNumber = number
    return largestNumber


def howMany(s1, s2):
    ## Count the number of nonoverlapping occurrances of s2 in s1
    if s2 != "":
        n = 0 # number of nonoverlapping occurrances
        i=0
        while i < len(s1):
            if s1[i:].startswith(s2):
                n += 1
                i = i + len(s2)
            else:
                i += 1
        return n
    else:
        return len(s1) + 1




def main():
    ## Calculate a factorial.
    n = getN()
    print(str(n) + '!', "is", fact(n))

def getN():
    while True:
        n = eval(input("Enter a positive integer: "))
        if isinstance(n, int) and (n > 0):
            return n
        else:
            print("The number you entered is not a positve integer.")

def fact(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
main()

