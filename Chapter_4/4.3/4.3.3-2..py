import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
x = np.linspace(0.01, 2, 100)  # X 축 데이터
y1 = np.exp(x)
y2 = np.log(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y1, linewidth=1, label='Exp')
plt.plot(x, y2, linewidth=1, label='Log')
plt.axhline(y=0, color='black', linewidth=1)

# 그래프에 제목, 레이블, 그리드 추가
plt.title("Simple Line Plots", fontsize=14)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(alpha=0.3)
plt.legend()  # 범례 표시
plt.show()
