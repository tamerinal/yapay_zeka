import csv
import tkinter as tk
from tkinter import filedialog

def load_csv():
    file_path = filedialog.askopenfilename(
        title="CSV Seç",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            preview_lines = []
            for i, row in enumerate(reader):
                preview_lines.append(", ".join(row))
                if i == 4:
                    break
            preview = "\n".join(preview_lines)
        text.config(state=tk.NORMAL)
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"Se\u00e7ilen dosya: {file_path}\n\u00d6n izleme:\n{preview}")
        text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("CSV Y\u00fckleyici")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

button = tk.Button(frame, text="CSV Dosyas\u0131 Y\u00fckle", command=load_csv)
button.pack()

text = tk.Text(frame, width=60, height=10, state=tk.DISABLED)
text.pack(pady=(10, 0))

root.mainloop()
