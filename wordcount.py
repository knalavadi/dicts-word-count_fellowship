# put your code here.
#open file
# initalize empty dictionary
#initalize counter 

# for each word in file 
#if that word exist in dictionary counter + one, 0 (use .get)
#else if that word doest exist add the word  plus counter = 1 


def word_counter(imported_file):
    """ print a dictionary of words in the file along with total count of each word """

    file_to_read = open(imported_file)

    word_dict = {}

    for line in file_to_read:
        words = line.split()

        for word in words:
            current_count = word_dict.get(word, 0)
            word_dict[word] = current_count + 1

    file_to_read.close()

    print word_dict

word_counter("test.txt")
                