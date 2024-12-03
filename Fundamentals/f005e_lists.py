# 💻 Exercises: Day 5
# from Fundamentals.f004_strings import country

## Exercises: Level 1

# 1. Declare an empty list
lst = list()
lst2 = []  # ✅ Correcto

# 2. Declare a list with more than 5 items
lst3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # ✅ Correcto

# 3. Find the length of your list
print(3, len(lst3))  # ✅ Correcto

# 4. Get the first item, the middle item, and the last item of the list
a = lst3[0]
b = lst3[len(lst3) // 2]
c = lst3[-1]  # ✅ Uso de índices correcto
print(4, a, b, c)  # ✅ Correcto

# 5. Declare a list called mixed_data_types, put your name, age, height, marital status, and address
mixed_data_types = ['Jose', 50, 1.65, 'soltero', 'Santander']  # ✅ Correcto

# 6. Declare a list variable named it_companies and assign initial values
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']  # ✅ Correcto

# 7. Print the list using print()
print(7, it_companies)  # ✅ Correcto

# 8. Print the number of companies in the list
print(8, len(it_companies))  # ✅ Correcto

# 9. Print the first, middle, and last company
print(9, it_companies[0])  # ✅ Correcto
print(9, it_companies[len(it_companies) // 2])  # ✅ Correcto
print(9, it_companies[-1])  # ✅ Correcto

# 10. Print the list after modifying one of the companies
it_companies[3] = 'Adobe'  # ✅ Correcto
print(10, it_companies)

# 11. Add an IT company to the list
it_companies.append('Atari')  # ✅ Correcto
print(11, it_companies)

# 12. Insert an IT company in the middle of the list
it_companies.insert(len(it_companies) // 2, 'Otra')  # ✅ Correcto
print(12, it_companies)

# 13. Change one of the it_companies names to uppercase (excluding IBM)
it_companies[2] = it_companies[2].upper()  # ✅ Correcto
print(13, it_companies)

# 14. Join the it_companies with a string '#;  '
word = '#'.join(it_companies)  # ✅ Correcto
print(14, word)

# 15. Check if a certain company exists in the list
boo = 'IBM' in it_companies  # ✅ Correcto
print(15, "Is IBM in the list?", boo)

# 16. Sort the list using sort() method
it_companies.sort()  # ✅ Correcto
print(16, it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()  # ✅ Correcto
print(17, it_companies)

# 18. Slice out the first 3 companies from the list
first_three_removed = it_companies[3:]  # ✅ Correcto
print(18, first_three_removed)

# 19. Slice out the last 3 companies from the list
last_three_removed = it_companies[:-3]  # ✅ Correcto
print(19, last_three_removed)

# 20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
del it_companies[middle_index]  # ✅ Correcto
print(20, it_companies)

# 21. Remove the first IT company from the list
it_companies.pop(0)  # ✅ Correcto
print(21, it_companies)

# 22. Remove the last IT company from the list
it_companies.pop(-1)  # ✅ Correcto
print(22, it_companies)

# 23. Remove all IT companies from the list
it_companies.clear()  # ✅ Correcto
print(23, it_companies)

# 24. Destroy the IT companies list
del it_companies  # ✅ Correcto

# 25. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.extend(back_end)  # ✅ Correcto
print(25, front_end)

# 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux
full_stack = front_end.copy()
redux_index = full_stack.index('Redux')  # ✅ Correcto
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(26, full_stack)

# ❌ ERROR: Añadir directamente 'Python' y 'Redux' no posiciona correctamente.
# ❌ Tu código:
# full_stack.append('Python')
# full_stack.append('Redux')

# ✅ Corrección:
# full_stack.insert(redux_index + 1, 'Python')
# full_stack.insert(redux_index + 2, 'SQL')
# Esto posiciona correctamente los elementos.

# Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()  # ✅ Correcto
min_age = ages[0]  # ✅ Correcto
max_age = ages[-1]  # ✅ Correcto

# Add the min age and the max age again to the list
ages.extend([min_age, max_age])  # ✅ Correcto

# Find the median age (one middle item or two middle items divided by two)
# ❌ Error: Falta paréntesis para sumar los dos valores antes de dividir.
if len(ages) % 2 == 0:
    median_age = ages[len(ages) // 2 - 1] + ages[len(ages) // 2] / 2
    #          ^ falta paréntesis aquí para calcular correctamente
else:
    median_age = ages[len(ages) // 2] / 2
    #                 ^ Error: El elemento central no debe dividirse entre 2 si la longitud es impar.

# ✅ Corrección:
if len(ages) % 2 == 0:
    median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2  # Añadido paréntesis
else:
    median_age = ages[len(ages) // 2]  # Eliminada división incorrecta.

print("Median age:", median_age)

# Find the average age (sum of all items divided by their number)
# ❌ Error: Se usa un bucle manual para sumar, lo cual es innecesario.
suma = 0  # Variable `sum` está sombreando la función `sum()` de Python, lo cual puede ser problemático.
print('¡****************************************')
for i in ages:
    suma += i

# ✅ Corrección:
average = sum(ages) / len(ages)  # Usar directamente `sum()` para mayor claridad.
print("Average age:", average)

# Find the range of the ages (max minus min)
# ❌ Error: Uso redundante de `sorted()` en lugar de usar directamente `max` y `min`.
print('range: ', sorted(ages, reverse=True)[0] - sorted(ages)[0])

# ✅ Corrección:
age_range = max(ages) - min(ages)  # Usar funciones directas para mejorar claridad y eficiencia.
print("Range:", age_range)

# Compare the value of (min - average) and (max - average), use abs() method
# ✅ Correcto: Esto no tiene errores.
print("Is |min - average| > |max - average|?:", abs(min_age - average) > abs(max_age - average))

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# ❌ Error: Lógica incorrecta para encontrar los países del medio.
middle = (' ' + countries[len(countries) // 2 + 1]) if len(countries) % 2 == 0 else ''
#          ^ Esto no selecciona correctamente dos países para listas pares.

middle_countries = countries[len(countries) // 2] + middle
#                     ^ Error: Solo maneja un país, no ambos para listas pares.

# ✅ Corrección:
if len(countries) % 2 == 0:
    middle_countries = countries[len(countries) // 2 - 1 : len(countries) // 2 + 1]  # Slicing para seleccionar ambos.
else:
    middle_countries = [countries[len(countries) // 2]]  # Seleccionar un país si es impar.

print("Middle country(ies):", middle_countries)

# Divide the countries list into two equal lists if it is even; if not, one more country for the first half.
# ❌ Error: Lógica difícil de leer para dividir la lista.
lst = countries[0 : len(countries) // 2 + 1 if len(countries) % 2 == 1 else len(countries) // 2]
#      ^ El slicing es correcto, pero la lógica es confusa.

# ✅ Mejora:
first_half = countries[: len(countries) // 2 + (len(countries) % 2)]
second_half = countries[len(first_half) :]  # Usar longitud de la primera mitad para calcular la segunda.
print("First half:", first_half)
print("Second half:", second_half)

# Unpack the first three countries and the rest as scandic countries
# ✅ Correcto: Esto no tiene errores.
china, russia, usa, *scandic = countries
print("China:", china, "Russia:", russia, "USA:", usa, "Scandic countries:", scandic)

# 🎉 CONGRATULATIONS ! 🎉
