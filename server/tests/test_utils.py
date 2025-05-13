import unittest  # Модуль для написання автоматичних тестів
import os
import sys

# Додаємо кореневу папку до системного шляху, щоб мати доступ до модуля utils.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from server.utils import save_json, load_json, save_xml, load_xml  # Імпортуємо функції для тестування

class TestUtils(unittest.TestCase):
    """
    Набір тестів для перевірки функцій збереження та завантаження JSON/XML.
    """

    def test_save_and_load_json(self):
        # Тестуємо збереження і завантаження JSON-файлу з даними
        data = {"a": 1, "b": 2}
        filename = "data/test_result.json"
        save_json(data, filename)
        result = load_json(filename)
        self.assertEqual(result, data)

    def test_save_and_load_xml(self):
        # Тестуємо збереження і завантаження XML-файлу з даними
        data = {"x": "10", "y": "20"}
        filename = "data/test_result.xml"
        save_xml(data, filename)
        result = load_xml(filename)
        self.assertEqual(result, data)

    def test_empty_json(self):
        # Тестуємо збереження і завантаження порожнього JSON
        data = {}
        filename = "data/test_empty.json"
        save_json(data, filename)
        result = load_json(filename)
        self.assertEqual(result, data)

    def test_empty_xml(self):
        # Тестуємо збереження і завантаження порожнього XML
        data = {}
        filename = "data/test_empty.xml"
        save_xml(data, filename)
        result = load_xml(filename)
        self.assertEqual(result, data)

    def tearDown(self):
        # Видаляємо всі створені тестові файли після кожного тесту
        files = [
            "data/test_result.json",
            "data/test_result.xml",
            "data/test_empty.json",
            "data/test_empty.xml"
        ]
        for file in files:
            if os.path.exists(file):
                os.remove(file)

# Запускаємо тести, якщо файл запускається напряму
if __name__ == "__main__":
    unittest.main(verbosity=2)  # verbose режим — показує повний звіт по кожному тесту
