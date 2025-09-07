## Using set

def Contains_duplicate(List,k):

    unique= set()
    for value in range(k):
        unique.add(List[value])

    if len(unique) != k:
        return True
    
    else:
        for i in range(0,len(List)):
            unique.remove(List[i])
            if i+k < len(List):
               if List[i+k] in unique:
                  return True
               else:
                  unique.add(List[i+k])
                              
            
        return False
    

List = [10, 20, 30, 40, 50, 60]
k=2
print(Contains_duplicate(List,k))