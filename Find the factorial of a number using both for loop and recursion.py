def fact(num):
    factorial=1
    for i in range(num+1):
        if i==0:
              i=1
              factorial=factorial*i
        else:
             factorial=factorial*i

    return factorial

number = int(input())
print(fact(number))