import numpy as np
import pandas as pd

score_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [65, 86, np.nan, 77],
    'Science': [68, 91, 70, 85]
}

score_df = pd.DataFrame(score_data)
print(score_df)

'''
      Name  Math  Science
0    Alice  65.0       68
1      Bob  86.0       91
2  Charlie   NaN       70
3    David  77.0       85
'''

# 딕셔너리로 데이터프레임 만들기 연습2
date = ['2024-05-11', '2024-05-12', '2024-05-13', '2024-05-14']
stock_data = {'Open': [1320, 1360, 1450, 1430],
              'Close': [1370, 1400, 1510, 1380],
              'Volume': [15234, 17086, 21149, 16396]}

stock_df = pd.DataFrame(stock_data, index=date)
print(stock_df)
'''
            Open  Close  Volume
2024-05-11  1320   1370   15234
2024-05-12  1360   1400   17086
2024-05-13  1450   1510   21149
2024-05-14  1430   1380   16396
'''

stock_df.index.name = '날짜'
stock_df.columns = ['시가', '종가', '거래량']
print(stock_df)
'''
              시가    종가    거래량
날짜                           
2024-05-11  1320  1370  15234
2024-05-12  1360  1400  17086
2024-05-13  1450  1510  21149
2024-05-14  1430  1380  16396
'''

# 리스트로 데이터프레임 만들기 연습
score_data2 = [['Alice', 55, 68], ['Bob', 86, 91],
               ['Charlie', np.nan, 70], ['David', 77, 82]]
score_df2 = pd.DataFrame(score_data2, columns=['Name', 'Math', 'Science'])
print(score_df2)
'''
      Name  Math  Science
0    Alice  55.0       68
1      Bob  86.0       91
2  Charlie   NaN       70
3    David  77.0       82
'''

print(score_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   Name     4 non-null      object 
 1   Math     3 non-null      float64
 2   Science  4 non-null      int64  
dtypes: float64(1), int64(1), object(1)
memory usage: 228.0+ bytes
None
'''

print(stock_df)
'''
              시가    종가    거래량
날짜                           
2024-05-11  1320  1370  15234
2024-05-12  1360  1400  17086
2024-05-13  1450  1510  21149
2024-05-14  1430  1380  16396
'''
# 행 선택 및 조작
print(stock_df.loc['2024-05-12'])
# print(stock_df.iloc[1])
'''
시가      1360
종가      1400
거래량    17086
Name: 2024-05-12, dtype: int64
'''
print(stock_df.loc['2024-05-12': '2024-05-14'])
# print(stock_df.iloc[1:])
# print(stock_df.iloc[1:4])
'''
              시가    종가    거래량
날짜                           
2024-05-12  1360  1400  17086
2024-05-13  1450  1510  21149
2024-05-14  1430  1380  16396
'''

print(stock_df.loc['2024-05-12', '시가'])  # 1360
# print(stock_df.iloc[1, 0])

print(stock_df.loc['2024-05-12': '2024-05-14', ['시가', '거래량']])
# print(stock_df.iloc[1:, [0,2]])
'''
             시가    거래량
날짜                     
2024-05-12  1360  17086
2024-05-13  1450  21149
2024-05-14  1430  16396
'''

stock_df.loc['2024-05-15'] = [1360, 1290, 9783]
print(stock_df)
'''
              시가    종가    거래량
날짜                           
2024-05-11  1320  1370  15234
2024-05-12  1360  1400  17086
2024-05-13  1450  1510  21149
2024-05-14  1430  1380  16396
2024-05-15  1360  1290   9783
'''

stock_df.drop('2024-05-15', axis=0, inplace=True)
print(stock_df)
'''
              시가    종가    거래량
날짜                           
2024-05-11  1320  1370  15234
2024-05-12  1360  1400  17086
2024-05-13  1450  1510  21149
2024-05-14  1430  1380  16396
'''

# 열 선택 및 조작

