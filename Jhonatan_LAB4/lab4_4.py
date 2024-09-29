# README
# lab4_4.py Updated
#
# Program's function: To take a sentece and return the 
# number of words in it.
#  
# Description: This version of the code uses recursion,
# a concept that allows a function to use itself. Thanks 
# to that, I was able to symplify the task even further
# without the need of a while loop. Below the code is an
# explanation of how the logic works.
# 
# Keywords:
# sntc = sentence, strn = string, f_sp_i = first space index

sntc = input("Enter a sentence: ")

def get_words(strn):
    strn = strn.strip()
    
    if not ' ' in strn: return [strn]
    else:
         f_sp_i = strn.index(' ')
         new_strn = strn[f_sp_i:]
         return [strn[:f_sp_i]] + get_words(new_strn)

print(f'Number of words: {len(get_words(sntc))}')

# LOGIC

# 1. get_words('hello world again')
# strn = 'hello world again'
# return ['hello'] + get_words(' world again')

# 2. get_words(' world again')
# strn = 'world again'
# return ['world'] + get_words(' again') 

# 3. get_words(' again')                   
# strn = 'again'                           
# return ['again'] 
#
# Simplify values 
#   
# get_words(' again') = ['again'] then 
# get_words(' world again') = ['world'] + ['again] then
# get_words('hello world again') = ['hello'] + ['world'] + ['again']


# IMPORTANT
# There might be a case where an user inputs no words, since
# the code assumes that there is at least one character in
# the sentence it will return 1 although there are not words.
# To fix that, copy and paste the following line of code at the
# beggining of the function get_words: 

# if strn.isspace(): return []
