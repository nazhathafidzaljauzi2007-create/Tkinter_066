import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x300")
root.configure(padx=20, pady=20)

labeljudul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan")
labeljudul.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(fill="x")
