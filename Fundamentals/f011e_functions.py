import math
import json

# Leer el archivo JSON con la codificación correcta
with open('countries_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 1. Función para sumar dos números
def add_two_numbers(one, two):
    return one + two
# ✅ Correcto: La función es funcional y clara.
# 💡 Mejora: Se puede agregar validación para verificar que ambos parámetros son números.
def add_two_numbers(one, two):
    if not isinstance(one, (int, float)) or not isinstance(two, (int, float)):
        raise ValueError("Ambos parámetros deben ser números.")
    return one + two

# 2. Calcular el área de un círculo
def area_of_circle(r):
    return 3.14 * r * r
# ✅ Correcto: La fórmula está correctamente implementada.
# 💡 Mejora: Utilizar `math.pi` para mayor precisión matemática.
def area_of_circle(r):
    return math.pi * r ** 2

# 3. Sumar argumentos arbitrarios
def add_all_nums(*args):
    return sum(x for x in args if type(x) == int)
# ✅ Correcto: Filtra los valores y suma los números enteros.
# ⚠️ Problema: No se valida si hay elementos no numéricos y devuelve 0 silenciosamente si todos los elementos son inválidos.
# 💡 Mejora: Incluir un manejo explícito de errores si algún argumento no es un número.
def add_all_nums(*args):
    if not all(isinstance(x, (int, float)) for x in args):
        raise ValueError("Todos los argumentos deben ser números.")
    return sum(args)

# 4. Convertir de Celsius a Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
# ✅ Correcto: La fórmula es precisa.
# 💡 Mejora: No requiere mejora.
# La implementación ya es óptima, no se requiere una mejora adicional.

# 5. Determinar la estación según el mes
def check_season(month):
    seasons = {
        'spring': {'March', 'April', 'May'},
        'summer': {'June', 'July', 'August'},
        'autumn': {'September', 'October', 'November'},
        'winter': {'December', 'January', 'February'}
    }
    for season, months in seasons.items():
        if month in months:
            return season
# ✅ Correcto: Lógica clara y funcional.
# ⚠️ Problema: Podría ser sensible a mayúsculas/minúsculas.
# 💡 Mejora: Convertir `month` a formato estándar (`title` o `lower`) antes de comparar.
def check_season(month):
    month = month.title()  # Asegura el formato estándar
    seasons = {
        'spring': {'March', 'April', 'May'},
        'summer': {'June', 'July', 'August'},
        'autumn': {'September', 'October', 'November'},
        'winter': {'December', 'January', 'February'}
    }
    for season, months in seasons.items():
        if month in months:
            return season

print(check_season('september'))  # Ejemplo de prueba

# 6. Calcular la pendiente de una línea
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("La pendiente es indefinida (línea vertical).")
    return (y2 - y1) / (x2 - x1)
# ✅ Correcto: Lógica clara y manejo de excepciones.
# No se requiere mejora adicional.

# 7. Resolver ecuación cuadrática
def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        solution1 = (-b + math.sqrt(discriminant)) / (2 * a)
        solution2 = (-b - math.sqrt(discriminant)) / (2 * a)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        solution1 = complex(real_part, imaginary_part)
        solution2 = complex(real_part, -imaginary_part)
    return solution1, solution2
# ✅ Correcto: Implementación completa que maneja soluciones reales y complejas.
# No se requiere mejora adicional.

# 8. Imprimir una lista
def print_list(lst):
    for item in lst:
        print(item)
# ✅ Correcto: Cumple su función de forma clara.
# No se requiere mejora adicional.

# 9. Invertir una lista
def reverse_list(lst):
    lst.reverse()
    return lst
# ✅ Correcto: Utiliza métodos nativos de Python para invertir listas.
# 💡 Mejora: Alternativamente, podría usarse slicing: `return lst[::-1]`.
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3, 4, 5]))  # Ejemplo de prueba

# 10. Capitalizar elementos de una lista
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
# ✅ Correcto: Usa comprensión de listas para procesar los elementos.
# 💡 Mejora: Verificar que los elementos de la lista sean cadenas antes de capitalizarlos.
def capitalize_list_items(lst):
    if not all(isinstance(item, str) for item in lst):
        raise ValueError("Todos los elementos de la lista deben ser cadenas.")
    return [item.capitalize() for item in lst]

print(capitalize_list_items(["aaa", "bbbbb", "cccccccc"]))  # Ejemplo de prueba

# 11. Agregar elemento a una lista
def add_item(lst, item):
    lst.append(item)
    return lst
