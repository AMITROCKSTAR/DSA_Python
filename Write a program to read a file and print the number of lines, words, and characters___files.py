def file_char_word_line_count(file_name):
    try:
        with open(file_name, "r",encoding="utf-8") as file:
            text = file.read()


        # Count lines 
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        num_lines=len(lines)
        num_words= len(text.split())
        num_chars= len(text)

        print(f"num_lines : {num_lines}")
        print(f"num_words: {num_words}")
        print(f"num_char: {num_chars}")

    except FileNotFoundError:
        print("Error:file not found error")





file_name = "sample.txt"
file_char_word_line_count(file_name)