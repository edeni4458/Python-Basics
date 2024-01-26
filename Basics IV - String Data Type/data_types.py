import math

# String Data Type

# Literal Assignment of Value
print("Topic")
print("--------------------------------")
print("String Data Type")
print("================================")
print('Literal Assignment of Value')
print("--------------------------------")

first = "Emmanuel"
last = "Denis"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

print('')

# Constructer Function
print("================================")
print('Constructer Function')
print("--------------------------------")


pizza = str('Pepporoni')
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

print('')


# Concatenation
print("================================")
print('Concatenation')
print("--------------------------------")

full_name = first + ' ' + last
print(full_name)

full_name += "!"
print(full_name)

print('')


# Casting a Number to a String
print("================================")
print('Casting a Number to a String')
print("--------------------------------")

decade = str(1980)
print(type(decade))
print(decade)

sentence = "I enjoy music from the " + decade + "s." 
print(sentence)

print('')


# Multiple Lines
print("================================")
print('Multiple Lines')
print("--------------------------------")

mutiline =  '''
The day of the Lord draws near.                     

I look forward to it.

                        And everyone who eagerly waits for Him, purifies themselves.


'''
print(mutiline)

print('')

# Escaping Special Characters 
print("================================")
print('Escaping Special Characters')
print("--------------------------------")

statment = 'I\'m back working for JJ!\tWhat, no way!\n\nWhat\'s the reason for\\ it?' 
print(statment)

print('')


# String Methods
print("================================")
print('String Methods')
print("--------------------------------")

print(full_name)
print(full_name.lower())
print(full_name.upper())

print(mutiline.title())
print(mutiline.replace("Him", "HIM"))
print(mutiline)

print(len(mutiline))
mutiline += '                                '
print(len(mutiline))
mutiline = "                               " + mutiline
print(len(mutiline))

print(len(mutiline.strip()))
print(len(mutiline.lstrip()))
print(len(mutiline.rstrip()))

print('')

# Build a Menu
print("================================")
print('Build a Menu')
print("--------------------------------")

title = "menu".upper()
print(title.center(20, '='))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("=================================")

print('')

# String Index Values
print("================================")
print('String Index Values')
print("--------------------------------")

print(first[3])
print(first[-1])
print(first[1:-1])
print(first[1:])
print(first[0:])

print('')

# Some methods return boolean values
print("================================")
print('Some methods return boolean values'.title())
print("--------------------------------")

print(first.startswith("J"))
print(first.endswith("l"))

print('')
# Boolean Data Type
print("================================")
print('Boolean Data Type')
print("--------------------------------")

my_value = True
x = bool(False)
print(type(x))
print(isinstance(my_value, bool))

print('')

# Numeric Data Types
print("================================")
print('Numeric Data Types')
print("--------------------------------")
print('Integer Types')
print("--------------------------------")

print(' ')
# Integer Types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

print(' ')

print('Float Types')
print("--------------------------------")
# Float Types
gpa  = 3.28
y = float(1.14)
print(type(gpa))

print(' ')

print('Complex Types')
print("--------------------------------")

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print(' ')

# Built-in Functions For Numbers
print("================================")
print('Built-in Functions For Numbers')
print("--------------------------------")

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

# Math Imported Operators
print('Math Imported Operators')
print("--------------------------------")

print('')

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

print('')

# Casting a Srting to a Number
print("================================")
print('Casting a Srting to a Number'.title())
print("--------------------------------")

zip_code = "54321"
zip_value = int(zip_code)
print(type(zip_value))

print("")

# Error if  you attempt to cast incorrect data
# zip_value = int("Arkansas")