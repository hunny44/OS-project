import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import time
import backend
# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*"), ("Python Files", "*.py"), ("C Files", "*.c")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Function to simulate a vulnerability scan
def scan_file():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showwarning("Warning", "Please select a file first!")
        return

    # Simulate scanning process
    scan_button.config(state=tk.DISABLED)
    status_label.config(text="Scanning in progress...", foreground="blue")
    root.update_idletasks()
    time.sleep(2)  # Simulating scan delay

    # Simulated scan results
    vulnerabilities = [
        ("Buffer Overflow", "High", "Line 45"),
        ("SQL Injection", "Medium", "Line 112"),
        ("Trapdoor Detected", "Critical", "Line 7")
    ]

    # Clear previous results
    for row in results_table.get_children():
        results_table.delete(row)

    # Insert new results
    for vul in vulnerabilities:
        results_table.insert("", tk.END, values=vul)

    status_label.config(text="Scan Complete! Vulnerabilities Found.", foreground="red")
    scan_button.config(state=tk.NORMAL)

# GUI Setup
root = tk.Tk()
root.title("Security Vulnerability Detection System")
root.geometry("600x400")
root.resizable(False, False)

# File Selection
file_frame = tk.Frame(root)
file_frame.pack(pady=10)
file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side=tk.LEFT, padx=5)
file_button = tk.Button(file_frame, text="Browse", command=select_file)
file_button.pack(side=tk.LEFT)

# Scan Button
scan_button = tk.Button(root, text="Scan File", command=scan_file, font=("Arial", 12), bg="blue", fg="white")
scan_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Select a file to start scanning.", font=("Arial", 10))
status_label.pack()

# Results Table
columns = ("Vulnerability", "Severity", "Location")
results_table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    results_table.heading(col, text=col)
    results_table.column(col, width=150)

results_table.pack(pady=10)

# Run GUI
root.mainloop()
