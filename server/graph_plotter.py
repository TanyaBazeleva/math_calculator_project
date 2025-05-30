import matplotlib.pyplot as plt  # Імпортуємо бібліотеку для побудови графіків
import numpy as np  # Імпортуємо бібліотеку для роботи з числовими масивами
import os  # Імпортуємо модуль для роботи з файлами і папками

def plot_graph(function_string):
    """
    Будує графік функції y = f(x), де f(x) задається як вираз (наприклад "x**2 + 2*x + 1").
    Зберігає графік як PNG і повертає ім'я файлу.
    """

    # Готуємо значення x від -10 до 10 з 400 точками для плавного графіка
    x = np.linspace(-10, 10, 400)

    # Перетворюємо текстовий вираз у математичну функцію
    try:
        # Використовуємо eval, обмежуючи доступ до небезпечних функцій
        y = eval(function_string, {"x": x, "np": np, "__builtins__": {}})
    except Exception as e:
        raise ValueError(f"Помилка у функції: {str(e)}")  # Якщо помилка, повідомляємо користувача

    # --- Побудова графіка ---
    plt.figure()  # Створюємо новий графік
    plt.plot(x, y, label=f"y = {function_string}")  # Малюємо графік
    plt.xlabel("x")  # Підпис осі X
    plt.ylabel("y")  # Підпис осі Y
    plt.title("Графік функції")  # Заголовок графіка
    plt.legend()  # Відображаємо легенду
    plt.grid(True)  # Додаємо сітку для зручності читання

    # Збереження графіка
    filename = "graph.png"  # Ім'я файлу для збереження
    save_path = os.path.join("data", filename)  # Формуємо шлях до файлу

    # Переконуємося, що папка 'data' існує, якщо ні — створюємо
    os.makedirs("data", exist_ok=True)

    plt.savefig(save_path)  # Зберігаємо графік у файл
    plt.close()  # Закриваємо графік, щоб звільнити пам'ять

    return filename  # Повертаємо ім'я створеного файлу

# Приклад запуску для перевірки
if __name__ == "__main__":
    f = input("Введіть функцію (наприклад x**2 + 2*x + 1): ")  # Запитуємо функцію у користувача
    name = plot_graph(f)  # Побудова графіка
    print(f"Графік збережено у {name}")  # Виводимо інформацію про збережений файл