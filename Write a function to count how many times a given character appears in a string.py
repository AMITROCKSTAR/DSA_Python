def count_char(text,character):
    count=0
    for char in text:
        if character == char:
            count+=1

    return count

character = input("Enter character: ")
text = "A clever fox jumps over the lazy dog"
print(count_char(text,character))


