def main():
    ## Calculate the amount of a pension.
    age = getAge()
    monthsOfService = getMonthsOfService()
    salary1 = getFirstSalary()
    salary2 = getSecondSalary()
    salary3 = getThirdSalary()
    pension = calculatePension(age, monthsOfService, salary1, salary2, salary3)
    displayPension(pension)

def getAge():
    age = eval(input("Enter your age: "))
    return age

def getMonthsOfService():
    monthsOfService = int(input("Enter number of months of service: "))
    return monthsOfService

def getFirstSalary():
    salary1 = eval(input("Enter first of three highest salaries: "))
    return salary1

def getSecondSalary():
    salary2 = eval(input("Enter second of three highest salaries: "))
    return salary2

def getThirdSalary():
    salary3 = eval(input("Enter third of three highest salaries: "))
    return salary3

def calculatePension(age, monthsOfService, salary1, salary2, salary3):
    ave = round((salary1 + salary2 + salary3) / 3, 2)
    yrs = monthsOfService / 12
    percentage = 36.25 + (2 * (yrs - 20))
    if percentage > 80:
        percentage = 80
    pension = ave * (percentage / 100)
    return pension

def displayPension(pension):
    print("Annual pension: ${0:,.2f}".format(pension))

main()