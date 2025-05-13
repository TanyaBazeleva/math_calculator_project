import statistics  # Імпортуємо модуль для статистичних операцій
from collections import Counter  # Імпортуємо Counter для знаходження моди

def calculate(task):
    parts = task.strip().split()  # Розбиваємо введене завдання на частини
    if not parts:
        raise ValueError("Порожнє завдання")  # Перевіряємо, чи є вхідні дані

    command = parts[0]  # Перше слово — це команда
    args = list(map(float, parts[1:]))  # Перетворюємо всі інші частини в числа

    # --- Операції з двома числами ---
    if command == "add" and len(args) == 2:
        return args[0] + args[1]  # Додавання

    elif command == "subtract" and len(args) == 2:
        return args[0] - args[1]  # Віднімання

    elif command == "multiply" and len(args) == 2:
        return args[0] * args[1]  # Множення

    elif command == "divide" and len(args) == 2:
        if args[1] == 0:
            raise ValueError("Ділення на нуль")  # Перевіряємо, щоб не ділити на нуль
        return args[0] / args[1]  # Ділення

    # --- Розв'язання лінійного рівняння ax + b = 0 ---
    elif command == "solve_linear" and len(args) == 2:
        a, b = args
        if a == 0:
            raise ValueError("Рівняння не має розв'язків")  # Якщо a = 0, рівняння немає розв’язку
        return -b / a  # Знаходимо корінь рівняння

    # --- Розв'язання квадратного рівняння ax^2 + bx + c = 0 ---
    elif command == "solve_quadratic" and len(args) == 3:
        a, b, c = args
        d = b ** 2 - 4 * a * c  # Обчислюємо дискримінант
        if d < 0:
            return "Немає дійсних коренів"  # Якщо дискримінант < 0, коренів немає
        elif d == 0:
            return f"Один корінь: {-b / (2 * a)}"  # Якщо дискримінант = 0, один корінь
        else:
            x1 = (-b + d ** 0.5) / (2 * a)  # Перший корінь
            x2 = (-b - d ** 0.5) / (2 * a)  # Другий корінь
            return f"Два корені: {x1} і {x2}"  # Якщо дискримінант > 0, два корені

    # --- СТАТИСТИКА ---

    # Обчислення середнього арифметичного значення
    elif command == "mean" and len(args) > 0:
        return statistics.mean(args)

    # Обчислення медіани
    elif command == "median" and len(args) > 0:
        return statistics.median(args)

    # Знаходження моди
    elif command == "mode" and len(args) > 0:
        counter = Counter(args)  # Рахуємо кількість кожного елемента
        max_count = max(counter.values())  # Визначаємо найбільшу частоту появи
        modes = [value for value, count in counter.items() if count == max_count]  # Визначаємо моду
        if len(modes) == 1:
            return modes[0]  # Якщо мода одна, повертаємо її
        else:
            return f"Кілька мод: {', '.join(map(str, modes))}"  # Якщо мод кілька, виводимо всі
    else:
        raise ValueError("Невідома команда або неправильна кількість аргументів")  # Обробка помилок