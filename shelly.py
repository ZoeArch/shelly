import re

user_input = input("Enter a string: ")
print("Input string:", user_input)

# compile a regular expression pattern into a regular expression object
p = re.compile("AP") # possibly replace ap with a variable? give the funtction an array and then automatically have the function run through it 

# use the match method to check if the pattern is at the start of the string
m = p.match(user_input)

# check if a match was found
if m:
    print("AP found at the start of the string.")
else:
    print("AP not found at the start of the string.")

def cleave(s, num_chars):
    return s[num_chars:]

def check(string, list):
    i = 0
    while (i > len(list)): 
        p = re.compile(list[i])
        i +=1
        p.match(string)
