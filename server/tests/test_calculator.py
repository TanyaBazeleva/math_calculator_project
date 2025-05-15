import unittest
from server.calculator import calculate


class TestCalculator(unittest.TestCase):
    """Тести для функції calculate(): арифметика, рівняння, статистика та обробка помилок"""

    # --- Арифметичні дії ---

    def test_01_add(self):
        """1 - Додавання"""
        self.assertEqual(calculate("add 2 3"), 5)
        self.assertEqual(calculate("add -1 -2"), -3)

    def test_02_subtract(self):
        """2 - Віднімання"""
        self.assertEqual(calculate("subtract 5 3"), 2)

    def test_03_multiply(self):
        """3 - Множення"""
        self.assertEqual(calculate("multiply 3 4"), 12)

    def test_04_divide(self):
        """4 - Ділення"""
        self.assertEqual(calculate("divide 10 2"), 5)

    def test_05_divide_by_zero(self):
        """5 - Ділення на нуль → помилка"""
        with self.assertRaises(ValueError):
            calculate("divide 5 0")

    # --- Рівняння ---

    def test_06_solve_linear_valid(self):
        """6 - Лінійне рівняння: 2x - 4 = 0 → x = 2"""
        self.assertEqual(calculate("solve_linear 2 -4"), 2)

    def test_07_solve_linear_no_solution(self):
        """7 - Лінійне рівняння: 0x + 3 = 0 → помилка"""
        with self.assertRaises(ValueError):
            calculate("solve_linear 0 3")

    def test_08_solve_quadratic_two_roots(self):
        """8 - Квадратне рівняння з двома коренями"""
        self.assertEqual(calculate("solve_quadratic 1 -3 2"), "Два корені: 2.0 і 1.0")

    def test_09_solve_quadratic_one_root(self):
        """9 - Один корінь (дискримінант = 0)"""
        self.assertEqual(calculate("solve_quadratic 1 2 1"), "Один корінь: -1.0")

    def test_10_solve_quadratic_no_roots(self):
        """10 - Немає дійсних коренів"""
        self.assertEqual(calculate("solve_quadratic 1 0 1"), "Немає дійсних коренів")

    # --- Статистика ---

    def test_11_mean(self):
        """11 - Середнє арифметичне"""
        self.assertEqual(calculate("mean 1 2 3 4"), 2.5)

    def test_12_median_odd(self):
        """12 - Медіана непарна кількість"""
        self.assertEqual(calculate("median 1 3 2"), 2)

    def test_13_median_even(self):
        """13 - Медіана парна кількість"""
        self.assertEqual(calculate("median 1 2 3 4"), 2.5)

    def test_14_mode_single(self):
        """14 - Одна мода"""
        self.assertEqual(calculate("mode 5 5 5"), 5.0)

    def test_15_mode_multiple(self):
        """15 - Кілька мод"""
        self.assertEqual(calculate("mode 1 2 2 3 3"), "Кілька мод: 2.0, 3.0")

    # --- Помилки ---

    def test_16_unknown_command(self):
        """16 - Невідома команда → помилка"""
        with self.assertRaises(ValueError):
            calculate("unknown 2 3")

    def test_17_empty_command(self):
        """17 - Порожній рядок → помилка"""
        with self.assertRaises(ValueError):
            calculate("")


if __name__ == "__main__":
    unittest.main(verbosity=2)
