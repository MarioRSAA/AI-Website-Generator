import tkinter as tk
from Backend import generate_website

root = tk.Tk()
root.title("AI Website Generator")
root.geometry("900x700")
root.resizable(False, False)
root.configure(bg="#0f172a")

title = tk.Label(
    root,
    text="AI Website Generator",
    fg="white",
    bg="#0f172a",
    font=("Segoe UI", 28, "bold")
)
title.pack(pady=(50, 10))

subtitle = tk.Label(
    root,
    text="Describe your website idea",
    fg="#94a3b8",
    bg="#0f172a",
    font=("Segoe UI", 14)
)
subtitle.pack(pady=(0, 30))

text = tk.Text(
    root,
    height=10,
    width=60,
    font=("Segoe UI", 14),
    bg="#020617",
    fg="white",
    insertbackground="white",
    relief="flat",
    padx=15,
    pady=15
)
text.pack(pady=10)

def generate():
    user_input = text.get()
    generate_website(user_input)


button = tk.Button(
    root,
    text="Generate Website",
    command=generate,
    font=("Segoe UI", 14, "bold"),
    fg="white",
    bg="#2563eb",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    width=20,
    height=2
)
button.pack(pady=30)

footer = tk.Label(
    root,
    text="Python • AI • Portfolio Project",
    fg="#64748b",
    bg="#0f172a",
    font=("Segoe UI", 10)
)
footer.pack(side="bottom", pady=10)

root.mainloop()
