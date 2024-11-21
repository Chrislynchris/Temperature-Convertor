import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (temp * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (temp - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = temp + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = temp - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (temp - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32

        result_label.config(text=f"Result: {result:.2f} {to_unit}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def reset_fields():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")
    from_unit_var.set("Celsius")
    to_unit_var.set("Fahrenheit")

def create_gui():
    global entry, from_unit_var, to_unit_var, result_label

    # Main window setup
    root = tk.Tk()
    root.title("Advanced Temperature Converter")
    root.geometry("500x400")
    root.resizable(False, False)
    root.configure(bg="#f4f4f4")

    # Title Label
    title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333")
    title_label.pack(pady=20)

    # Frame for Input Fields
    frame = tk.Frame(root, bg="#f4f4f4")
    frame.pack(pady=10)

    # Input Field
    input_label = tk.Label(frame, text="Enter Temperature:", font=("Arial", 12), bg="#f4f4f4")
    input_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry = ttk.Entry(frame, width=20, font=("Arial", 12))
    entry.grid(row=0, column=1, padx=10, pady=5)

    # From Unit Dropdown
    from_unit_var = tk.StringVar(value="Celsius")
    from_label = tk.Label(frame, text="From Unit:", font=("Arial", 12), bg="#f4f4f4")
    from_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    from_unit_menu = ttk.Combobox(frame, textvariable=from_unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
    from_unit_menu.grid(row=1, column=1, padx=10, pady=5)

    # To Unit Dropdown
    to_unit_var = tk.StringVar(value="Fahrenheit")
    to_label = tk.Label(frame, text="To Unit:", font=("Arial", 12), bg="#f4f4f4")
    to_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    to_unit_menu = ttk.Combobox(frame, textvariable=to_unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
    to_unit_menu.grid(row=2, column=1, padx=10, pady=5)

    # Buttons
    button_frame = tk.Frame(root, bg="#f4f4f4")
    button_frame.pack(pady=10)
    convert_button = tk.Button(button_frame, text="Convert", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=convert_temperature)
    convert_button.grid(row=0, column=0, padx=10, pady=10)

    reset_button = tk.Button(button_frame, text="Reset", font=("Arial", 12, "bold"), bg="#F44336", fg="white", command=reset_fields)
    reset_button.grid(row=0, column=1, padx=10, pady=10)

    # Result Label
    result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#333")
    result_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
