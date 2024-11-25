# 💻 Exercises: Day 9

# Exercises: Level 1

# Get user input for age and determine if they are old enough to drive
age = input("Enter your age: ")
if int(age) >= 18:  # ✅ Correcto: La lógica para verificar la mayoría de edad está bien implementada.
    print("You are old enough to learn to drive.")  # ✅ Correcto.
else:
    print('You need %d more year%s to learn to drive.' % (18 - int(age), 's' if 18 - int(age) > 1 else ''))
    # ✅ Correcto: El cálculo de años restantes funciona y usa una condición para pluralizar correctamente.



# Compare the values of my_age and your_age using if … else
age = 25
my_age = int(input('Enter your age: '))
print('You are the same age as me.' if my_age - age == 0 else 'You are %d year%s %s than me' % (
    abs(my_age - age), 's' if abs(my_age - age) > 1 else '', 'older' if my_age - age > 0 else 'younger'))
    # ✅ Correcto: El cálculo de diferencias y las condiciones están bien implementadas.

# 💡 Mejora
difference = abs(my_age - age)
older_or_younger = 'older' if my_age > age else 'younger'
print(f'You are the same age as me.' if difference == 0 else f'You are {difference} year{"s" if difference > 1 else ""} {older_or_younger} than me.')



# Get two numbers from the user and compare them
one = int(input('Enter number one: '))  # ✅ Correcto.
two = int(input('Enter number two: '))  # ✅ Correcto.
if one > two:  # ✅ Correcto.
    print('{} is greater than {}.'.format(one, two))  # ✅ Correcto.
elif two > one:  # ✅ Correcto.
    print('{} is greater than {}.'.format(two, one))  # ✅ Correcto.
else:  # ✅ Correcto.
    print('{} is equal to {}.'.format(two, one))  # ✅ Correcto.



# Exercises: Level 2

# Write a code which gives grade to students according to their scores
score = int(input('Enter a score: '))
if 80 <= score <= 100:  # ✅ Correcto.
    print('A')
elif score >= 70:  # ✅ Correcto.
    print('B')
elif score >= 60:  # ✅ Correcto.
    print('C')
elif score >= 50:  # ✅ Correcto.
    print('D')
else:  # ✅ Correcto.
    print('F')


# Check the season based on the month
month = input('Enter a month: ')
if month in ('September', 'October', 'November'):  # ✅ Correcto.
    print('The season is Autumn')
elif month in ('December', 'January', 'February'):  # ✅ Correcto.
    print('The season is winter')
elif month in ('March', 'April', 'May'):  # ✅ Correcto.
    print('The season is spring')
else:  # ✅ Correcto.
    print('The season is summer')


# 💡 Mejora
seasons = {
    'Autumn': ['September', 'October', 'November'],
    'Winter': ['December', 'January', 'February'],
    'Spring': ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August']
}
for season, months in seasons.items():
    if month in months:
        print(f'The season is {season}')
        break


# The following list contains some fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
if fruit not in fruits:  # ✅ Correcto.
    fruits.append(fruit)  # ✅ Correcto.
    print(fruits)  # ✅ Correcto.
else:
    print('That fruit already exist in the list')  # ✅ Correcto.



# Exercises: Level 3

# Person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, and print the middle skill
print('skills' in person)  # ✅ Correcto.
if person['skills']:  # ✅ Correcto.
    if len(person['skills']) % 2 == 0:  # ✅ Correcto.
        print(person['skills'][len(person['skills']) // 2 - 1], person['skills'][len(person['skills']) // 2])
    else:  # ✅ Correcto.
        print(person['skills'][len(person['skills']) // 2])

# Check if the person has the 'Python' skill
if person['skills']:  # ✅ Correcto.
    print('Python' in person['skills'])  # ✅ Correcto.

# Identify the developer type
string = ''
if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:  # ✅ Correcto.
    string = 'He is a fullstack developer'
    print(string)
else:
    if 'React' in person['skills'] and 'JavaScript' in person['skills']:  # ✅ Correcto.
        string = 'He is a front end developer'
        print(string)
    if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:  # ✅ Correcto.
        string = 'He is a backend developer'
        print(string)
if len(string) == 0:  # ✅ Correcto.
    print('unknown title')

# Check if the person is married and lives in Finland
if person['is_marred'] and person['country'] == 'Finland':  # ✅ Correcto.
    print('{} {} lives in {}. He is married'.format(person['first_name'], person['last_name'], person['country']))  # ✅ Correcto.

# 🎉 CONGRATULATIONS ! 🎉
