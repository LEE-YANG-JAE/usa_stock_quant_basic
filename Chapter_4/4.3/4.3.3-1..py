import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
x = np.linspace(-3, 3, 60)  # X 축 데이터
y = np.exp(x)  # Y축 데이터

# 그래프 그리기
plt.figure(figsize=(6, 4))  # 크기 설정
plt.plot(x, y)

# 그래프에 제목, 레이블, 그리드 추가
plt.title("Simple Line Plot", fontsize=14)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(alpha=0.3)

# 그래프 표시
plt.show()
