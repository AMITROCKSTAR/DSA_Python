# def vowels(vowel):
#     count=0
#     for char in vowel:
#         if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
#             count+=1
    
#     return count

def vowels(vowel):
    count=0
    vow="aeiouAEIOU"

    for char in vowel:
        if char in vow:
            count+=1
    
    return count
print(vowels("abcdefghijklmnopqrstuvwxyz"))