#to read a file's data
# ONE WAY -----------------------------------------
f = open("data.txt", "r")                # opens file
lines = f.readlines()                    # stores the file info in lines variable therefore in memory
f.close()                                # closes the file but it is still stored in memory
print(lines)



# OTHER WAY ---------------------------------------
f = open("data.txt", "r")                #opens file
lines = f.read().split("\n")             #stores file in varible but as it has .split it gives each line a list without the .split it would all be one string together
f.close()                                #closes file but it is still stored in memory
print(lines)


# find most common word in a text file-------------
import re                                 # imports regular expresions from a python library which is native to python - another library would be "random"  
import collections

text = open("1155-0.txt").read().lower()  # opens the file in question .read() reads it and .lower() makes it all lower case and converts it into a string in a variable called text
words = re.findall("\w+", text)           # this line converts the string into a line - "\w+", text = finds all the words in text

long_words = []
for word in words:                        # this loop takes the words that are bigger than 5 characters
    if len(word) > 5:
        long_words.append(word)

most_common = collections.Counter(long_words).most_common(10)   # this prints out the top 10 words from the list created by the loop above

print(most_common)