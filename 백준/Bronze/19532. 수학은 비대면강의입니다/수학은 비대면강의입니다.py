a, b, c, d, e, f = map(int, input().split())

up_x_hang = a * e
up_val = c * e

down_x_hang = d * b
down_val = f * b

X = (up_val - down_val) // (up_x_hang - down_x_hang)
Y = (a * f - c * d) // (up_x_hang - down_x_hang)
print(X, Y)