import os
import json
from modules import auth, recon, pentest, scraper, crackers, bypass, security, update, report

# Load config
with open("config.json", "r") as file:
    config = json.load(file)

def main_menu():
    while True:
        print("\n[1] Recon & OSINT")
        print("[2] Pentest")
        print("[3] Scraper")
        print("[4] Crackers")
        print("[5] Bypass Keamanan")
        print("[6] Pelaporan")
        print("[7] Update Tools")
        print("[8] Keluar")
        
        choice = input("Pilih menu: ")
        
        if choice == "1":
            recon.run()
        elif choice == "2":
            pentest.run()
        elif choice == "3":
            scraper.run()
        elif choice == "4":
            crackers.run()
        elif choice == "5":
            bypass.run()
        elif choice == "6":
            report.generate_report()
        elif choice == "7":
            update.check_update()
        elif choice == "8":
            exit()
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    if auth.login():
        main_menu()