def word_freq(text):
    sum_char =""
    dict_count={}
    for char in text:
        
        if(char==" " or char=="." or char==","):
            if sum_char in dict_count:
                dict_count[sum_char]=dict_count[sum_char]+1
                sum_char=""
                continue
            else:
                dict_count[sum_char]=1
                sum_char=""
                continue

        sum_char = sum_char+char 


    if sum_char in dict_count:
        dict_count[sum_char]=dict_count[sum_char]+1

    else:
        dict_count[sum_char]=1

    
    return dict_count
text = "Clever Fox Jump over the lazy Dog.Clever clever clever Fox Jump over the lazy Dog Summ, "
print(word_freq(text))

















