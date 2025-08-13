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
        The default symbol is 'x'.
    """

    # helpers: coord transforms
    def canvas_to_data(index, data_extent, canvas_length):
        min, max = data_extent
        coef = (max - min) / (canvas_length - 1)
        value = min + coef * (index - 0)
        return value

    def data_to_canvas(value, data_extent, canvas_length):
        min, max = data_extent
        coef = (canvas_length - 1) / (max - min)
        # index is a floating-point number
        index = 0 + coef * (value - min)
        return round(index)

    # canvas
    width, height = canvas_size
    canvas = [list(" ") * width for _ in range(height)]

    # data & indices
    x_index = list(range(width))
    x_data = list(map(lambda index: canvas_to_data(index, xlim, width), x_index))

    y_data = list(map(func, x_data))
    ylim = [min(y_data), max(y_data)]
    y_index = list(map(lambda value: data_to_canvas(value, ylim, height), y_data))

    # drawing (make sure that y-indices are not out of bound)
    indices = ((x, y) for x, y in zip(x_index, y_index) if y >= 0 and y < height)
    for x, y in indices:
        canvas[y][x] = symbol

    return list(reversed(canvas))
