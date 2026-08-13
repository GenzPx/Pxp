"""Modul recon - OSINT dasar memakai API publik (edukasi)."""
import json
import urllib.request


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")


def ip_info(ip):
    """Ambil info IP dari ip-api.com (public API)."""
    return json.loads(_get(f"http://ip-api.com/json/{ip}"))


def run():
    print("\n[ RECON & OSINT ]")
    target = input("Masukkan IP / domain: ").strip()
    if not target:
        print("[!] Input kosong.")
        return
    try:
        data = ip_info(target)
        if data.get("status") == "success":
            print(f"  IP       : {data.get('query')}")
            print(f"  ISP      : {data.get('isp')}")
            print(f"  Negara   : {data.get('country')} ({data.get('countryCode')})")
            print(f"  Kota     : {data.get('city')}")
            print(f"  Koordinat: {data.get('lat')}, {data.get('lon')}")
        else:
            print("[!] Gagal mendapatkan info.")
    except Exception as e:
        print(f"[!] Error: {e}")
