import tkinter as tk

def add_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text="Результат: " + str(result))
root = tk.Tk()
root.title("Калькулятор")
label1 = tk.Label(root, text="Введите первое число:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Введите второе число:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="Сложить", command=add_numbers)
calculate_button.pack()

result_label = tk.Label(root, text="Результат:")
result_label.pack()
root.mainloop()
