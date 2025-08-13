from ascii_graph_plot import ascii_graph_plot

graph = ascii_graph_plot(lambda x: x**2, [-2, 2], canvas_size=[60, 20])

for row in graph:
    print("".join(row))
