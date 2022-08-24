country = "bangla"

country_iter = iter(country)

print(type(country_iter))

print(next(country_iter))
print(next(country_iter))
print(next(country_iter))
print(next(country_iter))
print(next(country_iter))
print(next(country_iter))
# print(next(country_iter)) # StopIteration exception, since the iterator is ended


