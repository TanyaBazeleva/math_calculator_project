import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import json
import xml.etree.ElementTree as ET
from PIL import Image, ImageTk
import os

SERVER_URL = "http://localhost:8000"

# --- Допоміжні функції ---
def clean_html(text):
    import re
    return re.sub(r"<.*?>", "", text)

def clear_result():
    result_text.delete("1.0", tk.END)

# --- Відправка даних на сервер ---
def send_calculate():
    numbers = entry_numbers.get()
    operation = operation_var.get()

    if not numbers:
        messagebox.showwarning("Помилка", "Введіть числа")
        return
    if not operation:
        messagebox.showwarning("Помилка", "Оберіть операцію")
        return

    try:
        task = f"{operation} {numbers}"
        response = requests.post(SERVER_URL + "/calculate", data={"task": task}, timeout=5)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, clean_html(response.text))
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

def send_plot():
    function = entry_function.get()
    if not function:
        messagebox.showwarning("Помилка", "Введіть функцію")
        return
    try:
        response = requests.post(SERVER_URL + "/plot", data={"function": function}, timeout=5)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, clean_html(response.text))

        # Показати графік
        graph_path = os.path.join("data", "graph.png")
        if os.path.exists(graph_path):
            img = Image.open(graph_path)
            img.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(img)
            graph_label.config(image=photo)
            graph_label.image = photo
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

def send_file_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("JSON/XML files", "*.json *.xml")])
    if not file_path:
        return

    try:
        tasks = []
        if file_path.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                tasks = [t["task"] for t in data.get("tasks", [])]

        elif file_path.endswith(".xml"):
            tree = ET.parse(file_path)
            root_element = tree.getroot()
            tasks = [elem.text for elem in root_element.findall("task")]

        result_text.delete("1.0", tk.END)
        for task in tasks:
            response = requests.post(SERVER_URL + "/calculate", data={"task": task}, timeout=5)
            result_text.insert(tk.END, f"{task} -> {clean_html(response.text)}\n")
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

# --- Інтерфейс ---
root = tk.Tk()
root.title("Math Calculator Client")
root.geometry("600x750")
root.configure(bg="#f8f8f8")

style = ttk.Style()
style.configure("TButton", padding=6, font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TNotebook.Tab", font=("Arial", 12))

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# --- Вкладка обчислень ---
frame_calc = ttk.Frame(notebook)
notebook.add(frame_calc, text="Обчислення")

tt_label = ttk.Label(frame_calc, text="Введіть числа через пробіл:")
tt_label.pack(pady=5)
entry_numbers = ttk.Entry(frame_calc, width=50)
entry_numbers.pack(pady=5)

tt_label2 = ttk.Label(frame_calc, text="Оберіть операцію:")
tt_label2.pack(pady=5)
operation_var = tk.StringVar()
operation_menu = ttk.Combobox(frame_calc, textvariable=operation_var, width=30)
operation_menu['values'] = ["add", "subtract", "multiply", "divide", "mean", "median", "mode", "solve_linear", "solve_quadratic"]
operation_menu.pack(pady=5)

tt_btn = ttk.Button(frame_calc, text="Надіслати", command=send_calculate)
tt_btn.pack(pady=10)

# --- Вкладка графіка ---
frame_plot = ttk.Frame(notebook)
notebook.add(frame_plot, text="Графік")

tt_label3 = ttk.Label(frame_plot, text="Функція (наприклад: x**2 + 2*x + 1):")
tt_label3.pack(pady=10)
entry_function = ttk.Entry(frame_plot, width=50)
entry_function.pack(pady=5)

tt_btn2 = ttk.Button(frame_plot, text="Побудувати графік", command=send_plot)
tt_btn2.pack(pady=10)

graph_label = ttk.Label(frame_plot)
graph_label.pack(pady=10)

# --- Вкладка файл ---
frame_file = ttk.Frame(notebook)
notebook.add(frame_file, text="Файл (JSON/XML)")

tt_label4 = ttk.Label(frame_file, text="Виконати завдання з файлу")
tt_label4.pack(pady=10)

tt_btn3 = ttk.Button(frame_file, text="Вибрати файл", command=send_file_tasks)
tt_btn3.pack(pady=10)

# --- Результат ---
tt_label_result = ttk.Label(root, text="Результат:", font=("Arial", 14, "bold"))
tt_label_result.pack(pady=10)

result_text = tk.Text(root, height=12, font=("Arial", 14), bg="#ffffff", relief="solid", borderwidth=1)
result_text.pack(fill="both", expand=True, padx=10, pady=5)

tt_btn_clear = ttk.Button(root, text="Очистити результат", command=clear_result)
tt_btn_clear.pack(pady=10)

root.mainloop()