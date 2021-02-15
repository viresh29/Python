

# bug collector
"""
bugs = int(input("Enter # of bugs collected each day: "))

count = 0
for i in range(5):
    count = count + bugs
print("Total bugs collected = ",count)

"""

# calories burned
"""
cal = 4.2

calburn = 0
for i in range(10,31,5):
    calburn = i * cal
    print("Calburn in ", i, " mins is ",calburn)
"""

# budget analysis
"""
monthlybudget = float(input("Enter Monthly Budget: "))

keepgoing = 'y'

sum = 0.0

while keepgoing == 'y' or keepgoing == 'Y':
    #get the expense from user
    expense = float(input("Enter Expense: "))

    sum = sum + expense

    keepgoing = input("Do you have more expense? (Enter y for yes) ")

if sum > monthlybudget:
    print("over budget")
else:
    print("under budget")


"""

# distance traveled

# distance = speed x time

"""
speed = int(input("What is the speed of the vehicle in mph? "))
traveltime = int(input("How many hours has it traveled? "))

print("Hours\tDistance Traveled")
print("------------------------")

for i in range(0,traveltime):

    print(i+1,"\t",speed*(i+1))

"""

# average rainfall
"""
yr = int(input("Enter Years: "))



total = 0.0

for i in range(yr):
    for j in range(12):
        rainfall = float(input("Enter Rainfall in inches for  month: "))

        total = total + rainfall
        avg = total / 12
    print("Months\tTotal Rainfall\tAvg Rainfall")
    print("------------------------------------")
    print(j + 1,"\t",total,"\t",avg)

"""

# celsius to fahrenheit table

# F = 9/5C + 32

"""
print("Celsius\tFahrenheit")
print("-------------------")

for c in range(21):
    f = (9/5) * c + 32
    print(c,"\t",f)
"""

# pennies for pay
"""
d = int(input("Enter day: "))

print("day\tpenny")
print("----------")

total = 0

for i in range(d):
    penny = 1
    penny = penny * i + 1 * 2

    total = total + penny

    print(i+1,"\t$",penny)
print("Total= $",total)

"""


# sum of numbers

# ocean levels

"""
lvl = 1.6
current = 0
for i in range(25):
    current = current + lvl
    print(i+1,"\t",current)

"""

# tution increase

"""

feepersemester = 8000
#increase = 0.03

for i in range(5):
    increase = 0.03
    for j in range(2):
        feepersemester = feepersemester * (j + 1)
    increase = feepersemester * increase
    print("Year",i+1,feepersemester + increase)

"""


# calculte factorial of a number

# population

# pattern

"""
for r in range(7):
    for c in range(8 - r - 1):
        print('*',end='')
    print()
"""

"""
for r in range(6):
    print("#",end='')
    for c in range(r):
        print(" ",end='')
    print("#")

"""


# functions
"""
def main():
    print("I have a message for you.")
    message()
    print("Goodbye!")


def message():
    print("I am Arthur,")
    print("King of the Britons.")

#call the function
main()

"""
