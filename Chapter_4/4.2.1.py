print('Hello World')

a = 1
a = a + 1
print(a)

b = 4.5
c = a - b
print(c)

d = "Python is cool."
e = [1, 2, 3, 4]
f = {"Korea": "Seoul", "Japan": "Tokyo"}

print(type(d))
print(type(e))
print(type(f))

str_var1 = "Hello"
str_var2 = "Python"
str_var3 = str_var1 + " " + str_var2 + "!"  # 공백 (띄어쓰기)
print(str_var3)

period = 2.3
ret = 0.37
print("Total return is {}% after {}years.".format(100 * ret, period))
print(f"Total return is {100 * ret}% after {period}years.")

list_var1 = [10, 20, 30, "apple", "banana", "pear", [1, 2, 3]]
print(list_var1[0], list_var1[3], list_var1[-1])
print(list_var1[1: 5])

list_var2 = list_var1[:3] + [40, 50]
list_var2.append(60)
print(list_var2)
print(sum(list_var2), len(list_var2))