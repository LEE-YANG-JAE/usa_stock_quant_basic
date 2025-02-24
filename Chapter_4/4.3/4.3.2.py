import pandas as pd

s = pd.Series([10, 4, 3, 26, 12, 9])
print(type(s))
print(s)
'''
<class 'pandas.core.series.Series'>
0    10
1     4
2     3
3    26
4    12
5     9
dtype: int64
'''

s.index = ['a', 'b', 'c', 'd', 'e', 'f']
s.name = 'Test'
print(s)
'''
a    10
b     4
c     3
d    26
e    12
f     9
Name: Test, dtype: int64
'''

print(s.loc['c']) # 3
print(s.loc['b': 'd'])
'''
b     4
c     3
d    26
Name: Test, dtype: int64
'''
print(s.iloc[1: 4])
'''
b     4
c     3
d    26
Name: Test, dtype: int64
'''

t = s.iloc[:3]
print(t)
'''
a    10
b     4
c     3
Name: Test, dtype: int64
'''
t.loc['a'] = 100
print(s)
'''
a    100
b      4
c      3
d     26
e     12
f      9
Name: Test, dtype: int64
'''

s['a'] = 10
t = s.iloc[:3].copy()
t['a'] = 100
print(s)
'''
a    10
b     4
c     3
d    26
e    12
f     9
Name: Test, dtype: int64
'''
