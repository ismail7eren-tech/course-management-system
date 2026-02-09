import tkinter as tk
from tkinter import messagebox, simpledialog

class Kurs:
    def __init__(self, kurs_adi, egitmen, icerik):
        self.kurs_adi = kurs_adi
        self.egitmen = egitmen
        self.icerik = icerik
        self.ogrenciler = []

    def kaydol(self, ogrenci):
        self.ogrenciler.append(ogrenci)
        messagebox.showinfo("Başarılı", f"{ogrenci.isim} kursa kaydoldu.")

    def icerik_yukle(self, icerik):
        self.icerik = icerik
        messagebox.showinfo("Başarılı", "İçerik güncellendi.")

class Egitmen:
    def __init__(self, isim, uzmanlik_alanı):
        self.isim = isim
        self.uzmanlik_alanı = uzmanlik_alanı

class Ogrenci:
    def __init__(self, isim, e_posta):
        self.isim = isim
        self.e_posta = e_posta

kurslar = []

def kurs_olustur():
    kurs_adi = entry_kurs.get()
    egitmen_isim = entry_egitmen.get()
    uzmanlik = entry_uzmanlik.get()
    icerik = entry_icerik.get()
    if not kurs_adi or not egitmen_isim or not uzmanlik or not icerik:
        messagebox.showwarning("Uyarı", "Tüm alanları doldurun.")
        return
    egitmen = Egitmen(egitmen_isim, uzmanlik)
    kurs = Kurs(kurs_adi, egitmen, icerik)
    kurslar.append(kurs)
    messagebox.showinfo("Başarılı", "Kurs oluşturuldu.")
    entry_kurs.delete(0, tk.END)
    entry_egitmen.delete(0, tk.END)
    entry_uzmanlik.delete(0, tk.END)
    entry_icerik.delete(0, tk.END)

def kursa_kaydol():
    if not kurslar:
        messagebox.showinfo("Bilgi", "Önce kurs ekleyin.")
        return
    isim = simpledialog.askstring("Öğrenci Adı", "Ad:")
    email = simpledialog.askstring("Öğrenci E-Posta", "E-posta:")
    ogrenci = Ogrenci(isim, email)
    secenekler = "\n".join([f"{i}. {k.kurs_adi}" for i, k in enumerate(kurslar)])
    secim = simpledialog.askinteger("Kurs Seç", f"Kurs numarasını girin:\n{secenekler}")
    if secim is not None and 0 <= secim < len(kurslar):
        kurslar[secim].kaydol(ogrenci)

def icerik_guncelle():
    if not kurslar:
        messagebox.showinfo("Bilgi", "Hiç kurs yok.")
        return
    secenekler = "\n".join([f"{i}. {k.kurs_adi}" for i, k in enumerate(kurslar)])
    secim = simpledialog.askinteger("Kurs Seç", f"Kurs numarasını girin:\n{secenekler}")
    if secim is not None and 0 <= secim < len(kurslar):
        yeni = simpledialog.askstring("Yeni İçerik", "İçeriği girin:")
        if yeni:
            kurslar[secim].icerik_yukle(yeni)

def kurslari_goster():
    listbox.delete(0, tk.END)
    if not kurslar:
        listbox.insert(tk.END, "Hiç kurs yok.")
    for kurs in kurslar:
        listbox.insert(tk.END, f"Kurs: {kurs.kurs_adi} | Eğitmen: {kurs.egitmen.isim} | İçerik: {kurs.icerik}")

# Arayüz
pencere = tk.Tk()
pencere.title("📚 Kurs Yönetim Sistemi")

tk.Label(pencere, text="Kurs Adı").grid(row=0, column=0)
entry_kurs = tk.Entry(pencere)
entry_kurs.grid(row=0, column=1)

tk.Label(pencere, text="Eğitmen Adı").grid(row=1, column=0)
entry_egitmen = tk.Entry(pencere)
entry_egitmen.grid(row=1, column=1)

tk.Label(pencere, text="Uzmanlık Alanı").grid(row=2, column=0)
entry_uzmanlik = tk.Entry(pencere)
entry_uzmanlik.grid(row=2, column=1)

tk.Label(pencere, text="Kurs İçeriği").grid(row=3, column=0)
entry_icerik = tk.Entry(pencere)
entry_icerik.grid(row=3, column=1)

tk.Button(pencere, text="Kurs Oluştur", command=kurs_olustur).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(pencere, text="Kursa Kaydol", command=kursa_kaydol).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(pencere, text="İçerik Güncelle", command=icerik_guncelle).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(pencere, text="Kursları Görüntüle", command=kurslari_goster).grid(row=7, column=0, columnspan=2, pady=5)

listbox = tk.Listbox(pencere, width=80)
listbox.grid(row=8, column=0, columnspan=2, pady=10)

pencere.mainloop()
