import matplotlib.pyplot as plt
import numpy as np


# Завдання 1
print("--- Завдання 1 ---")
weeks = ['Тиждень 1', 'Тиждень 2', 'Тиждень 3', 'Тиждень 4']
traffic = [1500, 1600, 1700, 1800]
sales_product_a = [300, 350, 400, 450]
sales_product_b = [200, 250, 300, 350]
sales_product_c = [100, 150, 200, 250]

# Графік трафіку
plt.figure(figsize=(10, 6))
plt.plot(weeks, traffic, label='Трафік', color='blue', linewidth=2)
plt.title('Активність веб-трафіку')
plt.xlabel('Тиждень')
plt.ylabel('Кількість відвідувань')
plt.legend()
plt.grid(True)
plt.savefig('traffic_plot.png')
plt.close()
print("Графік трафіку збережено як traffic_plot.png")

# Графік продажів
plt.figure(figsize=(10, 6))
plt.plot(weeks, sales_product_a, label='Продукт A', color='red', linewidth=2)
plt.plot(weeks, sales_product_b, label='Продукт B', color='green', linewidth=2)
plt.plot(weeks, sales_product_c, label='Продукт C', color='orange', linewidth=2)
plt.title('Продажі трьох продуктів')
plt.xlabel('Тиждень')
plt.ylabel('Кількість продаж')
plt.legend()
plt.grid(True)
plt.savefig('sales_plot.png')
plt.close()
print("Графік продажів збережено як sales_plot.png")


# Завдання 2
print("\n--- Завдання 2 ---")
x = np.linspace(0, 10, 1000)
y = np.sin(x) * np.cos(x)

plt.figure(figsize=(12, 6))
plt.plot(x, y, color='purple', linewidth=1.5)
plt.title('Графік функції y = sin(x) * cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig('function_plot.png')
plt.close()
print("Графік функції збережено як function_plot.png")


# Завдання 3
print("\n--- Завдання 3 ---")
sizes = [50, 25, 15, 10]
labels = ['Продажі', 'Інвестиції', 'Ліцензії', 'Інше']
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Конвори сегментів')
plt.savefig('pie_chart.png')
plt.close()
print("Кругова діаграма збережена як pie_chart.png")
