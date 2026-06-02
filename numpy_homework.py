import numpy as np

# Завдання 1: Додати число до кінця масиву
print("--- Завдання 1 ---")
array = np.array([12, -5, 7, 9, -3, 15])
array = np.append(array, 10)
print("Масив після додавання числа 10:", array)

# Завдання 2: Видалити другий рядок з двовимірного масиву
print("\n--- Завдання 2 ---")
two_d_array = np.array([
    [5, 2, 8],
    [1, 7, 4],
    [3, 6, 9]
])
print("Оригінальний двовимірний масив:")
print(two_d_array)
two_d_array = np.delete(two_d_array, 1, axis=0)
print("Масив після видалення другого рядка:")
print(two_d_array)

# Завдання 3: Аналіз конверсій
print("\n--- Завдання 3 ---")
conversions = np.array([50, 65, 80, 45, 70, 90, 55, 85, 60, 75])
print("Основний масив конверсій:", conversions)

# Обчислення статистичних показників
median = np.median(conversions)
variance = np.var(conversions)
std_dev = np.std(conversions)
print(f"\nМедіана конверсій: {median}")
print(f"Дисперсія конверсій: {variance}")
print(f"Стандартне відхилення конверсій: {std_dev}")

# Створення чотирьох нових масивів з різними типами випадкових чисел
uniform_arr = np.random.uniform(0, 100, size=10)
int_arr = np.random.randint(0, 100, size=10)
float_arr = np.random.rand(10) * 100
normal_arr = np.random.normal(loc=65, scale=15, size=10)

# Об'єднання з основним масивом
combined_array = np.concatenate((conversions, uniform_arr, int_arr, float_arr, normal_arr))
print("\nОб'єднаний масив:")
print(combined_array)

# Обчислення середнього значення
mean_combined = np.mean(combined_array)
print(f"\nСереднє значення об'єднаного масиву: {mean_combined}")
print(f"Чи більше середнє за 2000? {mean_combined > 2000}")
