f = open("newfile.txt", "a")             # opens and creates file called newfile.txt to write on it with "w" - if using "a" it means append not create new or re-write
f.write("\nHello World\n")                         # writes Hello on the file opened above - depending on where you use the \n the lines will brake accordingly
f.close()                                # closes the file but it is still stored in memory



#----------------------------------------------------------------------

words = ["the", "quick", "brown", "fox"]

words_as_string = "\n".join(words)      # this will append \n to the words in words list above it
f = open("newfile.txt", "w")
f.write(words_as_string)
f.close()