import unittest
import os
from server.utils import save_json, load_json, save_xml, load_xml

#Тести для функцій збереження та завантаження JSON/XML
class TestUtils(unittest.TestCase):
    def test_1_json_save_load(self):
        """1 - Збереження і завантаження JSON"""
        data = {"a": 1, "b": 2}
        filename = "data/test_result.json"
        save_json(data, filename)
        result = load_json(filename)
        self.assertEqual(result, data)

    def test_2_xml_save_load(self):
        """2 - Збереження і завантаження XML"""
        data = {"x": "10", "y": "20"}
        filename = "data/test_result.xml"
        save_xml(data, filename)
        result = load_xml(filename)
        self.assertEqual(result, data)

    def test_3_empty_json(self):
        """3 - Порожній словник у JSON"""
        data = {}
        filename = "data/test_empty.json"
        save_json(data, filename)
        result = load_json(filename)
        self.assertEqual(result, data)

    def test_4_empty_xml(self):
        """4 - Порожній словник у XML"""
        data = {}
        filename = "data/test_empty.xml"
        save_xml(data, filename)
        result = load_xml(filename)
        self.assertEqual(result, data)

    def tearDown(self):
        """Видалення тимчасових файлів після тестів"""
        for filename in [
            "data/test_result.json",
            "data/test_result.xml",
            "data/test_empty.json",
            "data/test_empty.xml"
        ]:
            if os.path.exists(filename):
                os.remove(filename)

if __name__ == "__main__":
    unittest.main()
