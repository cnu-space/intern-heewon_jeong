import math

from ascii_graph_plot import ascii_graph_plot

# parabola
print("== parabola ==")
graph = ascii_graph_plot(lambda x: x**2, [-2, 2], canvas_size=[40, 20])
for row in graph:
    print("".join(row))
print("\n\n")


# sin(x)
print("== sin(x) ==")
graph = ascii_graph_plot(lambda x: math.sin(x), [-10, 10], canvas_size=[80, 20])
for row in graph:
    print("".join(row))
print("\n\n")
