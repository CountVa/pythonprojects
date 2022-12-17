a = 'Hello, World!'

# Работа с регистром
print(a.capitalize())  # Преобразует первый символ в верхний регистр.
print(a.lower())  # Преобразует символы строки в нижний регистр.
print(a.upper())  # Преобразует символы строки в верхний регистр.
print(a.title())  # Преобразует первые символы подстрок в верхний регистр.

# Поиск элементов
print(a.count("o"))  # Подсчитывает число вхождений заданной подстроки sub.
print(a.find("o"))  # Отыскивает первое вхождение подстроки sub или возвращает -1.
print(a.rfind("o"))  # Отыскивает последнее вхождение подстроки.
print(a.index("o"))  # Отыскивает первое вхождение подстроки sub или возбуждает исключение.
print(a.rindex("o"))  # Отыскивает последнее вхождение"o" подстроки или возбуждает исключение.

# Проверки
print(a.isalnum())  # Проверяет, являются ли все символы в строке алфавитно-цифровыми символами.
print(a.isalpha())  # Проверяет, являются ли все символы в строке алфавитными символами.
print(a.isdigit())  # Проверяет, являются ли все символы в строке цифровыми символами.
print(a.islower())  # Проверяет, являются ли все символы в строке символами нижнего регистра.
print(a.isspace())  # Проверяет, являются ли все символы в строке пробельными символами.
print(a.istitle())  # Проверяет, являются ли первые символы всех слов символами верхнего регистра.
print(a.isupper())  # Проверяет, являются ли все символы в строке символами верхнего регистра.
print(a.endswith("!"))  # Проверяет, оканчивается ли строка подстрокой "!".
print(a.startswith("H"))  # Проверяет, начинается ли строка подстрокой "H".

# Преобразование
print(a.replace("o", "OO"))  # Замещает подстроку "o"  подстрокой "OO".
print(a.lstrip("Hle"))  # Удаляет начальные пробельные символы или символы, перечисленные в аргументе chrs.
print(a.rstrip("!ld"))  # Удаляет конечные пробельные символы или символы, перечисленные в аргументе chrs.
print(a.strip("H!"))  # Удаляет начальные и конечные пробельные символы или символы, перечисленные в аргументе chrs.

a = "125.25; 25.7; 74.1"

new_a = a.split(sep=';')
print(new_a)
new_a = ",".join(new_a)
print("Координаты:", new_a)