#list_number = [1,2,3,4,5]

# Enter value in the list 
list_number = list(map(int,input("Enter value in the list").split()))
sum=0
avg=0

for i in range(len(list_number)):
    sum=sum+list_number[i]

## Average2
avg = sum//len(list_number)
print("Sum of the numbers in list: ", sum)

print("Average of the numbers in the list: ", avg)