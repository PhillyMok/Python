months = []

def main():
    ## display months containing the letter r.
    global months
    fillList()
    months = deleteNoRs()
    displayMonths()

def fillList():
    global months
    infile = open("Months.txt", 'r')
    months = [line.rstrip() for line in infile]
    infile.close

def deleteNoRs():
    reducedList = []
    for i in range(12):
        if 'r' in months[i].lower():
            reducedList.append(months[i])
    return reducedList

def displayMonths():
    print("The R months are:")
    print((", ").join(months))

main()