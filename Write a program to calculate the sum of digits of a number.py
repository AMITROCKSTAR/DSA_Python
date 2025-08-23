def sum(number):

    if number==1:
        return 1
    
    return number+sum(number-1)

number = int(input())
print(sum(number))