# DATA TYPES
# In Python, a data type is a classification that specifies 
# which type of value a variable can hold. 
# Python has several built-in data types, including:
# We can chdck the data type of a variable using the type() function.

# Basic Data Types
# 1.NUMERIC: 
# Integer:26, 100, -5, 0
my_integer = 42
print(type(my_integer))  # Output: <class 'int'>
print(my_integer)  # Output: 42
# Float: 3.14, -0.5, 2.0
my_float = 3.14
print(type(my_float))  # Output: <class 'float'>
print(my_float)  # Output: 3.14
# Complex: 2 + 3j, -1 - 4j
my_complex = 2 + 3j
print(type(my_complex))  # Output: <class 'complex'>
print(my_complex)  # Output: (2+3j)


# 2.SEQUENCE: 
# String: "Hello", 'Python', "123"
# List: [1, 2, 3], ["apple", "banana", "cherry"]
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(fruits[0])  # Output: apple
print(fruits[-1])  
mixed_list = [42, "hello", 3.14, True]
print(type(mixed_list))  # Output: <class 'list'>
print(mixed_list)
# Tuple: (1, 2, 3), ("apple", "banana", "cherry")
# A tuple can store multiple items of different types
my_tuple = (1, 2, 3, "Hello", True)
print(my_tuple)  # Output: (1, 2, 3, 'Hello', True)

# 3.MAPPING: Dictionary.
# {"key": "value", "name": "John", "age": 30}
# A dictionary contains key-value k pair ko hum dictionary kehtay hen.
# json file b key value pair mein hota hai.
my_dict = {"name": "Muhammad Tariq", "age":47, "city": "Karachi","education":"BSc"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}


