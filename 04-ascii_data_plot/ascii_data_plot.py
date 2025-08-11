def ascii_data_plot(x_data, y_data, symbol="x", canvas_size=(80, 80)):

    import math

    h, v = canvas_size  # 가로, 세로

    L = [list(" " * h) for i in range(v)]  # h x v 크기의 공백 리스트

    coord_x = [(x, -10 + (20 / (h - 1)) * x) for x in range(h)]  # [(step: value)]
    coord_y = [(y, 1 - (2 / (v - 1)) * y) for y in range(v)]

    xticks = {}
    yticks = {}

    for data in x_data:
        diff = {
            abs(value - data): step for step, value in coord_x
        }  # diff = {눈금과 값 차이: step}
        xticks.update({data: diff[min(diff)]})  # min(dictionary) - 최소인 key 반환

    for data in y_data:
        diff = {abs(value - data): step for step, value in coord_y}
        yticks.update({data: diff[min(diff)]})

    x_axis = [
        ["+" if k in xticks.values() else "-" for k in range(h)],
        ["+" if k in xticks.values() else " " for k in range(h)],
    ]

    y_axis = [
        ["+" if k in yticks.values() else "|" for k in range(v)],
        ["+" if k in yticks.values() else " " for k in range(v)],
    ]

    L[0:2] = x_axis
    L[-1:-3:-1] = x_axis

    T = list([*tup] for tup in zip(*L))

    T[0:2] = y_axis
    T[-1:-3:-1] = y_axis

    L = list([*tup] for tup in zip(*T))

    # ---------------------------------------
    # 그래프 그리기

    res = [
        (x, y)
        for (y, y_val) in coord_y
        for (x, x_val) in coord_x
        if abs(round(math.sin(x_val) - y_val, 1)) < 0.1
    ]

    for x, y in res:
        L[y][x] = symbol

    return L
