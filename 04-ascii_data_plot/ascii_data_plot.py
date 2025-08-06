import math
from collections import deque

import numpy as np

h, v = 72, 21  # 가로, 세로
x = list(np.arange(-10, 11, 5))
y = list(np.arange(-1, 1.1, 0.2))

L = [list(" " * h) for i in range(v)]  # h x v 크기의 공백 리스트


def axis(l, gap, scale, size):  # e.g. -10, -5, 0, ... -> gap = 5
    axis = l[:]
    for k in range(size):
        if axis[k] == "+":
            pass
        elif k == 0 or k == size - 1:
            axis[k] = "+"
        elif k % (scale) == 0:
            axis[k] = "+"
        else:
            axis[k] = gap
    return axis


# x축
l = L[0]
xscale = round(h / (len(x) - 1))  # 간격의 개수 = 눈금 숫자 개수-1
x_axis = [axis(l, "-", xscale, h), axis(l, " ", xscale, h)]

L[0:2] = x_axis
L[-1:-3:-1] = x_axis

# y축
T = list([*tup] for tup in zip(*L))  # 전치
yscale = round(v / (len(y) - 1))
y_axis = [axis(T[0], "|", yscale, v), axis(T[1], " ", yscale, v)]

T[0:2] = y_axis
T[-1:-3:-1] = y_axis

# --------------------------------
# y축 눈금
T = deque(T)
index_y = [
    i for i, v in enumerate(T[1]) if v == "+"
]  # 눈금들('+'로 표시된 곳)의 위치 인덱스
dict_y = {
    i: float(round(n, 1)) for i, n in zip(index_y, reversed(y))
}  # 딕셔너리 {인덱스: 눈금 숫자}
# float(round(n,1)): 0.5999999999999996 -> 0.6
a = list(" " * v)
for k in range(len(a)):
    if k in dict_y.keys():
        a[k] = f"{str(dict_y[k]):>4s}" + " "  # 길이 5인 문자열로 통일
    else:
        a[k] = " " * 5
T.appendleft(a)

# x축 눈금
L = list([*tup] for tup in zip(*T))
index_x = [i for i, v in enumerate(L[1]) if v == "+"]
dict_x = {i: int(n) for i, n in zip(index_x, x)}
a = list(" " * (h + 5))
for k in range(len(a)):
    if k in dict_x.keys():
        a[k + 2 : k + 5] = f"{str(dict_x[k]):>3s}"
L.append(a)

# -------------------------------
# 치역 / 각 칸에 해당하는 y값
n = [(k, v) for k, v in dict_y.items()]
Range = {}
for i in range(1, len(n)):
    n_i, n_f = n[i - 1][1], n[i][1]
    i_i, i_f = n[i - 1][0], n[i][0]
    delta_n, delta_i = n_f - n_i, i_f - i_i

    interval = delta_n / delta_i
    ordinate = {float(f"{n_i+(interval*k):.1f}"): i_i + k for k in range(delta_i + 1)}
    Range.update(ordinate)

# 정의역
n = [(k, v) for k, v in dict_x.items()]
domain = {}
for i in range(1, len(n)):
    n_i, n_f = n[i - 1][1], n[i][1]
    i_i, i_f = n[i - 1][0], n[i][0]
    delta_n, delta_i = n_f - n_i, i_f - i_i

    interval = delta_n / delta_i
    abscissa = {n_i + (interval * k): i_i + k for k in range(delta_i + 1)}
    domain.update(abscissa)

# ----------------------------
f = {
    xv: Range[round(math.sin(xk), 1)] for xk, xv in domain.items()
}  # {x인덱스:y인덱스}

for k, v in f.items():
    L[v][k] = "*"

for i in L:
    print("".join(i))
