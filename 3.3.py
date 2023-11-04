#Soal praktikum informatika no 1
#import module random dari python standar library
import random, sys

#opening menu awal
print("""\033[32m
.:: Permainan Suit/Pingsut ::.
-> Player vs Computer
\033[0;0m
Jempol (Gajah)      🐘 #1
Telunjuk (Manusia)  🥷  #2
Kelingking (Semut)  🐜 #3
""")

#variabel karakter yang dipilih player & Keadaan jika Player salah pilih
try:
    pil = int(input("\033[32m.:: Choose Your Character ::.\n        #"))
    if(pil < 1 or pil > 3):
        raise ValueError
except ValueError:
    sys.exit("\033[31mKarakter belum rilis. Masukkan pilihan antara 1 - 3.")

#variabel komputer memilih secara acak
kom = (random.randint(1,3))

#kamus untuk berbagai kemungkinan antara player & komputer
variable_dict = {
    "1"  : "🐘",
    "2"  : "🥷 ",
    "3"  : "🐜",
    "11" : "Sama-sama Gajah! sesama gajah saling membantu...🤝",
    "12" : "🐘🏆\nKamu abis nginjek manusia, kamu\033[33m menang!🎉",
    "13" : "🐜🏆\nKamu abis dikerjain sama semut, kamu\033[31m kalah!💔",
    "21" : "🐘🏆\nDiinjek gajah.. kamu\033[31m kalah!💔",
    "22" : "Sama-sama Manusia! Jangan berantem woiii...🤝",
    "23" : "🥷🏆\nKamu gak sengaja injek semut, kamu\033[33m menang!🎉",
    "31" : "🐜🏆\nKamu gigit gajah, kamu\033[33m menang!🎉",
    "32" : "🥷🏆\nKamu dibunuh manusia, kamu\033[31m kalah!💔",
    "33" : "Sesama semut harus saling membahu..🤝!",
}
 
#print hasil
print("\033[0m.::",variable_dict.get(f"{pil}")," vs ",variable_dict.get(f"{kom}"),"::.\n")
output = (f"{pil}{kom}")
print("\n\033[0m",variable_dict.get(output),"\n\033[0m")
