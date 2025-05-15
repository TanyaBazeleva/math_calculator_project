import unittest
import os
from server.graph_plotter import plot_graph


class TestPlotGraph(unittest.TestCase):
    def test_1_valid_function(self):
        """1 - Коректний вираз → файл має зберегтись"""
        filename = plot_graph("x**2 + 2*x + 1")
        path = os.path.join("data", filename)
        self.assertTrue(os.path.exists(path), f"Графік {filename} не знайдено")

    def test_2_invalid_function(self):
        """2 - Некоректний вираз → має бути ValueError"""
        with self.assertRaises(ValueError):
            plot_graph("invalid_function(x)")

    def tearDown(self):
        """Після кожного тесту — видалення графіка"""
        path = os.path.join("data", "graph.png")
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
