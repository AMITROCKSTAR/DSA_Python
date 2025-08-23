def palindrome(number):
    rev=0
    rem=0
    duplicate_number=number

    while(number>0):
        rem= number%10
        rev= rev*10+rem
        number = number//10

    if duplicate_number==rev:
        return "Palindrome"
    
    else:
        return "Non-Palindrome"
    

print(palindrome(2222))
