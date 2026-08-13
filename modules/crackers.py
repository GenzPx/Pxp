"""Modul crackers - identifikasi & uji hash terhadap wordlist (edukasi)."""
import hashlib


def identify(h):
    """Deteksi jenis hash sederhana berdasarkan panjang & charset."""
    if re_fullmatch_hex(h):
        return {
            32: "MD5", 40: "SHA-1", 56: "SHA-224", 64: "SHA-256",
            96: "SHA-384", 128: "SHA-512",
        }.get(len(h), "unknown")
    return "unknown"


def re_fullmatch_hex(h):
    import re
    return bool(re.fullmatch(r"[0-9a-fA-F]+", h))


def crack(target_hash, wordlist_path):
    """Coba cocokkan hash dengan kata-kata di wordlist."""
    algos = {"MD5": hashlib.md5, "SHA-1": hashlib.sha1, "SHA-256": hashlib.sha256,
             "SHA-512": hashlib.sha512}
    kind = identify(target_hash)
    if kind == "unknown" or kind not in algos:
        print(f"[!] Tipe hash tidak didukung/dikenali: {kind}")
        return None
    fn = algos[kind]
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for word in f:
                word = word.strip()
                if fn(word.encode()).hexdigest().lower() == target_hash.lower():
                    return word
    except FileNotFoundError:
        print(f"[!] Wordlist tidak ditemukan: {wordlist_path}")
        return None
    return None


def run():
    print("\n[ CRACKERS ]")
    h = input("Masukkan hash: ").strip()
    wl = input("Path wordlist (default: wordlist.txt): ").strip() or "wordlist.txt"
    print(f"[*] Tipe hash terdeteksi: {identify(h)}")
    res = crack(h, wl)
    print(f"[+] Hasil: {res}" if res else "[-] Tidak ditemukan.")
