import math
x = int(input())
arr=[]
odd=[]
for i in range(x+1,1,-1):
    if x % i == 0:
        if i % 2 == 0:
            arr.append(i)
        else:
            odd.append(i)
if (x<10):
    print("Invalid number")
elif len(arr)+len(odd)==1:
    print("Please input a different number")
else:
    print(arr)
    print("Product: "+ str(math.prod(arr)))
    print("Sum: "+ str(sum(arr)))