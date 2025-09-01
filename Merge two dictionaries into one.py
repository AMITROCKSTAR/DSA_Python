def merge_dict(dict1,dict2):
    # merge both dictionary
    for key,value in dict2.items():
        dict1[key]=value

    return dict1

dict1 = {"name":"amit","class":"12"}
dict2 = {"class":"12"}

print(merge_dict(dict1,dict2))