# An Armstrong number (also called a narcissistic number, pluperfect digital invariant (PPDI), or pluperfect number) 
# is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

def Armstrong_number(num):
    count=0
    temp_num,check = num,num
    while(num>0):     ### 123
        count+=1
        num=num//10
    
    print(count)
    arms = 0
    while(temp_num>0):
        rem = temp_num%10
        arms = arms + pow(rem,count)
        temp_num = temp_num//10
    
    print("Check",check)
    print("arms",arms)
    if check==arms:
        return "Armstrong number"
    
    else:
        return "Not Armstrong number"
    
num = int(input("Enter number: "))
print(Armstrong_number(num))