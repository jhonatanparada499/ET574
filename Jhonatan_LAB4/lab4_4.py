# logic
# Only words for words longer than 2

sntc = input("Enter a sentence: ") #sntc = sentence

def get_words(par):
    string = str(par) # forces the parameter to be a string (extra security)
    words_found = [] # will catch all the words it finds in the string
    new_word = '' # will define each word in the string

    # string lenght must not be 0 & must not be only spaces.
    # will loop over string until it is empty
    while len(string) and string.isspace() == False:
        
        string = string.strip() # removes unnecessary spaces  

        # there will be a point where the string will be only one word
        if not ' ' in string:
            words_found.append(string) # the only word in the string is appended to words_found
            
            string = '' # since the string is empty the loop stops at this point

        else: # happens if there are yet spaces in the string
            new_word = string[:string.index(' ')] # defines always the first word in string
            words_found.append(new_word) # appends the new word

            string = string[string.index(' '):] # string is redefined excluding the word found

            # Example:
            # string before = 'hello world'
            # string after = ' world'

            # since string after is not empty it keeps 
            # looping over itself until it gets the last word
    
    return words_found # returns all the words found in the string as a list

print(f'Number of words: {get_words(sntc)}')

