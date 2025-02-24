a = 15
if a % 2 == 0:
    print("짝수입니다.")
if a % 3 == 0:
    print("3의 배수입니다.")
if a > 20:
    print("20보다 큽니다.")
if a < 20:
    print("20보다 작습니다.")

# 3의 배수입니다.
# 20보다 작습니다.

price_A = 25000
price_B = 77000

if price_A < 27000:
    print("Buy A")
else:
    print("Sell A")

if price_B < 70000:
    print("Buy B")
else:
    print("Sell B")

# Buy A
# Sell B

# 조건문 연습3
num = 77
if num > 100:
    print("greater than 100")
elif 90 < num <= 100:
    print("greater than 90 and less than or equal to 100")
elif 80 < num <= 90:
    print("greater than 80 and less than or equal to 90")
elif 70 < num <= 80:
    print("greater than 70 and less than or equal to 70")
else:
    print("less than or equal to 70")

# greater than 70 and less than or equal to 70

# 반복문 연습1
for i in range(10):
    print(i)

'''
0
1
2
3
4
5
6
7
8
9
'''

# 반복문 연습2
s = 0
for i in range(1, 101):
    s = s + i
print("1 + 2 + ... + 100 =", s)  # 1 + 2 + ... + 100 = 5050

# 반복문 연습3
list_var = [i for i in range(1, 5 + 1)]
for i in list_var:
    j = i * 10
    print(i, j)

'''
1 10
2 20
3 30
4 40
5 50
'''

# 반복문 연습4
dict_var = {'key1': 10, 'key2': 20, 'key3': 30}
for j in dict_var:
    print(j, dict_var[j])
'''
key1 10
key2 20
key3 30
'''

# 반복문 연습5
fruits = ["peach", "water melon", "apple", "lemon", "pear"]
for i, fruit in enumerate(fruits):
    print(f"{i + 1}번 과일은 {fruit}입니다.")

'''
1번 과일은 peach입니다.
2번 과일은 water melon입니다.
3번 과일은 apple입니다.
4번 과일은 lemon입니다.
5번 과일은 pear입니다.
'''

# 반복문 연습6
for i in range(2, 10):
    print(f"=== {i}단 ===")  # 제목 출력
    for j in range(1, 10):
        print(f"{i}x{j}={i * j}")
    print()  # 빈줄 출력

'''
=== 2단 ===
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
2x6=12
2x7=14
2x8=16
2x9=18

=== 3단 ===
3x1=3
3x2=6
3x3=9
3x4=12
3x5=15
3x6=18
3x7=21
3x8=24
3x9=27

=== 4단 ===
4x1=4
4x2=8
4x3=12
4x4=16
4x5=20
4x6=24
4x7=28
4x8=32
4x9=36

=== 5단 ===
5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45

=== 6단 ===
6x1=6
6x2=12
6x3=18
6x4=24
6x5=30
6x6=36
6x7=42
6x8=48
6x9=54

=== 7단 ===
7x1=7
7x2=14
7x3=21
7x4=28
7x5=35
7x6=42
7x7=49
7x8=56
7x9=63

=== 8단 ===
8x1=8
8x2=16
8x3=24
8x4=32
8x5=40
8x6=48
8x7=56
8x8=64
8x9=72

=== 9단 ===
9x1=9
9x2=18
9x3=27
9x4=36
9x5=45
9x6=54
9x7=63
9x8=72
9x9=81
'''

# 반복문 연습7
nums = [i for i in range(1, 11)]
for k in nums:
    if k % 3 == 0:
        continue
    print(k)
    if k > 7:
        break

'''
1
2
4
5
7
8
'''

# 반복문 연습8
s = 0
i = 0
while i < 100:
    i = i + 1
    s = s + i
print("1 + 2 + ... + 100 =", s)  # 1 + 2 + ... + 100 = 5050

# 반복문 연습9
epsilon = 1.0
decay_factor = 0.9
i = 1
while True:
    epsilon = epsilon * decay_factor
    if epsilon < 1e-7:
        break
    i = i + 1
print(i, epsilon)  # 153 9.979388823371132e-08


# 입력값, 반환값 모두 없는 함수
def greeting():
    print("How are you dong?")


# 반환값이 없는 함수
def even_odd(a):
    if a % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


# 입력값, 반환값 모두 있는 함수
def square_sum(a, b):
    return a ** 2 + b ** 2


# 함수 연습2
greeting()
even_odd(10)
result = square_sum(3, 4)
print(result)
'''
How are you dong?
Even number
25
'''


# 함수 연습3
def bonus(a, b, c=10):
    res = a + b + c
    return res


res1 = bonus(10, 20)
res2 = bonus(10, 20, 15)
print(res1, res2)  # 40 45

# 함수 연습4
a = 10


def my_func(x):
    y = 20
    res = x + y + a
    return res


res = my_func(3)
print(res)  # 33

print(f"a={a}")

'''
print(f"y={y}")
Traceback (most recent call last):
   line 294, in <module
    print(f"y={y}")
               ^
NameError: name 'y' is not defined
'''

'''
# 함수 연습6
a = 10

def my_func(x):
    global a
    global y
    y = 20
    a = a + 1
    res = x + y + a
    return res


res = my_func(3)
print(res)
print(f"y={y}")

# y=20
'''