# ✅ Correcto: Añade un elemento al final de la lista.
# 💡 Mejora: Asegurarse de que el parámetro `lst` sea una lista.
def add_item(lst, item):
    if not isinstance(lst, list):
        raise TypeError("El primer argumento debe ser una lista.")
    lst.append(item)
    return lst

# 12. Eliminar elemento de una lista
def remove_item(lst, item):
    lst.remove(item)
    return lst
# ✅ Correcto: Elimina el elemento dado si existe en la lista.
# 💡 Mejora: Manejar el caso donde el elemento no esté en la lista.
def remove_item(lst, item):
    if item not in lst:
        raise ValueError("El elemento no existe en la lista.")
    lst.remove(item)
    return lst

# 13. Suma de números en un rango
def sum_of_numbers(n):
    return sum(range(n + 1))
# ✅ Correcto: Suma los números de 0 a n eficientemente.
# 💡 Mejora: Validar que el parámetro sea un número entero no negativo.
def sum_of_numbers(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El parámetro debe ser un entero no negativo.")
    return sum(range(n + 1))

print(sum_of_numbers(5))  # Ejemplo de prueba

# 14. Suma de números impares
def sum_of_odds(n):
    return sum(x for x in range(1, n + 1) if x % 2 == 1)
# ✅ Correcto: Filtra y suma solo los impares.
# 💡 Mejora: Agregar validación de entrada como en `sum_of_numbers`.
def sum_of_odds(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El parámetro debe ser un entero no negativo.")
    return sum(x for x in range(1, n + 1) if x % 2 == 1)

# 15. Suma de números pares
def sum_of_even(n):
    return sum(x for x in range(0, n + 1) if x % 2 == 0)
# ✅ Correcto: Filtra y suma solo los pares.
# 💡 Mejora: Agregar validación de entrada como en `sum_of_numbers`.
def sum_of_even(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El parámetro debe ser un entero no negativo.")
    return sum(x for x in range(0, n + 1) if x % 2 == 0)

# Exercises: Level 2
# 16. Contar pares e impares
def evens_and_odds(n):
    evens = sum(1 for x in range(n + 1) if x % 2 == 0)
    odds = sum(1 for x in range(n + 1) if x % 2 != 0)
    return evens, odds
# ✅ Correcto: Cuenta correctamente pares e impares usando comprensión de listas.
# 💡 Mejora: Validar que el parámetro sea un entero no negativo.
def evens_and_odds(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El parámetro debe ser un entero no negativo.")
    evens = sum(1 for x in range(n + 1) if x % 2 == 0)
    odds = sum(1 for x in range(n + 1) if x % 2 != 0)
    return evens, odds

print(evens_and_odds(100))  # Ejemplo de prueba

# 17. Factorial
def factorial(n):
    prod = 1
    for t in range(1, n + 1):
        prod *= t
    return prod
# ✅ Correcto: Implementación tradicional para calcular factoriales.
# 💡 Mejora: Manejar casos de entrada no válida y usar `math.factorial` para mayor eficiencia.
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El parámetro debe ser un entero no negativo.")
    return math.factorial(n)

# 18. Verificar si una lista está vacía
def is_empty(lst):
    return len(lst) == 0
# ✅ Correcto: Devuelve True si la lista está vacía, False de lo contrario.
# 💡 Mejora: Validar que el argumento sea una lista.
def is_empty(lst):
    if not isinstance(lst, list):
        raise TypeError("El argumento debe ser una lista.")
    return len(lst) == 0

# 19. Calcular estadísticas

# Calcular la media
def calculate_mean(lst):
    return sum(lst) / len(lst)
# ✅ Correcto: Calcula la media correctamente.
# 💡 Mejora: Verificar que la lista no esté vacía y que contenga solo números.
def calculate_mean(lst):
    if not lst:
        raise ValueError("La lista no puede estar vacía.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Todos los elementos de la lista deben ser números.")
    return sum(lst) / len(lst)

# Calcular la mediana
def calculate_median(lst):
    lst = sorted(lst)
    mid = len(lst) // 2
    return (lst[mid] if len(lst) % 2 != 0 else (lst[mid - 1] + lst[mid]) / 2)
# ✅ Correcto: Calcula correctamente la mediana.
# 💡 Mejora: Validar que la lista no esté vacía y contenga números.
def calculate_median(lst):
    if not lst:
        raise ValueError("La lista no puede estar vacía.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Todos los elementos de la lista deben ser números.")
    lst = sorted(lst)
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 != 0 else (lst[mid - 1] + lst[mid]) / 2

# Calcular la moda
def calculate_mode(lst):
    return max(set(lst), key=lst.count)
# ✅ Correcto: Calcula correctamente la moda.
# 💡 Mejora: Manejar casos en los que la lista esté vacía o no haya una moda única.
def calculate_mode(lst):
    if not lst:
        raise ValueError("La lista no puede estar vacía.")
    return max(set(lst), key=lst.count)

# Calcular el rango
def calculate_range(lst):
    return max(lst) - min(lst)
# ✅ Correcto: Calcula correctamente el rango.
# 💡 Mejora: Verificar que la lista no esté vacía.
def calculate_range(lst):
    if not lst:
        raise ValueError("La lista no puede estar vacía.")
    return max(lst) - min(lst)

# Calcular la varianza
def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)
# ✅ Correcto: Calcula correctamente la varianza.
# 💡 Mejora: Validar la lista como en `calculate_mean`.
def calculate_variance(lst):
    if not lst:
        raise ValueError("La lista no puede estar vacía.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Todos los elementos de la lista deben ser números.")
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

# Calcular la desviación estándar
def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
# ✅ Correcto: Calcula correctamente la desviación estándar.
# 💡 Mejora: Validar la lista como en `calculate_variance`.
def calculate_std(lst):
    if not lst:
        raise ValueError("La lista no puede estar vacía.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Todos los elementos de la lista deben ser números.")
    return math.sqrt(calculate_variance(lst))

# 20. Verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# ✅ Correcto: Comprueba la primalidad con optimización de raíz cuadrada.
# 💡 Mejora: Asegurarse de que el parámetro sea un número entero.
def is_prime(n):
    if not isinstance(n, int):
        raise ValueError("El parámetro debe ser un número entero.")
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 21. Verificar unicidad en una lista
def check_uniques(lst):
    return len(set(lst)) == len(lst)
# ✅ Correcto: Usa conjuntos para verificar elementos únicos.
# 💡 Mejora: Validar que la entrada sea una lista.
def check_uniques(lst):
    if not isinstance(lst, list):
        raise TypeError("El parámetro debe ser una lista.")
    return len(set(lst)) == len(lst)

# 22. Verificar tipo homogéneo en una lista
def same_type(lst):
    return all(isinstance(x, type(lst[0])) for x in lst)
# ✅ Correcto: Verifica si todos los elementos son del mismo tipo.
# 💡 Mejora: Validar que la lista no esté vacía.
def same_type(lst):
    if not lst:
        raise ValueError("La lista no puede estar vacía.")
    return all(isinstance(x, type(lst[0])) for x in lst)

# 23. Validar variables de Python
def is_valid_python_variable(s):
    return s.isidentifier()
# ✅ Correcto: Usa el método nativo para verificar identificadores válidos.
# 💡 Mejora: Manejar casos donde el argumento no sea una cadena.
def is_valid_python_variable(s):
    if not isinstance(s, str):
        raise TypeError("El parámetro debe ser una cadena.")
    return s.isidentifier()

# 24. Idiomas más hablados
def most_spoken_languages(dta):
    dictionary = {}
    for t in dta:
        for language in t['languages']:
            dictionary[language] = dictionary.get(language, 0) + 1
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:10]
# ✅ Correcto: Calcula correctamente los idiomas más hablados.
# 💡 Mejora: Manejar casos en los que el parámetro no sea una lista de diccionarios.
def most_spoken_languages(dta):
    if not isinstance(dta, list) or not all(isinstance(country, dict) for country in dta):
        raise TypeError("El parámetro debe ser una lista de diccionarios.")
    dictionary = {}
    for t in dta:
        for language in t['languages']:
            dictionary[language] = dictionary.get(language, 0) + 1
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:10]

print(most_spoken_languages(data))  # Ejemplo de prueba

# 25. Países más poblados
def most_populated_countries(dta):
    return sorted(dta, key=lambda x: x['population'], reverse=True)[:10]
# ✅ Correcto: Ordena y selecciona los países con mayor población.
# 💡 Mejora: Validar que el parámetro sea una lista de diccionarios y que contenga las claves necesarias.
def most_populated_countries(dta):
    if not isinstance(dta, list) or not all(isinstance(country, dict) for country in dta):
        raise TypeError("El parámetro debe ser una lista de diccionarios.")
    if not all('population' in country for country in dta):
        raise ValueError("Cada diccionario debe contener la clave 'population'.")
    return sorted(dta, key=lambda x: x['population'], reverse=True)[:10]

print(most_populated_countries(data))  # Ejemplo de prueba

# 🎉 CONGRATULATIONS ! 🎉


