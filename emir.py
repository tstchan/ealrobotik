import pyfirmata
import time
kart=pyfirmata.Arduino('COM3')
omuz_motoru=kart.get_pin('d:3:s')
dirsek_motoru=kart.get_pin('d:5:s')
while True:
    girdi_omuz=input("omuz açısı girin")
    sayı_omuz=int(girdi_omuz)
    girdi_dirsek=input("dirsek açısı girin")
    sayı_dirsek=int(girdi_dirsek)
    if sayı_omuz <0 or sayı_omuz>180:
        print("hata")
    else:
        omuz_motoru.write(sayı_omuz)
        print(f"omuz motoru {sayı_omuz} dereceye döndü")
    if sayı_dirsek <0 or sayı_dirsek>180:
        print("hata")
    else:
        dirsek_motoru.write(sayı_dirsek)
        print(f"dirsek motoru {sayı_dirsek} dereceye döndü")
    print("kol hareket ettirildi")
