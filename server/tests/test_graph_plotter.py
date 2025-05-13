import unittest  # Модуль для написання автоматичних тестів
import os
import sys

# Додаємо кореневу папку до системного шляху, щоб мати доступ до модуля graph_plotter.py
# (важливо при запуску тестів із окремої папки)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from server.graph_plotter import plot_graph  # Імпортуємо функцію для тестування

class TestGraphPlotter(unittest.TestCase):
    """
    Набір тестів для перевірки функції plot_graph.
    Охоплює: побудову правильних функцій і обробку помилок.
    """

    def test_valid_function(self):
        # Побудова графіка для правильної функції
        filename = plot_graph("x**2 + 2*x + 1")  # Має створити зображення
        self.assertTrue(os.path.exists(os.path.join("data", filename)))

    def test_invalid_function(self):
        # Побудова графіка для некоректного виразу → очікуємо помилку
        with self.assertRaises(ValueError):
            plot_graph("invalid_function(x)")

    def tearDown(self):
        # Після кожного тесту — видаляємо збережене зображення (якщо є)
        filename = os.path.join("data", "graph.png")
        if os.path.exists(filename):
            os.remove(filename)

# Запускаємо тести, якщо файл запускається напряму
if __name__ == "__main__":
    unittest.main(verbosity=2)  # verbose режим — показує повний звіт по кожному тесту
