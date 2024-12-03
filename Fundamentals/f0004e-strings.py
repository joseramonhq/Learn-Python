# 🌕 You are an extraordinary person and you have a remarkable potential. 
# You have just completed day 4 challenges and you are four steps ahead on your way to greatness. 
# Now do some exercises for your brain and muscles.

## 💻 Exercises - Day 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print(1, 'Thirty', 'Days', 'Of', 'Python')  # ❌ Esto no concatena las palabras en una sola cadena; solo las imprime separadas por comas.
print(1, ' '.join(['Thirty', 'Days', 'Of', 'Python']))  # ✅ Corrección: Usar `join` para concatenar con espacios.
print(1, '{} {} {} {}'.format('Thirty', 'Days', 'Of', 'Python'))  # ✅ También es correcto usar `format`.

# 2. Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'.
print(2, ' '.join(['Coding', 'For', 'All']))  # ✅ Se aplica la misma técnica que en el ejercicio 1.

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4. Print the variable company using print().
print(4, company)  # ✅ Correcto.

# 5. Print the length of the company string using len() method and print().
print(5, len(company))  # ✅ Correcto.

# 6. Change all the characters to uppercase letters using upper() method.
print(6, company.upper())  # ✅ Correcto.

# 7. Change all the characters to lowercase letters using lower() method.
print(7, company.lower())  # ✅ Correcto.

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string "Coding For All".
print(8, company.capitalize())  # ✅ Correcto.
print(8, company.title())  # ✅ Correcto.
print(8, company.swapcase())  # ✅ Correcto.

# 9. Cut (slice) out the first word of "Coding For All" string.
print(9, company[7:])  # ✅ Uso correcto del slicing.

# 10. Check if "Coding For All" string contains the word "Coding" using the method index, find or other methods.
print(10, "Coding" in company)  # ❌ `__contains__` no es necesario. ✅ Usar el operador `in` es más legible.

# 11. Replace the word "Coding" in the string "Coding For All" with "Python".
print(11, company.replace("Coding", "Python"))  # ✅ Correcto.

# 12. Change "Python for Everyone" to "Python for All" using the replace method.
print(12, 'Python for Everyone'.replace("Everyone", "All"))  # ✅ Correcto.

# 13. Split the string "Coding For All" using space as the separator (split()).
print(13, company.split(" "))  # ✅ Correcto.

# 14. Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma.
print(14, "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))  # ✅ Correcto.

# 15. What is the character at index 0 in the string "Coding For All".
print(15, company[0])  # ✅ Correcto.

# 16. What is the last index of the string "Coding For All".
print(16, company[-1])  # ✅ Correcto.

# 17. What character is at index 10 in "Coding For All" string.
print(17, company[10])  # ✅ Correcto.

# 18. Create an acronym or an abbreviation for the name "Python For Everyone".
print(18, ''.join([word[0] for word in 'Python For Everyone'.split()]))  # ✅ Corrección: Forma más clara y escalable.

# 19. Create an acronym or an abbreviation for the name "Coding For All".
print(19, ''.join([word[0] for word in company.split()]))  # ✅ Corrección similar al ejercicio anterior.

# 20. Use index to determine the position of the first occurrence of "C" in "Coding For All".
print(20, company.index("C"))  # ✅ Correcto.

# 21. Use index to determine the position of the first occurrence of "F" in "Coding For All".
print(21, company.index("F"))  # ✅ Correcto.

# 22. Use rfind to determine the position of the last occurrence of "l" in "Coding For All People".
print(22, 'Coding For All People'.rfind("l"))  # ✅ Correcto.

# 23. Use index or find to find the position of the first occurrence of the word "because" in the sentence.
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(23, sentence.find("because"))  # ✅ Correcto.

# 24. Use rindex to find the position of the last occurrence of the word "because".
print(24, sentence.rindex("because"))  # ✅ Correcto.

# 25. Slice out the phrase "because because because" from the sentence.
print(25, sentence[sentence.find("because"):sentence.rindex("because") + len("because")])  # ✅ Corrección: Usar slicing.

# 26. Does "Coding For All" start with a substring "Coding"?
print(26, company.startswith("Coding"))  # ✅ Correcto.

# 27. Does "Coding For All" end with a substring "coding"?
print(27, company.endswith("coding"))  # ✅ Correcto.

# 28. Remove the left and right trailing spaces in the string.
print(28, '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'.strip())  # ✅ Correcto.

# 29. Which variable returns True with isidentifier()? 
# thirty_days_of_python is valid; 30DaysOfPython is not.
print(29, "30DaysOfPython".isidentifier())  # ❌ Incorrecto: Retorna False.
print(29, "thirty_days_of_python".isidentifier())  # ✅ Correcto.

# 30. Join the Python library names with a hash and space.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(30, ' # '.join(libraries))  # ✅ Correcto.

# 31. Use the new line escape sequence to separate sentences.
print(31, 'I am enjoying this challenge.\nI just wonder what is next.')  # ✅ Correcto.

# 32. Use a tab escape sequence to write structured text.
print(32, 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')  # ✅ Correcto.

# 33. Use string formatting to display structured text.
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')  # ✅ Usar `f-strings` para mayor claridad.

# 34. String formatting for arithmetic operations.
a, b = 8, 6
print(f'{a} + {b} = {a + b}')  # ✅ Correcto.
print(f'{a} - {b} = {a - b}')  # ✅ Correcto.
print(f'{a} * {b} = {a * b}')  # ✅ Correcto.
print(f'{a} / {b} = {a / b:.2f}')  # ✅ Correcto.
print(f'{a} % {b} = {a % b}')  # ✅ Correcto.
print(f'{a} // {b} = {a // b}')  # ✅ Correcto.
print(f'{a} ** {b} = {a ** b}')  # ✅ Correcto.

# 🎉 CONGRATULATIONS! 🎉
