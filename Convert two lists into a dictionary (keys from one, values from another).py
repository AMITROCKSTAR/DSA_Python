def list_to_dictionary(list1,list2):
    dictionary = {}
    
    for i,j in zip(list1,list2):
        dictionary[i]=j

    return dictionary

list1 = ["Name","Age","Gender"]
list2 = ["Amit",25,"Male"]

print(list_to_dictionary(list1,list2))



