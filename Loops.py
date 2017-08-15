
#While  --> Repeate until the loop condition is true
#For --> specify the iteration

#While loop
"""
num = int(input('Enter the value of n= '))
if (num <=0):
    print("Enter a valid value")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
print(sum)
"""

#For loop


for quant in range(99,0,-1):
    if(quant>1):
        print(quant,"Bottles of beer on the wall,",quant," bottles of beer")
        if(quant>2):
            suffix= str(quant)+" bottles of beer on wall"
        else:
            suffix = '1 bottle of beer on the wall'
    elif(quant == 1):
        print("1 bottle of beer on the wall, 1 bottle of beer")
        suffix=" No more beer on the wall"

    print("Take one down and pass it around", suffix)
    print("---")


for x in range(20):
    if(x%2==0):
        continue
    print(x)