def prime_number(num):
    
    for outer in range(num-1): # num = 50
        outer= outer+2
        count=0
        for inner in range(outer-1):  # num = 2
            if outer%(inner+2)==0:
                count+=1

        if count==1:
            print(outer)
            

prime_number(50)


                                                  
