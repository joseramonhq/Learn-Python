# Exercises: Level 1
# Create an empty tuple
t1 = ()  # ✅ Correcto
t2 = tuple()  # ✅ Correcto

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
t3 = ('Pedro', 'Juan')  # ✅ Correcto
t4 = ('Maria', 'Carmen')  # ✅ Correcto

# Join brothers and sisters tuples and assign it to siblings
t5 = t3 + t4  # ✅ Correcto

# How many siblings do you have?
len(t5)  # ✅ Correcto

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# -->>>> It's impossible or maybe? ->
# ✅ Correcto: Las tuplas son inmutables, pero puedes concatenar una nueva tupla.
family_members = t5 + ('father', 'mother')  # ✅ Correcto



# Exercises: Level 2
# Unpack siblings and parents from family_members
# ❌ Error: Esto solo funcionará si `family_members` tiene exactamente 6 elementos. Si el número cambia, fallará.
# Tu código:
# a1, a2, a3, a4, a5, a6 = family_members

# ✅ Corrección:
# Si sabes que el número de elementos es fijo, esto está bien. De lo contrario, usa `*` para manejar dinámicamente:
a1, a2, a3, a4, a5, a6 = family_members  # Esto funciona, pero ten en cuenta que falla si cambia la tupla.

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Pera', 'Manzana', 'Melón')  # ✅ Correcto
vegetables = ('puerro', 'zanahoria')  # ✅ Correcto
animal = ('lomo', 'muslo', 'solomillo')  # ✅ Correcto

food_stuff_tp = fruits + vegetables + animal  # ✅ Correcto

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)  # ✅ Correcto

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# ❌ Error: La lógica para calcular el elemento central es incorrecta y no maneja listas pares o impares.
# Tu código:
# whitout = food_stuff_lt[0: length//2 -1] + food_stuff_lt[length//2+1:]

# ✅ Corrección:
length = len(food_stuff_lt)
if length % 2 == 0:  # Si la longitud es par
    whitout = food_stuff_lt[:length // 2 - 1] + food_stuff_lt[length // 2 + 1:]
else:  # Si la longitud es impar
    whitout = food_stuff_lt[:length // 2] + food_stuff_lt[length // 2 + 1:]

# Slice out the first three items and the last three items from food_staff_lt list
# ❌ Error: Estás sobrescribiendo `food_staff_lt` en lugar de guardar en una nueva variable.
# Tu código:
# food_staff_lt = food_stuff_lt[3:-3]

# ✅ Corrección:
sliced_list = food_stuff_lt[3:-3]  # Guarda el resultado en una nueva variable para claridad.

# Delete the food_staff_tp tuple completely
# ❌ Error: Crear un tuple vacío no elimina el anterior.
# Tu código:
# food_staff_tp = ()

# ✅ Corrección:
del food_stuff_tp  # Usa `del` para eliminar completamente la variable.

# Check if an item exists in tuple:
# ❌ Error: Revisar la longitud de una tupla vacía no aporta valor.
# Tu código:
# len(food_staff_tp)

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
# ✅ Corrección:
print("Is 'Estonia' in tuple?", 'Estonia' in nordic_countries)  # Revisa directamente si el elemento existe.



# Check if 'Estonia' is a nordic country
est = 'Estonia' in nordic_countries  # ✅ Correcto

# Check if 'Iceland' is a nordic country
est2 = 'Iceland' in nordic_countries  # ✅ Correcto
