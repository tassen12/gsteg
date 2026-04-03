import os
import time
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

clear()

# ===== BANNER =====
banner = r"""
________  ________  _________  _______   ________     
│╲   ____╲│╲   ____╲│╲___   ___╲╲  ___ ╲ │╲   ____╲    
╲ ╲  ╲___│╲ ╲  ╲___│╲│___ ╲  ╲_╲ ╲   __╱│╲ ╲  ╲___│    
 ╲ ╲  ╲  __╲ ╲_____  ╲   ╲ ╲  ╲ ╲ ╲  ╲_│╱_╲ ╲  ╲  ___  
  ╲ ╲  ╲│╲  ╲│____│╲  ╲   ╲ ╲  ╲ ╲ ╲  ╲_│╲ ╲ ╲  ╲│╲  ╲ 
   ╲ ╲_______╲____╲_╲  ╲   ╲ ╲__╲ ╲ ╲_______╲ ╲_______╲
    ╲│_______│╲_________╲   ╲│__│  ╲│_______│╲│_______│
             ╲│_________│                              
"""

print(banner)

# ===== LOADING =====
print("\n[+] Initializing system", end="", flush=True)
for _ in range(6):
    time.sleep(0.3)
    print(".", end="", flush=True)

time.sleep(0.5)
clear()

# ===== TITLE =====
stagehide = r"""
   _____ _             _     _     _          
  / ____| |           (_)   | |   (_)        
 | (___ | |_ _   _  __ _  __| |    _  ___  ___   
  \___ \| __| | | |/ _` |/ _` |   | |/ _ \/ _ \  
  ____) | |_| |_| | (_| | (_| |_  | | (_) (_) |  
 |_____/ \__|\__,_|\__,_|\__,_(_) |_|\___/\___/  
================================================
"""

print(stagehide)

type_text("[ STEGHIDE ENCODER v1.0 ]", 0.03)
print()

# ===== MENU =====
type_text("[1] Enter secret file", 0.02)
time.sleep(0.5)
secret = input(">> File to hide: ")

type_text("\n[2] Select cover image", 0.02)
time.sleep(0.5)
image = input(">> Image file: ")

type_text("\n[3] Encoding...", 0.03)
time.sleep(1)

# ===== EXECUTE =====
command = f'steghide embed -ef "{secret}" -cf "{image}" -p ""'
os.system(command)

# ===== DONE =====
print("\n[✓] Done!")
type_text("Your data has been hidden successfully.", 0.02)
