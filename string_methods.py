country = 'Bangladesh'

print(len(country))
print(country.upper())
print(country.lower())

# method vs function : methods are associate with object, but functions are not
# len functions but upper method

print('Ban' in country) # True since 'Ban' exists in country

eng_country = country.replace('Bangla', 'English')

print(eng_country) # Englishdesh
