## Identify president by number.
infile = open("USPres.txt", 'r')
for i in range(15):
    infile.readline()
print("The 16th president was")
print(infile.readline().rstrip() + '.')
infile.close()