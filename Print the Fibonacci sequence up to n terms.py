def fibonacci(num):
    # num=5
    a=0
    b=1
    c=0
   
    for i in range(num):
        c=a+b
        print(a," ")
        a=b
        b=c
    
number = int(input())
fibonacci(number)