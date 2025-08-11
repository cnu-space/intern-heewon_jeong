from ascii_data_plot import ascii_data_plot

x_data = [-10 + ((10 - (-10)) / 4) * n for n in range(5)]
y_data = [float(f"{-1 + (((1 - (-1)) / 10 ) * n) :.1f}") for n in range(11)]

result = ascii_data_plot(x_data, y_data, symbol="*", canvas_size=(72, 21))

for i in result:
    print("".join(i))
