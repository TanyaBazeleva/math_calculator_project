import unittest  # Модуль для написання автоматичних тестів
import sys
import os

# Додаємо кореневу папку до системного шляху, щоб мати доступ до модуля calculator.py
# (важливо при запуску тестів із окремої папки)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from server.calculator import calculate  # Імпортуємо функцію для тестування

class TestCalculator(unittest.TestCase):
    """
    Набір тестів для перевірки функції calculate.
    Охоплює: арифметичні дії, рівняння, статистику та помилки.
    """

    # --- Арифметика ---

    def test_add(self):
        # Перевіряємо додавання
        self.assertEqual(calculate("add 2 3"), 5)
        self.assertEqual(calculate("add -1 -2"), -3)

    def test_subtract(self):
        # Перевіряємо віднімання
        self.assertEqual(calculate("subtract 5 3"), 2)

    def test_multiply(self):
        # Перевіряємо множення
        self.assertEqual(calculate("multiply 3 4"), 12)

    def test_divide(self):
        # Перевіряємо ділення
        self.assertEqual(calculate("divide 10 2"), 5)
        # Перевіряємо ділення на 0 (повинна бути помилка)
        with self.assertRaises(ValueError):
            calculate("divide 5 0")

    # --- Рівняння ---

    def test_solve_linear(self):
        # Лінійне рівняння: 2x + (-4) = 0 → x = 2
        self.assertEqual(calculate("solve_linear 2 -4"), 2)
        # Якщо коефіцієнт a = 0 → немає розв'язку
        with self.assertRaises(ValueError):
            calculate("solve_linear 0 3")

    def test_solve_quadratic(self):
        # Квадратне рівняння з двома коренями
        self.assertEqual(calculate("solve_quadratic 1 -3 2"), "Два корені: 2.0 і 1.0")
        # Один корінь (дискримінант = 0)
        self.assertEqual(calculate("solve_quadratic 1 2 1"), "Один корінь: -1.0")
        # Немає дійсних коренів (дискримінант < 0)
        self.assertEqual(calculate("solve_quadratic 1 0 1"), "Немає дійсних коренів")

    # --- Статистика ---

    def test_mean(self):
        # Середнє арифметичне
        self.assertEqual(calculate("mean 1 2 3 4"), 2.5)

    def test_median(self):
        # Непарна кількість елементів
        self.assertEqual(calculate("median 1 3 2"), 2)
        # Парна кількість елементів
        self.assertEqual(calculate("median 1 2 3 4"), 2.5)

    def test_mode(self):
        # Одна мода — повертається число
        self.assertEqual(calculate("mode 1 1 2 3 3 3"), 3.0)
        self.assertEqual(calculate("mode 5 5 5"), 5.0)

        # Кілька мод — повертається рядок зі списком
        self.assertEqual(calculate("mode 1 2 2 3 3"), "Кілька мод: 2.0, 3.0")

    # --- Обробка помилок ---

    def test_unknown_command(self):
        # Невідома команда → очікуємо помилку
        with self.assertRaises(ValueError):
            calculate("unknown 2 3")

    def test_empty_task(self):
        # Порожній рядок → помилка
        with self.assertRaises(ValueError):
            calculate("")

# Запускаємо тести, якщо файл запускається напряму
if __name__ == "__main__":
    unittest.main(verbosity=2)  # verbose режим — показує повний звіт по кожному тесту