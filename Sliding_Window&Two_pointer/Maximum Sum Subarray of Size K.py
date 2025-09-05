def max_sum_subarray_size_k(array_list,k):
    maxm=-1

    # for i,element in enumerate(array_list):  array_list=[1,2,3,4,5,6], n=6, k=4
    i=0
    j=k
    sum=0
    for initial in range(k):
        sum=sum+array_list[initial] ## final_sum =10  , creating window of size k
    # print(f"sum_window:{sum}")
    while j<len(array_list):
        maxm = max(sum,maxm) # maxm=10
        # print(f"maxm:{maxm}")
        sum= sum-array_list[i]+array_list[j] ## 10-1+5 = 14 
        # print(f"sum: {sum}")
        i=i+1
        # print(i)
        j=j+1
        # print(j)

    return max(maxm,sum)

print(f"maximum_subarray_of_size_k_sum: {max_sum_subarray_size_k([1,2,3,-1,3,4,-4,5,6,-5,0,2,-3],4)}")





