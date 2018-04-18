def draw_horizontal_line():
    print(" --- " * dim)

def draw_vertical_line():
    print("|    " * (dim+1))

dim = int(input("Dimension: "))

draw_horizontal_line()

for i in range(dim):
    draw_vertical_line()
    draw_horizontal_line()
