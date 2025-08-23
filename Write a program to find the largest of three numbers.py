def largest():
    a=10
    b=13
    c=4

    # Python built-in max function

    print(max(a,b,c))

    ## Writing logic to print largest between 3 numbers
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)

    elif b>a:
        if b>c:
            print(b)
        else:
            print(c)

    else:
        print(c)
       
         
largest()