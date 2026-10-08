import pyfirmata
import time
kart=pyfirmata.Arduino('COM3')
omuz_motoru=kart.get_pin('d:3:s')
dirsek_motoru=kart.get_pin('d:5:s')
guncel_omuz=0
guncel_dirsek=0
HIZ=0.02
while True:
    try:
        secim=input("hizi değiştirmek ister misiniz? (e/h): ")
        if secim == "e":
            girdi_hiz=input("hizi giriniz")
            HIZ=float(girdi_hiz)
        girdi_omuz=input("omuz açisini giriniz")
        sayi_omuz=int(girdi_omuz)
        girdi_dirsek=input("dirsek açisini giriniz")
        sayi_dirsek=int(girdi_dirsek)
    except ValueError:
        print("lütfen sayi gir")
        continue
    if sayi_omuz <0 or sayi_omuz>180:
        print("hata")
        continue
    else:
        if sayi_omuz > guncel_omuz:
            adim=1
        else:
            adim=-1
        for aci in range(guncel_omuz, sayi_omuz + adim, adim):
            omuz_motoru.write(aci)
            time.sleep(HIZ)
        guncel_omuz=sayi_omuz
        print(f"omuz motoru {sayi_omuz} dereceye döndü")
    if sayi_dirsek <0 or sayi_dirsek>180:
        print("hata")
        continue
    else:
        if sayi_dirsek > guncel_dirsek:
            adim=1
        else:
            adim=-1
        for aci in range(guncel_dirsek, sayi_dirsek + adim, adim):
            dirsek_motoru.write(aci)
            time.sleep(HIZ)
        guncel_dirsek=sayi_dirsek
        print(f"dirsek motoru {sayi_dirsek} dereceye döndü")
    print("kol hareket ettirildi")
