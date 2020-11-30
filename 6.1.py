#6.1 Dictionary

Georgia = {
    'name' : 'georgia',
    'city' : 'leeds',
    'food' : 'pasta'
    }
print(Georgia['name'])
print(Georgia['city'])

favourite_numbers = {
    'charlotte' : 8,
    'georgia' : 24,
    'richard' : 10,
    'taylor' : 13,
    'lucy' : 2
    }

print ("Charlotte's favourite number is " +
       str(favourite_numbers['charlotte']))
print(favourite_numbers['georgia'])
print(favourite_numbers['richard'])
print(favourite_numbers['taylor'])
print(favourite_numbers['lucy'])

glossary = {
    'integer' : 'An integer is a number',
    'float' : 'A float is a number with decimol point',
    'string' : 'A string is text used with double quotation marks or single'
    }
print("What is an integer?\n " + glossary ['integer'])

for name, city in Georgia.items():
    print(name.title() + "'s favourite city is " + city.title() + ".")
