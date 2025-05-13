from wsgiref.simple_server import make_server  # Імпортуємо сервер для обробки запитів
import cgi  # Модуль для роботи з веб-формами
import os  # Модуль для роботи з файлами і папками
from calculator import calculate  # Імпортуємо функцію для обчислення виразів
from graph_plotter import plot_graph  # Імпортуємо функцію для побудови графіків

# Переконуємося, що папка data існує (тут зберігатимуться графіки)
os.makedirs("data", exist_ok=True)

# Головна функція додатка
def app(environ, start_response):
    path = environ.get("PATH_INFO", "").lstrip("/")  # Отримуємо шлях до запиту
    method = environ.get("REQUEST_METHOD", "GET")  # Отримуємо метод HTTP (GET або POST)
    status = "200 OK"  # Початковий статус відповіді
    headers = [("Content-type", "text/html; charset=utf-8")]  # Встановлюємо заголовки відповіді
    body = ""  # Змінна для збереження HTML-коду відповіді

    # --- Головна сторінка ---
    if path == "":
        try:
            with open("index.html", encoding="utf-8") as f:
                body = f.read()  # Зчитуємо файл головної сторінки
        except FileNotFoundError:
            status = "404 NOT FOUND"  # Якщо файл не знайдено, змінюємо статус
            body = "<h1>Файл index.html не знайдено.</h1>"

    # Обробка запиту на обчислення
    elif path == "calculate" and method == "POST":
        form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)  # Отримуємо дані з форми
        task = form.getfirst("task", "")  # Беремо вираз для обчислення
        if task:
            try:
                result = calculate(task)  # Викликаємо функцію обчислення
                body = f"<h2>Результат: {result}</h2><a href='/'>Назад</a>"  # Виводимо результат
            except Exception as e:
                body = f"<h2>Помилка: {str(e)}</h2><a href='/'>Назад</a>"  # Виводимо повідомлення про помилку
        else:
            body = "<h2>Помилка: Завдання порожнє.</h2><a href='/'>Назад</a>"

    # Обробка запиту на побудову графіка
    elif path == "plot" and method == "POST":
        form = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)  # Отримуємо дані з форми
        function = form.getfirst("function", "")  # Беремо функцію для побудови графіка
        if function:
            try:
                filename = plot_graph(function)  # Викликаємо функцію побудови графіка
                image_url = f"/data/{filename}"  # Формуємо шлях до збереженого графіка
                body = f"<h2>Графік побудовано:</h2><img src='{image_url}' width='400'><br><a href='/'>Назад</a>"
            except Exception as e:
                body = f"<h2>Помилка: {str(e)}</h2><a href='/'>Назад</a>"
        else:
            body = "<h2>Помилка: Введіть функцію.</h2><a href='/'>Назад</a>"

    # Відображення збережених графіків
    elif path.startswith("data/"):
        file_path = os.path.join("data", path.replace("data/", ""))  # Формуємо шлях до файлу
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                start_response("200 OK", [("Content-type", "image/png")])  # Встановлюємо заголовки для зображення
                return [f.read()]  # Відправляємо файл у відповідь
        else:
            status = "404 NOT FOUND"
            body = "<h1>Файл графіка не знайдено</h1>"

    # Обробка невідомих маршрутів
    else:
        status = "404 NOT FOUND"
        body = "<h1>Помилка 404: Сторінку не знайдено</h1>"

    # Відправляємо відповідь клієнту
    start_response(status, headers)
    return [body.encode("utf-8")]

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8000
    print("=== Math Calculator API Server is running ===")
    with make_server(HOST, PORT, app) as server:
        print(f"Server is available at http://{HOST}:{PORT}")
        server.serve_forever()