import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]
a = [2, 3, 4, 5, 6]
b = [4, 8, 3, 9, 6]

plt.scatter(a, b, label='Titik 1', color='red')
plt.scatter(x, y, label='Titik 2', color='blue')


plt.title('Scatter Plot')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')


plt.legend()
plt.show()
