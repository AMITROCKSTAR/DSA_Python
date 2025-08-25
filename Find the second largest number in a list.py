def second_largest(liSt):
    # a,b=0,0

    ## Using Use sorted(set(numbers))[-2] if you want a short and simple solution:
    print("2nd largest:", sorted(set(liSt))[-2])   # 45

    # for i in liSt:
    #     if b<i and b>a or b==a:
    #         a=b  ## a=0,2,4,6
    #         b=i  ## b=2,4,6,9

    #     elif b>i and a<i or a==i:
    #         a=i  ## a=1 
         
    #     elif b>i and a>i or a==i:
    #         continue

    # return a
    
    


liSt=[2,1,4,2,6,9,2,5,2,3,4,5,6,7,2,46,2,5,7,2,5,8,9,4,6,9,9,9,9,45]
print(second_largest(liSt))