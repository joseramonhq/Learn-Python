# Create an empty dictionary called dog
dog = dict()  # ✅ Correcto
dog = {}  # ✅ Correcto

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Belmont'  # ✅ Correcto
dog['color'] = 'negro'  # ✅ Correcto
dog['breed'] = 'Pastor'  # ✅ Correcto
dog['legs'] = 4  # ✅ Correcto
dog['age'] = 12  # ✅ Correcto

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
student = {
    'first_name': 'Jose',
    'last_name': 'Ramon',
    'gender': 'Varón',
    'age': 50,
    'marital_status': 'Soltero',
    'skills': ['Programar', 'Leer'],
    'country': 'España',
    'city': 'Santander',
    'address': 'Panamá',
}  # ✅ Correcto

# Get the length of the student dictionary
length = len(student)  # ✅ Correcto
print("Length of student dictionary:", length)

# Get the value of skills and check the data type, it should be a list
sk = student['skills']  # ✅ Correcto
check = type(sk)  # ✅ Correcto
print("Skills:", sk, "Type:", check)

# Modify the skills values by adding one or two skills
# ❌ Error: Añades habilidades redundantes y poco claras.
# Tu código:
# student['skills'].append('Cagar')
# student['skills'].extend(['Cagar Mucho', 'Mear'])

student['skills'].append('Escribir')  # ✅ Correcto: Añade una habilidad relevante.
student['skills'].extend(['Hablar', 'Analizar'])  # ✅ Correcto: Extiende con habilidades útiles.
print("Updated skills:", student['skills'])

# Get the dictionary keys as a list
lst = list(student.keys())  # ✅ Correcto
print("Dictionary keys:", lst)

# Get the dictionary values as a list
lst2 = list(student.values())  # ✅ Correcto
print("Dictionary values:", lst2)

# Change the dictionary to a list of tuples using items() method
lst3 = list(student.items())  # ✅ Correcto
print("Dictionary as list of tuples:", lst3)

# Delete one of the items in the dictionary
removed_skill = student['skills'].pop()  # Elimina el último elemento de la lista 'skills'.
print("Removed skill:", removed_skill)

# Delete one of the dictionaries
del student  # ✅ Correcto: Elimina el diccionario por completo.
print("Student dictionary deleted.")
