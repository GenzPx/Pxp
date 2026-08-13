"""Modul scraper - ambil judul & meta halaman web (edukasi)."""
import re
import urllib.request


def run():
    print("\n[ SCRAPER ]")
    url = input("Masukkan URL (http/https): ").strip()
    if not url.startswith(("http://", "https://")):
        print("[!] URL harus diawali http:// atau https://")
        return
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
        title = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
        meta = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', html, re.I)
        print(f"  Title      : {title.group(1).strip() if title else '-'}")
        print(f"  Description: {meta.group(1).strip() if meta else '-'}")
        print(f"  Size HTML  : {len(html)} bytes")
    except Exception as e:
        print(f"[!] Error: {e}")
