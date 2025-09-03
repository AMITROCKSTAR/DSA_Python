# 1st approach : convert list into set then again into list
# 2nd approach list comprehension

def unique_element(duplicate_element_list):
    # unique_list=[]

    # [unique_list.append(i) for i in duplicate_element_list if i not in unique_list]
    u_l=set(duplicate_element_list)
    u_l=list(u_l)

    # return unique_list
    return u_l
unique_list = [1,2,3,2,5,3,7,2,4,5]
print(unique_element(unique_list))