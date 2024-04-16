import matplotlib.pyplot as plt

def f1(x):
    return 3 * x - 5

def f2(x):
    return 45 * x + 1

def f3(x):
    return 98 * x**2 + 30

def f4(x):
    return (8 * x + 3)**0.5

def f5(x):
    return 98 * x**2

def f6(x, z):
    return (3 * x**2 + 3 * z)**0.25

x = range(-10, 11)

y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
y3 = [f3(i) for i in x]
y4 = [f4(i) for i in x]
y5 = [f5(i) for i in x]
y6 = [f6(i, 1) for i in x]  # Aquí se asume que z = 1, puedes cambiarlo según sea necesario

plt.plot(x, y1, label='f1(x) = 3x - 5')
plt.plot(x, y2, label='f2(x) = 45x + 1')
plt.plot(x, y3, label='f3(x) = 98x^2 + 30')
plt.plot(x, y4, label='f4(x) = (8x + 3)^0.5')
plt.plot(x, y5, label='f5(x) = 98x^2')
plt.plot(x, y6, label='f6(x, z) = (3x^2 + 3z)^0.25')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de funciones')
plt.legend()
plt.grid(True)

plt.show()

