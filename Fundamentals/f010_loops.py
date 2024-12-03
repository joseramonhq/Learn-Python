# 💻 Exercises: Day 10
# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.

import json

# Leer el archivo JSON con la codificación correcta
with open('countries_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)  # Cargar el contenido del archivo en un diccionario de Python


for t in range(11):
    print(t)
# Iterate 10 to 0 using for loop, do the same using while loop.
for t in range(10,-1,-1):
    print(t)
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
str1=''
for t in range(7):
    str1 +='#'
    print(str1)
# Use nested loops to create the following:
#
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

print('\n\n\n')
for i in range(16):
    str2 = ''
    for j in range(16):
        if i % 2 == 0:
            if j%2 == 0:
                str2+='#'
            else:
                str2+=' '
        else:
            str2+=' '
    print(str2)



# Print the following pattern:
#
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(11):
    print('{} x {} = {}'.format(i,i,i*i))

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in languages:
    print(language)

# Use for loop to iterate from 0 to 100 and print only even numbers
for t in range(0,101,2):
    print(t)

# Use for loop to iterate from 0 to 100 and print only odd numbers
print('********************************')
for t in range(0,101):
    if t%2==1:
        print(t)

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
summa = 0
for t in range(0,101):
    summa += t
print(summa)
# The sum of all numbers is 5050.

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
evens = odds = 0
for t in range(0,101):
    if t % 2 == 0:
        evens += t
    else:
        odds += t
print('evens: ',evens)
print('odds',odds)

# The sum of all evens is 2550. And the sum of all odds is 2500.
# Exercises: Level 3

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for country in countries:
    if 'land' in country:
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']

for t in range(1, len(fruit_list) + 1):
    print(fruit_list[-t])

# Go to the data folder and use the countries_data.py file.

# What are the total number of languages in the data
set01 = set()
for country in data:
    for languages in country['languages']:
        set01.add(language)
print(len(set01))

# Find the ten most spoken languages from the data
diction = {}
for country in data:
    for language in country['languages']:
        if language not in diction:
            diction[language] = 1
        else:
            diction[language] += 1

sorted_dict_desc = dict(sorted(diction.items(), key=lambda item: item[1], reverse=True))
print(list(sorted_dict_desc.items())[:10])




# Find the 10 most populated countries in the world
print("Top 10 Most Populated Countries:")
population_dict = {country['name']: country['population'] for country in data}  # ✅ Correcto: Crear diccionario.
sorted_population = dict(sorted(population_dict.items(), key=lambda item: item[1], reverse=True))
print(list(sorted_population.items())[:10])  # ✅ Correcto: Imprimir solo los 10 primeros.


# Find the 10 most populated countries in the world
# 🎉 CONGRATULATIONS ! 🎉