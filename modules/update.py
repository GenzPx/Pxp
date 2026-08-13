"""Modul update - cek versi terbaru dari GitHub (edukasi)."""
import json
import urllib.request

REPO = "GenzPx/Pxp"


def check_update():
    print("\n[ UPDATE TOOLS ]")
    try:
        req = urllib.request.Request(
            f"https://api.github.com/repos/{REPO}/releases/latest",
            headers={"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github+json"},
        )
        data = json.load(urllib.request.urlopen(req, timeout=15))
        print(f"[+] Versi terbaru: {data.get('tag_name', '-')}")
        print(f"    {data.get('name', '')}")
        print(f"    {data.get('html_url', '')}")
    except Exception as e:
        print(f"[!] Gagal cek update: {e}")
