## Determine 34th president.
infile = open("USPres.txt", 'r')
num = 0
for pres in infile:
    num += 1
    if num == 34:
        print("The 34th president was")
        print(pres.strip() + '.')
        break
infile.close()