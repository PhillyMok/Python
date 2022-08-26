def main():
    ## Compare salary options
    opt1 = option1()
    opt2 = option2()
    print("Option 1 = ${0:,.2f}.".format(opt1))
    print("Option 2 = ${0:,.2f}.".format(opt2))
    if opt1 > opt2:
        print("Option 1 pays better.")
    elif opt1 == opt2:
        print("Options pay the same.")
    else:
        print("Option 2 is better.")

def option1():
    ## Compute the total salary for 10 days,
    ## with a flat salary of $100/day.
    sum = 0
    for i in range(10):
        sum += 100
    return sum

def option2():
    ## Compute the total salary for 10 days,
    ## starting at $1 and doubling each day.
    sum = 0
    daySalary = 1
    for i in range(10):
        sum += daySalary
        daySalary *= 2
    return sum
main()