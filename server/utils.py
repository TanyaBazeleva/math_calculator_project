import json  # Імпортуємо модуль для роботи з JSON-файлами
import xml.etree.ElementTree as ET  # Імпортуємо модуль для роботи з XML
import os  # Імпортуємо модуль для роботи з файлами і папками

# --- Функція збереження даних у форматі JSON ---
def save_json(data, filename):

    # Переконуємося, що папка для файлу існує, якщо ні — створюємо її
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Відкриваємо файл для запису у форматі JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # Зберігаємо дані з красивим форматуванням

# --- Функція завантаження даних з JSON-файлу ---
def load_json(filename):
    # Відкриваємо файл і читаємо JSON-дані
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)  # Повертаємо словник, отриманий із JSON

# --- Функція збереження словника у форматі XML ---
def save_xml(data: dict, filename):

    # Переконуємося, що папка для файлу існує, якщо ні — створюємо її
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Створюємо кореневий елемент <results>
    root = ET.Element("results")

    # Додаємо кожен ключ і його значення як окремий елемент <item>
    for key, value in data.items():
        item = ET.Element("item")  # Створюємо елемент
        item.set("name", key)  # Додаємо атрибут "name" для кожного елемента
        item.text = str(value)  # Встановлюємо значення елемента
        root.append(item)  # Додаємо елемент до кореня

    # Створюємо дерево XML і записуємо його у файл
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

# --- Функція завантаження даних з XML-файлу у словник ---
def load_xml(filename):

    # Читаємо XML-файл і отримуємо кореневий елемент
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    # Проходимо кожен <item> і додаємо його дані до словника
    for item in root.findall("item"):
        result[item.get("name")] = item.text  # Отримуємо атрибут "name" і його значення

    return result  # Повертаємо словник з даними