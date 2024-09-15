#A print("Python").Upper()
#Errors: .Upper() is not a method of the function print(), first character must be lowercase
print("Python".upper())

#B Print('Say it ain't so.')
#Errors: Quote mark in the word "ain't" is closing the string of the function 
#and it is not concatenating the rest of it
print('Say it ain\'t so')

#C print('*'*5 +Hotel+'*'*5)
#Erros: Unless "Hotel" is a variable containing a string, it must be set as string in order to 
#be concatenated with the other strings
print('*'*5+'Hotel'+'*'*5)

#D txt = "ET" 
#  class = 574
#  print(txt+class)
#Errors: Forgot to add quotation mark to 574, int or float values cannot be concatenated with strings
txt = "ET" 
class_0 = "574"
print(txt+class_0)

#E n = 1234
#  print(n.find('2'))
#Errors: .find() is a string method, therefore, variable n must contain a string, not an int or
#float value
n = '1234'
print(n.find('2'))

#F num = 101
#  print(num[0])
#Errors: The brackets in this context are used to access an element by their index, they don't
#work with int and float values but strings and lists
num = '101'
print(num[0])

