import tkinter as tk
import math

# Fungsi untuk menambah nombor atau simbol ke dalam paparan
def click(button_value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + button_value)

# Fungsi untuk membersihkan paparan
def clear():
    display.delete(0, tk.END)

# Fungsi untuk mengira hasil
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Fungsi untuk mengira punca kuasa dua
def square_root():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Fungsi untuk mengira kuasa dua
def square():
    try:
        result = float(display.get()) ** 2
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Fungsi untuk mengira peratusan
def percentage():
    try:
        result = float(display.get()) / 100
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Fungsi untuk memadam satu karakter dari belakang
def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Membuat tetingkap utama
root = tk.Tk()
root.title("Calculator")

# Paparan kalkulator
display = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
display.grid(row=0, column=0, columnspan=4)

# Butang nombor dan operasi
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Membuat butang dan menambah ke dalam tetingkap
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Butang tambahan
clear_button = tk.Button(root, text='C', width=5, height=2, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

exit_button = tk.Button(root, text='Exit', width=5, height=2, font=("Arial", 18), command=root.quit)
exit_button.grid(row=5, column=1, padx=5, pady=5)

sqrt_button = tk.Button(root, text='√', width=5, height=2, font=("Arial", 18), command=square_root)
sqrt_button.grid(row=5, column=2, padx=5, pady=5)

square_button = tk.Button(root, text='x²', width=5, height=2, font=("Arial", 18), command=square)
square_button.grid(row=5, column=3, padx=5, pady=5)

percent_button = tk.Button(root, text='%', width=5, height=2, font=("Arial", 18), command=percentage)
percent_button.grid(row=6, column=0, padx=5, pady=5)

backspace_button = tk.Button(root, text='⌫', width=5, height=2, font=("Arial", 18), command=backspace)
backspace_button.grid(row=6, column=1, padx=5, pady=5)

# Menjalankan tetingkap utama
root.mainloop()
