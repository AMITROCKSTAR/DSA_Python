def duplicate(List,k):
    window = set()

    for i,idx in enumerate(List):

        if idx in window:
            return True
        
        window.add(idx)

        if len(window)>k:
            window.remove(List[i-k])
    return False

List = [1,2,3,4,2]
k=3
print(duplicate(List,k))