"""Modul auth - gerbang akses CLI (edukasi)."""
import getpass


def login():
    """Konfirmasi penggunaan yang sah sebelum masuk menu utama."""
    print("\n=====================================")
    print("  PXP TOOLKIT - DISCLAIMER")
    print("=====================================")
    print("Tool ini hanya untuk EDUKASI dan pengujian")
    print("keamanan yang DIIZINKAN (authorized testing).")
    print("Penggunaan tanpa izin adalah ilegal.")
    print("=====================================")
    ans = input("\nLanjut dengan tanggung jawab sendiri? (y/n): ").strip().lower()
    return ans == "y"
