# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# Find the length of the set it_companies
len(it_companies)  # ✅ Correcto

# Add 'Twitter' to it_companies
it_companies.add('Twitter')  # ✅ Correcto

# Insert multiple IT companies at once to the set it_companies
# ❌ Error: Los nombres añadidos no son de compañías reales, pero técnicamente está bien como código.
# Tu código:
# it_companies.update({'asdfsdf', 'sadfasdf', 'asdfasdf'})

# ✅ Mejora: Usa nombres más apropiados para añadir valor al ejercicio.
it_companies.update({'Twitter', 'LinkedIn', 'Tesla'})

# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')  # ✅ Correcto

# What is the difference between remove and discard
# ✅ Correcto: "discard no da error si no encuentra el item a quitar".


# Exercises: Level 2
# Join A and B
c = A.union(B)  # ✅ Correcto

# Find A intersection B
d = A.intersection(B)  # ✅ Correcto

# Is A subset of B
A.issubset(B)  # ✅ Correcto

# Are A and B disjoint sets
A.isdisjoint(B)  # ✅ Correcto

# Join A with B and B with A
# ✅ Correcto: Estas operaciones son equivalentes.
e = A.union(B)
f = B.union(A)

# What is the symmetric difference between A and B
g = A.symmetric_difference(B)  # ✅ Correcto

# Delete the sets completely
del A  # ✅ Correcto
del B  # ✅ Correcto


# Exercises: Level 3
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(ages)  # ✅ Correcto
ans = len(ages_set) <= len(ages)  # ✅ Correcto, pero la lógica puede mejorarse para mayor claridad.

# ✅ Mejora:
# Explicita cuál es más grande con una comparación directa.
is_list_bigger = len(ages) > len(ages_set)
print("Is the list bigger than the set?:", is_list_bigger)

# Explain the difference between the following data types: string, list, tuple and set
# ✅ Correcto: Tu explicación está bien, pero puede ser más detallada.
# string: Cadena de caracteres, inmutable, indexada y ordenada.
# list: Mutable, ordenada, permite duplicados, usa `[]`.
# tuple: Inmutable, ordenada, permite duplicados, usa `()`.
# set: Mutable, no indexada, no permite duplicados, usa `{}`.


# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence?
# ❌ Error: Falta el código para calcular las palabras únicas.
# Tu código incompleto:
# "Use split methods and set to get the unique words."

# ✅ Corrección:
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())  # Convierte las palabras en un conjunto para eliminar duplicados.
print("Number of unique words:", len(unique_words))  # Muestra el número de palabras únicas.
print("Unique words:", unique_words)  # Opcional: Lista las palabras únicas.

# 🎉 CONGRATULATIONS ! 🎉
