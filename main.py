#Variabel input
import random
from libs import welcome_mesage


position = random.randint(1,5)

welcome_mesage("PAY TO GAMES")


user = input("Masukan Nama: ")

while user == "":
   user = input("isi lah masak gak di isi namanya: ")

bentuk_goa = "|_|"
goa_kosong =[bentuk_goa] * 5

goa = goa_kosong.copy()
goa[position - 1] = "|o.o|"

goa_kosong = ' '.join(goa_kosong)
goa = ' '.join(goa)


print(f'''
halo {user}! Coba perhatikan goa dibawah ini 
{goa_kosong}
''')

pilihan_user = int(input("Menurut kamu di goa nomer berapa? [1 / 2 / 3 / 4 / 5]:"))

confirm_answar = input(f"Yakin jawabanya ini {pilihan_user}? [y/n]: ")

if confirm_answar == "n":
    print("program dihentikan! ")
    exit()
elif confirm_answar == "y":
    if pilihan_user == position:
     print(f"{goa}, Good Kamu Menang! ")
    else:
     print(f"{goa}, Tolol Kamu Kalah HAHAHAHAHA")
else:
   print("Silakan ulangi programnya!")
   exit()