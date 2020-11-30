#6.5 River

rivers = {
    'nile' : 'egypt',
    'themes' : 'england',
    'Mississippi' : 'usa',
    }

for name, country in rivers.items():
    print("The " + name.title() + " is in the country.." + country.title() + "!")


for name in rivers.keys():
    print("This river is called..." + name.title() + "!")
