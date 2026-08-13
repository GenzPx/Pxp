"""Modul security - cek kekuatan password & bantu hash (edukasi/defensif)."""
import hashlib
import re


def password_strength(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if len(pw) >= 12:
        score += 1
    if re.search(r"[a-z]", pw) and re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"\d", pw):
        score += 1
    if re.search(r"[^a-zA-Z0-9]", pw):
        score += 1
    labels = ["Sangat Lemah", "Lemah", "Sedang", "Kuat", "Sangat Kuat"]
    return labels[min(score, len(labels) - 1)]


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def run():
    print("\n[ SECURITY TOOLS ]")
    print("1) Cek kekuatan password")
    print("2) Hash SHA-256")
    c = input("Pilih: ").strip()
    if c == "1":
        pw = input("Masukkan password: ")
        print(f"[*] Kekuatan: {password_strength(pw)}")
    elif c == "2":
        t = input("Masukkan teks: ")
        print(f"[*] SHA-256: {sha256(t)}")
    else:
        print("[!] Pilihan tidak valid.")
