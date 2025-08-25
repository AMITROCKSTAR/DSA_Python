# 1st Approach : Store all elements in set because it keep unique values
# 2nd Approach : If order matters then use "dict.fromkeys()"



def remove_duplicates(liSt):
    # list_to_set=set()
    # for i in liSt:
    #     list_to_set.add(i)
    # list_to_set={i for i in liSt} ## Set comprehension ----->>>> 1st approach
    #unique_list = list(dict.fromkeys(liSt)) ## ------------->>>>> 2nd approach
    
    unique_list=[]

    [unique_list.append(i) for i in liSt if i not in unique_list] ## -------> 3rd approach
    # return list_to_set
    # return unique_list
    return unique_list
listt = [1,2,3,4,3,2,5]
print(remove_duplicates(listt))