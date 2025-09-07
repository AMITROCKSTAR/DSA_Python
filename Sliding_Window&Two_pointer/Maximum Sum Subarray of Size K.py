def max_sum_subarray_size_k(array_list,k):
    n=len(array_list)
    if n<k:
        return None
    
    maxm=-1

    # for i,element in enumerate(array_list):  array_list=[1,2,3,4,5,6], n=6, k=4
    i=0
    j=k
    # sum=0
    ##computing sum of first k elements

    summ=sum(array_list[:k])
    # for initial in range(k):
    #     sum=sum+array_list[initial] ## final_sum =10  , creating window of size k
    # print(f"sum_window:{sum}")
    while j<len(array_list):
        maxm = max(summ,maxm) # maxm=10
        # print(f"maxm:{maxm}")
        summ= summ-array_list[i]+array_list[j] ## 10-1+5 = 14 
        # print(f"sum: {sum}")
        i=i+1
        # print(i)
        j=j+1
        # print(j)

    return max(maxm,summ)

print(f"maximum_subarray_of_size_k_sum: {max_sum_subarray_size_k([2, 1, 5, 1, 3, 2],3)}")





## Approach 1: Brute Force (O(n*k))

# Loop through all subarrays of size k, compute sum, track max.

# 🔹 Approach 2: Sliding Window (O(n)) ✅

# Step 1: Calculate sum of first k elements.

# Step 2: Slide window → subtract element going out, add element coming in.

# Step 3: Track maximum sum.
# Complexity

# Time: O(n)

# Space: O(1)