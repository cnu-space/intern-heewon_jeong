def ascii_graph_plot(func, xlim, canvas_size=(80, 80), symbol="x"):
    """Return a nested list of characters whose content, when printed,
       depicts the line plot of the provided data.

    :param func:
        A function to be plotted, given as a lambda expression of x.

    :param xlim:
        A pair of minimum and maximum value of x.

    :param canvas_size:
        The canvas size, provided as a pair of the number of rows and columns,
        onto which the data will be drawn.
        The default canvas size is 80 x 80.

    :param symbol:
        The symbol used to mark each data point.
        The default symbol is ‘x’.
    """

    import math

    h, v = canvas_size  # 가로, 세로
    L = [list(" " * h) for i in range(v)]  # h x v 크기의 공백 리스트

    # 정의역
    x_index = [x for x in range(h)]
    x_val = [xlim[0] + ((xlim[1] - xlim[0]) / (h - 1)) * x for x in x_index]

    # 치역
    fx = list(map(func, x_val))  # f(x_val) (i.e. 함숫값) 들의 리스트
    ylim = [min(fx), max(fx)]  # 최대, 최소 함숫값으로 y의 범위 설정하기

    y_index = [y for y in range(v)]
    y_val = [ylim[1] - ((ylim[1] - ylim[0]) / (v - 1)) * y for y in y_index]

    # 그래프 그리기
    coord_x = list(zip(x_index, x_val))
    coord_y = list(zip(y_index, y_val))

    yscale = (ylim[1] - ylim[0]) / (v - 1)
    res = [
        (x_index, y_index)
        for (y_index, y_val) in coord_y
        for (x_index, x_val) in coord_x
        if abs(round(func(x_val) - y_val, 1)) < yscale
    ]

    for x, y in res:  # res: 프레임 안에서 symbol들이 위치할 x, y좌표의 리스트
        L[y][x] = symbol

    return L
