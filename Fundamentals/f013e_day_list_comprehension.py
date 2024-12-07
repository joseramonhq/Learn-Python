# 💻 Exercises: Day 13
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst = list(x for x in numbers if x <= 0)
print(lst)
# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flattened_list)
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Using list comprehension create the following list of tuples:

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
lista = list((i, 1, i, i**2, i**3, i**4,i**5) for i in range(0,11))
print(lista)
# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
result = [[c.upper(), c[:3].upper(), k.upper()] for [c, k] in sum(countries, [])]
print(result)
# Change the following list to a list of dictionaries:
#
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
result = [{'country' : country.upper(), 'city': city.upper()} for sublist in countries for country,city in sublist]
print(result)
# Change the following list of lists to a list of concatenated strings:
#
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
result = [a + ' ' + b for sublist in names for a, b in sublist]
print(result)
# Write a lambda function which can solve a slope or y-intercept of linear functions.
calcular_recta = lambda x, y: (
    sum((xi - sum(x)/len(x)) * (yi - sum(y)/len(y)) for xi, yi in zip(x, y)) / sum((xi - sum(x)/len(x))**2 for xi in x),
    sum(y)/len(y) - sum(x)/len(x) * sum((xi - sum(x)/len(x)) * (yi - sum(y)/len(y)) for xi, yi in zip(x, y)) / sum((xi - sum(x)/len(x))**2 for xi in x)
)#
# 🎉 CONGRATULATIONS ! 🎉
