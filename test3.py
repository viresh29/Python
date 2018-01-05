

#print(eval('4+2*3'))

FILE = open('C:\\Users\\viresh.patel\\Documents\\Excel Docs\\global_superstore.csv','r').readlines()
#print(len(FILE))
header = open('C:\\Users\\viresh.patel\\Documents\\Excel Docs\\global_superstore.csv').readline()

records = 1
for i in range(len(FILE)):
    if i % 10000 == 0:
        newfile = open(str('C:\\Users\\viresh.patel\\Documents\\Excel Docs\\') + "global_superstore" + str(records) + ".csv", 'w+')
        if records > 1:
            newfile.write(header)
        newfile.writelines(FILE[i:i+10000])
        records += 1




