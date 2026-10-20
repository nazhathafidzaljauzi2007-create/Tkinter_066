import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x700")
root.configure(padx=20, pady=20)

labeljudul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan")
labeljudul.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(fill="x")

Listmapel = [f"Mata Pelajaran {i+1}" for i in range(10)]
entries = []

for i, mapel in enumerate(Listmapel):
    lbl = tk.Label(frame_input, text=f"Nilai {mapel}:", anchor="w")
    lbl.grid(row=i, column=0, sticky="w", pady=2)
    
    entry = tk.Entry(frame_input, width=15)
    entry.grid(row=i, column=1, padx=10, pady=2)
    entries.append(entry)

frame_prodi = tk.Frame(root)
frame_prodi.pack(fill="x", pady=15)

lbl_prodi = tk.Label(frame_prodi, text="Pilih Prodi / Jurusan:", anchor="w")
lbl_prodi.pack(anchor="w")

daftar_prodi = [
    "Teknik Mesin", "Teknik Sipil", "Teknologi Informasi", 
    "Artificial Intelligence", "Elektro Medis", "Teknik Elektro"
]

combo_prodi = ttk.Combobox(frame_prodi, values=daftar_prodi, state="readonly")
combo_prodi.pack(fill="x", pady=5)
combo_prodi.current(2)

def PrediksiProdi():
    prodi_terpilih = combo_prodi.get()
    labelhasil.config(text=f"Hasil Prediksi: {prodi_terpilih}", fg="green")

btnPrediksi = tk.Button(
    root, 
    text="Hasil Prediksi", 
    command=PrediksiProdi,
    bg="#4CAF50", 
    fg="white", 
    pady=5
)
btnPrediksi.pack(pady=10)

labelhasil = tk.Label(
    root, 
    text="Hasil Prediksi: -"
)
labelhasil.pack()

root.mainloop()