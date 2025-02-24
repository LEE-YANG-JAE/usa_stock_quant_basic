print('Hello World')  # Hello World

a = 1
a = a + 1
print(a)  # 2

b = 4.5
c = a - b
print(c)  # -2.5

d = "Python is cool."
e = [1, 2, 3, 4]
f = {"Korea": "Seoul", "Japan": "Tokyo"}

print(type(d))  # <class 'str'>
print(type(e))  # <class 'list'>
print(type(f))  # <class 'dict'>

str_var1 = "Hello"
str_var2 = "Python"
str_var3 = str_var1 + " " + str_var2 + "!"  # 공백 (띄어쓰기)
print(str_var3)  # Hello Python!

period = 2.3
ret = 0.37
print("Total return is {}% after {}years.".format(100 * ret, period))  # Total return is 37.0% after 2.3years.
print(f"Total return is {100 * ret}% after {period}years.")  # Total return is 37.0% after 2.3years.

list_var1 = [10, 20, 30, "apple", "banana", "pear", [1, 2, 3]]
print(list_var1[0], list_var1[3], list_var1[-1])  # 10 apple [1, 2, 3]
print(list_var1[1: 5])  # [20, 30, 'apple', 'banana']

list_var2 = list_var1[:3] + [40, 50]
list_var2.append(60)
print(list_var2)  # [10, 20, 30, 40, 50, 60]
print(sum(list_var2), len(list_var2))  # 210 6

a = 10
b = a
a = 20
print(a, b)  # 20 10

print(list_var2)  # [10, 20, 30, 40, 50, 60]
list_var3 = list_var2
list_var3[0] = 0
print(list_var2, list_var3)  # [0, 20, 30, 40, 50, 60] [0, 20, 30, 40, 50, 60]

list_var4 = list_var2.copy()
list_var2[0] = 100
print(list_var2, list_var3, list_var4)  # [100, 20, 30, 40, 50, 60] [100, 20, 30, 40, 50, 60] [0, 20, 30, 40, 50, 60]

dict_var1 = {'name': 'Gildong Hong', 'gender': 'male', 'age': 25}
dict_var2 = {'Date': ['2024-05-21', '2024-05-22'], 'Price': [34200, 35100]}
print(dict_var1['name'], dict_var1['gender'], dict_var1['age'])  # Gildong Hong male 25
print(dict_var2['Date'], dict_var2['Price'])  # ['2024-05-21', '2024-05-22'] [34200, 35100]

print(dict_var1.items())  # dict_items([('name', 'Gildong Hong'), ('gender', 'male'), ('age', 25)])
print(dict_var1.keys())  # dict_keys(['name', 'gender', 'age'])
print(dict_var2.values())  # dict_values([['2024-05-21', '2024-05-22'], [34200, 35100]])

tuple_var1 = (10, 20, 30)
print(tuple_var1[1])  # 20
print(sum(tuple_var1), len(tuple_var1))  # 60 3
x, y, z = tuple_var1
print(x, y, z)  # 10 20 30

a = 8
b = 5
c = 2

print(a * b, a / b, a // b, a % b)  # 40 1.6 1 3
print(b ** 3)  # 125
print(5 + 3 * c ** 2 / 4 - 2)  # 6.0

a = True
b = False
c = 10 > 5
print(a, b, c, a + b + c) # True False True 2
print(a and b, a or b, not a) # False True False
