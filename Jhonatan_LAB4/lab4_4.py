# README
# This portion of the lab uses functions, lists with 
# the method append(), slicing, built-in functions
# such as: input(), len() and str(), string methods such as:
# isspace(), strip() and index(), while loops, and if-else statements

# LOGIC
# 1. Imagine you have a string ' hello world '
# 2. Use the strip method to remove the leading and trailing whitespace
# 3. Now the string is 'hello world'
# 4. Remove and save the first word somewhere [hello]
# 5. Now the string is ' world'
# 6. Go back to step 1 with the new string and repeat until string is ''

# CHALLENGE
# I believe this code is 100% functional, if you don't think so,
# try to input any sentence with any amount of spaces and any amount
# of words with any lenght. Were you able to break it?

# IMPORTANT
# 1. This code does not differentiate between numbers and letters,
# so, for example, there will be 4 words in 'My id is 123'. 
# 2. If you type a symbol alone such as 'hello . world', it will count
# as a word, so the total of words would be 3, although '.' is a symbol.

sntc = input("Enter a sentence: ") #sntc = sentence

# functions are defined with the key word def and allows to reuse code
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

        # happens if there are yet spaces in the string
        else:
            new_word = string[:string.index(' ')] # defines always the first word in string
            words_found.append(new_word) # appends the new word

            string = string[string.index(' '):] # string is redefined excluding the word found

            # Example:
            # string before = 'hello world'
            # string after = ' world'

            # since string after is not empty it keeps 
            # looping over itself until it gets the last word
    
    return words_found # returns all the words found in the string as a list

# displays the len of words_found
print(f'Number of words: {len(get_words(sntc))}')

