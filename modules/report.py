"""Modul report - buat laporan markdown sederhana (edukasi)."""
import json
import os
from datetime import datetime


def generate_report():
    print("\n[ PELAPORAN ]")
    title = input("Judul laporan: ").strip() or "Laporan Pxp"
    body = input("Isi/catatan: ").strip() or "-"
    os.makedirs("reports", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join("reports", f"report_{ts}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"- Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"{body}\n")
    print(f"[+] Laporan tersimpan: {path}")
