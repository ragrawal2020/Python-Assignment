arr=[1,2,3,4,5]
a=int(input("Enter a number"))
for x in range(len(arr)):
    if(a == arr[x]):
        print("Your number is found in the array")
else:
    print("Your number is not found")


