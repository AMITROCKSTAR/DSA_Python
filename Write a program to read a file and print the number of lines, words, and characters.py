def no_of_line_char_words(text):
    
   # count of characters
   char_count= len(text)

   # count of words
   word_count = len(text.split())

   # count of lines
   line_count = text.count("\n") +1  if text else 0

   print(f"Lines: {line_count}")
   print(f"word_count: {word_count}")
   print(f"char_count: {char_count}")



text = """
Scrum is an agile framework for managing complex projects that emphasizes teamwork, adaptability,
and delivering value in short cycles. Work is organized into sprints (2–4 weeks), each producing a usable product increment. It involves three main roles: the Product Owner (manages the product backlog and priorities), the Scrum Master (facilitates the process and removes obstacles), and the Development Team (builds the product). Scrum uses key artifacts like the product backlog, sprint backlog, and increment, along with events such as sprint planning, daily standups, sprint reviews, and retrospectives to ensure continuous progress and improvement. In essence, Scrum helps teams collaborate effectively, adapt to change, and deliver high-quality results iteratively.

"""
no_of_line_char_words(text)