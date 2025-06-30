import csv
import tkinter as tk
from tkinter import filedialog


def load_csv(text_widget: tk.Text) -> None:
    """Open a CSV file and display a short preview inside ``text_widget``."""
    file_path = filedialog.askopenfilename(
        title="CSV Seç",
        filetypes=[("CSV files", "*.csv")],
    )
    if not file_path:
        return

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        preview_lines = []
        for i, row in enumerate(reader):
            preview_lines.append(", ".join(row))
            if i == 4:
                break
    preview = "\n".join(preview_lines)

    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, f"Seçilen dosya: {file_path}\nÖn izleme:\n{preview}")
    text_widget.config(state=tk.DISABLED)


def main() -> None:
    """Create the application window."""
    root = tk.Tk()
    root.title("CSV Yükleyici")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    text = tk.Text(frame, width=60, height=10, state=tk.DISABLED)
    text.pack(pady=(10, 0))

    button = tk.Button(frame, text="CSV Dosyası Yükle", command=lambda: load_csv(text))
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
