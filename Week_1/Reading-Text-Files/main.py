# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file:
        content = file.read()
        #print(content)

    return content
read_file_content("story.txt")


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    d = dict()
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    # Print the contents of dictionary
    for key in (d.keys()):
        print(key, ":", d[key])

    #return {"as": 10, "would": 20}
count_words()